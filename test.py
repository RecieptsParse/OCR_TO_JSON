import unittest
import product_database
import vendor_database
import search
import convert
import prompt_examples
import faiss
import langchain
import pickle
import os

class TestConvert(unittest.TestCase):
    # TestCase's are defined for functions in convert.py in order of appearance
    
    # setUp the attributes needed for the tests
    def setUp(self):
        self.prompt_prefix = '''You are a capable large language model. Your task is to extract data from a given receipt and format it into the JSON schema below. Use the default values if you're not sure. Try to infer a value for the field: unabbreviatedDescription. The values for the fields "description" and "unnabbreviatedDescription" can not be the same. Please wrap all numeric values in double-quotes. Some items may be priced at a weighted rate, such as "per pound" or "per ounce". Text can be used for multiple fields. Please use double-quotes for all string values. If there are double-quotes inside string values, please escape those characters with the "\" character.
    
    {format_instructions}
    
    '''
        self.format_instructions = 'The output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n```\n{"$defs": {"Item": {"properties": {"description": {"description": "item name", "title": "Description", "type": "string"}, "unabbreviatedDescription": {"default": "", "description": "unabbreviated name of field:description", "title": "Unabbreviateddescription", "type": "string"}, "includedItems": {"items": {"type": "string"}, "title": "Includeditems", "type": "array"}, "quantity": {"default": 0, "description": "number of items", "title": "Quantity", "type": "integer"}, "unitPrice": {"default": 0.0, "description": "cost per unit", "title": "Unitprice", "type": "number"}, "totalPrice": {"default": 0.0, "description": "total cost of unit(s) purchased", "title": "Totalprice", "type": "number"}, "discountAmount": {"default": 0.0, "description": "discount for item", "title": "Discountamount", "type": "number"}}, "required": ["description"], "title": "Item", "type": "object"}}, "properties": {"merchant": {"description": "name of merchant", "title": "Merchant", "type": "string"}, "address": {"description": "address", "title": "Address", "type": "string"}, "city": {"description": "city", "title": "City", "type": "string"}, "state": {"description": "state", "title": "State", "type": "string"}, "phoneNumber": {"description": "phone number", "title": "Phonenumber", "type": "string"}, "receiptDate": {"description": "purchase date", "title": "Receiptdate", "type": "string"}, "receiptTime": {"description": "time purchased", "title": "Receipttime", "type": "string"}, "totalItems": {"description": "number of items", "title": "Totalitems", "type": "integer"}, "diningOptions": {"default": "", "description": "here or to-go items for consumable items", "title": "Diningoptions", "type": "string"}, "paymentType": {"default": "cash", "description": "payment method", "title": "Paymenttype", "type": "string"}, "creditCardType": {"default": "", "description": "credit card type", "title": "Creditcardtype", "type": "string"}, "totalDiscount": {"default": 0.0, "description": "total discount", "title": "Totaldiscount", "type": "number"}, "tax": {"description": "tax amount", "title": "Tax", "type": "number"}, "total": {"description": "total amount paid", "title": "Total", "type": "number"}, "ITEMS": {"items": {"$ref": "#/$defs/Item"}, "title": "Items", "type": "array"}}, "required": ["merchant", "address", "city", "state", "phoneNumber", "receiptDate", "receiptTime", "totalItems", "tax", "total", "ITEMS"]}\n```'        
        self.example_prompt = convert.get_example_prompt()
        self.receiptParser = convert.make_receiptParser()
        self.fewshot_prompt = convert.make_fewshot_prompt(self.format_instructions)
        self.model = convert.make_model()
        
    def test_validate_float_Item(self):
        self.assertEqual(convert.Item.validate_float_Item("<UNKNOWN>"), 0.00)
        self.assertEqual(convert.Item.validate_float_Item("7.7"), 7.7)
        self.assertEqual(convert.Item.validate_float_Item(3.33), 3.33)
        self.assertEqual(convert.Item.validate_float_Item(5),5.0)
    
    def test_validate_quantity(self):
        self.assertEqual(convert.Item.validate_quantity("<UNKNOWN>"), 0)
        self.assertEqual(convert.Item.validate_quantity("7.1"), 8)
        self.assertEqual(convert.Item.validate_quantity("7"), 7)
        self.assertEqual(convert.Item.validate_quantity(3.33), 4)
        self.assertEqual(convert.Item.validate_quantity(5),5)
        self.assertEqual(convert.Item.validate_quantity(5),5.0)

    def test_validate_string_Item(self):
        self.assertEqual(convert.Item.validate_string_Item("<UNKNOWN>"), "")
        self.assertEqual(convert.Item.validate_string_Item("UNKNOWN"), "")
        self.assertEqual(convert.Item.validate_string_Item("UNKNOWN orange"), "orange")
        self.assertEqual(convert.Item.validate_string_Item("Apple    banana   \n"), "Apple banana")
        self.assertEqual(convert.Item.validate_string_Item("grape"), "grape")
    
    def test_validate_includedItems(self):
        test_array = convert.Item.validate_includedItems(["", "<UNKNOWN>", "UNKNOWN grape", "Apple     banana", "orange"])
        self.assertTrue(len(test_array), 3)
        self.assertEqual(test_array[0], "grape")
        self.assertEqual(test_array[1], "Apple banana")
        self.assertEqual(test_array[2], "orange")

    def test_validate_totalItems(self):
        self.assertEqual(convert.ReceiptInfo.validate_totalItems("<UNKNOWN>"), 0)
        self.assertEqual(convert.ReceiptInfo.validate_totalItems("7.1"), 8)
        self.assertEqual(convert.ReceiptInfo.validate_totalItems("7"), 7)
        self.assertEqual(convert.ReceiptInfo.validate_totalItems(3.33), 4)
        self.assertEqual(convert.ReceiptInfo.validate_totalItems(5),5)
        self.assertEqual(convert.ReceiptInfo.validate_totalItems(5),5.0)
        
    def test_validate_paymentType(self):
        self.assertEqual(convert.ReceiptInfo.validate_paymentType("<UNKNOWN>"), 'cash')
        self.assertEqual(convert.ReceiptInfo.validate_paymentType("<CARD>"), 'credit')
        self.assertEqual(convert.ReceiptInfo.validate_paymentType("credit"), 'credit')
        self.assertEqual(convert.ReceiptInfo.validate_paymentType("Visa"), "credit")
        self.assertEqual(convert.ReceiptInfo.validate_paymentType("debit"), "debit")
        self.assertEqual(convert.ReceiptInfo.validate_paymentType(0), 'cash')
        self.assertEqual(convert.ReceiptInfo.validate_paymentType(1.2), 'cash')

    def test_validate_diningOptions(self):
        self.assertEqual(convert.ReceiptInfo.validate_diningOptions("HERE"), "DINE IN")
        self.assertEqual(convert.ReceiptInfo.validate_diningOptions("DINE CREDIT"), "DINE IN")
        self.assertEqual(convert.ReceiptInfo.validate_diningOptions("Delivery"), "TO GO")
        self.assertEqual(convert.ReceiptInfo.validate_diningOptions("for go"), "TO GO")
        self.assertEqual(convert.ReceiptInfo.validate_diningOptions("<UNKNOWN>"), "")
    
    def test_validate_float_ReceiptInfo(self):
        self.assertEqual(convert.ReceiptInfo.validate_float_ReceiptInfo("<UNKNOWN>"), 0.00)
        self.assertEqual(convert.ReceiptInfo.validate_float_ReceiptInfo("7.7"), 7.7)
        self.assertEqual(convert.ReceiptInfo.validate_float_ReceiptInfo(3.33), 3.33)
        self.assertEqual(convert.ReceiptInfo.validate_float_ReceiptInfo(5),5.0)
    
    def test_validate_string_ReceiptInfo(self):
        self.assertEqual(convert.ReceiptInfo.validate_string_ReceiptInfo("<UNKNOWN>"), "")
        self.assertEqual(convert.ReceiptInfo.validate_string_ReceiptInfo("UNKNOWN"), "")
        self.assertEqual(convert.ReceiptInfo.validate_string_ReceiptInfo("UNKNOWN orange"), "orange")
        self.assertEqual(convert.ReceiptInfo.validate_string_ReceiptInfo("Apple    banana   \n"), "Apple banana")
        self.assertEqual(convert.ReceiptInfo.validate_string_ReceiptInfo("grape"), "grape")
        
    def test_get_prompt_prefix(self):
        prefix = self.prompt_prefix
        self.assertEqual(convert.get_prompt_prefix(), prefix)

    def test_get_example_prompt(self):
        example_prompt = self.example_prompt
        input_variables = example_prompt.input_variables
        self.assertTrue(isinstance(example_prompt, langchain.prompts.prompt.PromptTemplate))
        self.assertFalse(isinstance(example_prompt, str))
        self.assertEqual(input_variables[0], 'ExampleInput')
        self.assertEqual(input_variables[1], 'ExampleOutput')
        self.assertTrue(len(input_variables) == 2)
        self.assertEqual(example_prompt.template, "input:\n{ExampleInput}\noutput:\n{ExampleOutput}")        
        
    def test_get_suffix(self):
        self.assertEqual(convert.get_suffix(), "input:\n{input}\noutput:\n")
        
    def test_make_receiptParser(self):
        self.assertTrue(isinstance(self.receiptParser, langchain.output_parsers.pydantic.PydanticOutputParser))
        self.assertEqual(self.receiptParser.get_format_instructions(), self.format_instructions)
    
    def test_make_fewshot_prompt(self):
        fewshot_prompt = self.fewshot_prompt
        self.assertTrue(isinstance(fewshot_prompt, langchain.prompts.few_shot.FewShotPromptTemplate))
        
        # input_variables
        self.assertTrue(isinstance(fewshot_prompt.input_variables, list))
        self.assertEqual(len(fewshot_prompt.input_variables), 1)
        self.assertEqual(fewshot_prompt.input_variables[0], 'input')
        
        # partial_variables
        self.assertTrue(isinstance(fewshot_prompt.partial_variables, dict))
        self.assertEqual(len(fewshot_prompt.partial_variables), 1)
        self.assertEqual(list(fewshot_prompt.partial_variables.keys())[0], 'format_instructions')
        self.assertEqual(fewshot_prompt.partial_variables['format_instructions'], self.format_instructions)
        
        # examples is tested in test_get_prompt_examples()
        
        # example_prompt is tested in test_get_example_prompt()
        
        # example_separator
        self.assertEqual(fewshot_prompt.example_separator, '\n')
        
        # suffix is tested in test_get_suffix()
        
    def test_make_model(self):
        self.assertTrue(isinstance(self.model, langchain.chat_models.openai.ChatOpenAI))
        self.assertEqual(self.model.model_name, 'gpt-3.5-turbo-16k')
        self.assertEqual(self.model.temperature, 1.00)
        self.assertEqual(self.model.openai_api_key, "INSERT_OPENAI_API KEY")
        
    # make_chain() is not tested due to it being composed of the return values of other functions that are tested

class TestPromptExamples(unittest.TestCase):
    # TestCase for the singular getter method in prompt_examples.py
    
    def test_get_prompt_examples(self):
        examples = prompt_examples.get_prompt_examples()
        self.assertTrue(isinstance(examples, list))
        self.assertEqual(len(examples), 7)
        self.assertEqual(examples[0], {"ExampleInput": prompt_examples.example_1_input, "ExampleOutput": prompt_examples.example_1_output})

class TestVendorDatabase(unittest.TestCase):
    # TestCase for the file: vendor_database.py
    
    # setUp the class attributes for the tests
    def setUp(self):
        self.vendor_index_path = 'vendor_embeddings.index'
        self.vendor_mapping_path = 'vendor_mapping.pk1'
        vendor_database.make_vendor_database()

    def test_make_vendor_database(self):
        # Test if the index file was created
        if os.path.exists(self.vendor_index_path):
            index = faiss.read_index(self.vendor_index_path)
            self.assertTrue(isinstance(index, faiss.swigfaiss.IndexFlat))
            os.remove(self.vendor_index_path)
        else:
            raise Exception(f"{self.vendor_index_path} does not exist")
        
        # Test if the mapping file was created
        if os.path.exists(self.vendor_mapping_path):
            with open(self.vendor_mapping_path, 'rb') as f:
                vendor_mapping = pickle.load(f)
                self.assertEqual(len(vendor_mapping), 144)
                self.assertEqual(vendor_mapping[15], 'Grocery and Supermarkets')
                self.assertEqual(vendor_mapping[30], 'Restaurants and Food Services')
                self.assertEqual(vendor_mapping[45], 'Clothing and Apparel')
                self.assertEqual(vendor_mapping[70], 'Health and Beauty')
                self.assertEqual(vendor_mapping[90], 'Electronics and Appliances')
                self.assertEqual(vendor_mapping[110], 'Home and Garden')
                self.assertEqual(vendor_mapping[140], 'Entertainment and Leisure')
            os.remove(self.vendor_mapping_path)
        else:
            raise Exception(f"{self.vendor_mapping_path} does not exist")

class TestProductDatabase(unittest.TestCase):
    # TestCase for the file: product_database.py
    
    # setUp the class attributes for the tests
    def setUp(self):
        self.product_index_path = 'product_embeddings.index'
        self.product_mapping_path = 'product_mapping.pk1'
        product_database.make_product_database()
    
    def test_make_product_database(self):       
        # Test if the index file was created
        if os.path.exists(self.product_index_path):
            index = faiss.read_index(self.product_index_path)
            self.assertTrue(isinstance(index, faiss.swigfaiss.IndexFlat))
            os.remove(self.product_index_path)
        else:
            raise Exception(f"{self.product_index_path} does not exist")
        
        # Test if the mapping file was created
        if os.path.exists(self.product_mapping_path):
            with open(self.product_mapping_path, 'rb') as f:
                product_mapping = pickle.load(f)
                self.assertEqual(len(product_mapping), 145)
                self.assertEqual(product_mapping[0], 'Food Products')
                self.assertEqual(product_mapping[10], 'Beverages')
                self.assertEqual(product_mapping[20], 'Health And Beauty')
                self.assertEqual(product_mapping[30], 'Clothing And Accessories')
                self.assertEqual(product_mapping[38], 'Electronics')
                self.assertEqual(product_mapping[45], 'Home')
                self.assertEqual(product_mapping[55], 'Outdoor Goods')
                self.assertEqual(product_mapping[65], 'Automotive')
                self.assertEqual(product_mapping[75], 'Toys And Games')
                self.assertEqual(product_mapping[85], 'Sporting Goods')
                self.assertEqual(product_mapping[95], 'Books And Stationery')
                self.assertEqual(product_mapping[100], 'Pharmacy And Health Products')
                self.assertEqual(product_mapping[110], 'Pet Supplies')
                self.assertEqual(product_mapping[120], 'Baby Products')
                self.assertEqual(product_mapping[125], 'Cleaning Supplies')
                self.assertEqual(product_mapping[135], 'Gifts And Miscellaneous')
                self.assertEqual(product_mapping[144], 'Event Tickets')
                os.remove(self.product_mapping_path)
        else:
            raise Exception(f"{self.product_mapping_path} does not exist")

class TestSearch(unittest.TestCase):
    # TestCase for the file: search.py
    
    def setUp(self):
        vendor_database.make_vendor_database()
        product_database.make_product_database()
        self.vendor_classifier = search.get_classifier('vendor')
        self.product_classifier = search.get_classifier('product')
        
    def test_load_resources(self):
        self.vendor_classifier.load_resources()
        self.product_classifier.load_resources()
        # Check index attributes
        self.assertTrue(isinstance(self.vendor_classifier.index, faiss.swigfaiss.IndexFlat))
        self.assertTrue(isinstance(self.product_classifier.index, faiss.swigfaiss.IndexFlat))
        
        # Check vendor_classifier mapping attribute
        vendor_mapping = self.vendor_classifier.mapping
        self.assertEqual(len(vendor_mapping), 144)
        self.assertEqual(vendor_mapping[15], 'Grocery and Supermarkets')
        self.assertEqual(vendor_mapping[30], 'Restaurants and Food Services')
        self.assertEqual(vendor_mapping[45], 'Clothing and Apparel')
        self.assertEqual(vendor_mapping[70], 'Health and Beauty')
        self.assertEqual(vendor_mapping[90], 'Electronics and Appliances')
        self.assertEqual(vendor_mapping[110], 'Home and Garden')
        self.assertEqual(vendor_mapping[140], 'Entertainment and Leisure')
        
        
        # Check product_classifier mapping attribute
        product_mapping = self.product_classifier.mapping
        self.assertEqual(len(product_mapping), 145)
        self.assertEqual(product_mapping[0], 'Food Products')
        self.assertEqual(product_mapping[10], 'Beverages')
        self.assertEqual(product_mapping[20], 'Health And Beauty')
        self.assertEqual(product_mapping[30], 'Clothing And Accessories')
        self.assertEqual(product_mapping[38], 'Electronics')
        self.assertEqual(product_mapping[45], 'Home')
        self.assertEqual(product_mapping[55], 'Outdoor Goods')
        self.assertEqual(product_mapping[65], 'Automotive')
        self.assertEqual(product_mapping[75], 'Toys And Games')
        self.assertEqual(product_mapping[85], 'Sporting Goods')
        self.assertEqual(product_mapping[95], 'Books And Stationery')
        self.assertEqual(product_mapping[100], 'Pharmacy And Health Products')
        self.assertEqual(product_mapping[110], 'Pet Supplies')
        self.assertEqual(product_mapping[120], 'Baby Products')
        self.assertEqual(product_mapping[125], 'Cleaning Supplies')
        self.assertEqual(product_mapping[135], 'Gifts And Miscellaneous')
        self.assertEqual(product_mapping[144], 'Event Tickets')
        
    # Check the KNN search() function for classification
    def test_search(self):
        self.assertEqual(self.vendor_classifier.search("mcDonalds hamburger meal take-out fries", 5), 'Restaurants and Food Services')
        self.assertEqual(self.product_classifier.search("organic apples", 5), 'Food Products')
        self.assertFalse(self.vendor_classifier.search("mcDonalds hamburger meal take-out fries", 5) == 'Grocery and Supermarkets')
        self.assertFalse(self.product_classifier.search("organic apples", 5) == 'Beverages')

    def tearDown(self):
        # Remove the index and mapping files
        if os.path.exists(self.vendor_classifier.index_path):
            os.remove(self.vendor_classifier.index_path)
        if os.path.exists(self.vendor_classifier.mapping_path):
            os.remove(self.vendor_classifier.mapping_path)
        if os.path.exists(self.product_classifier.index_path):
            os.remove(self.product_classifier.index_path)
        if os.path.exists(self.product_classifier.mapping_path):
            os.remove(self.product_classifier.mapping_path)  

    # get_classifier() is not tested, as its proper function is integral for the rest of the tests.
    # Should get_classifier() fail, the other tests will fail as well as a domino effect.

    # query_classification() is not tested, as its constituent functions are tested above          
          
if __name__ == "__main__":
    unittest.main(verbosity=2)