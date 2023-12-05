import unittest
import product_database
import vendor_database
import search
import convert
import langchain
import pickle
import os

class TestConvertMethods(unittest.TestCase):
    def setUp(self):
        self.example_prompt = convert.get_example_prompt()
        self.receiptParser = convert.make_receiptParser()
        self.fewshot_prompt = convert.make_fewshot_prompt(self.receiptParser.get_format_instructions())
        self.model = convert.make_model()
        
    # do we test classes???
    
    def test_get_prompt_prefix(self):
        expected_prefix = '''You are a capable large language model. Your task is to extract data from a given receipt and format it into the JSON schema below. Use the default values if you're not sure. Try to infer a value for the field: unabbreviatedDescription. The values for the fields "description" and "unnabbreviatedDescription" can not be the same. Please wrap all numeric values in double-quotes. Some items may be priced at a weighted rate, such as "per pound" or "per ounce". Text can be used for multiple fields. Please use double-quotes for all string values. If there are double-quotes inside string values, please escape those characters with the "\" character.
    
    {format_instructions}
    
    '''
        self.assertEqual(convert.get_prompt_prefix(), expected_prefix)

    def test_get_prompt_template(self):
        # Get the attr:example_prompt from self
        example_prompt = self.example_prompt
        
        # Type checking
        self.assertTrue(isinstance(example_prompt, langchain.prompts.prompt.PromptTemplate))
        self.assertFalse(isinstance(example_prompt, str))
        
        # Check attr:input_variables
        input_variables = example_prompt.input_variables
        self.assertEqual(input_variables[0], 'ExampleInput')
        self.assertEqual(input_variables[1], 'ExampleOutput')
        self.assertTrue(len(input_variables) == 2)
        
        # Check attr:template
        self.assertEqual(example_prompt.template, "input:\n{ExampleInput}\noutput:\n{ExampleOutput}")
        
    def test_get_suffix(self):
        self.assertEqual(convert.get_suffix(), "input:\n{input}\noutput:\n")

if __name__ == "__main__":
    unittest.main(verbosity=2)

# class product_database_test(unittest.TestCase):
# # assert ideas 
# #  [] check make sure same length/ same aount of entries --> checks to make sure it exists
#      def test_product(self):
#          make_product_database()
     
#      def load_data_from_pk1_file_product(self,file_path):
#         with open(file_path, 'rb') as f:
#             data = pickle.load(f)
#         return data
     
#      def test_load_data_from_pk1_file_product(self):
#         test_instance = product_database_test()
#         sample_data_product = {'key': 'value'} # need to review logic
#         with open('product_mapping.pk1', 'wb') as f:
#             pickle.dump(sample_data_product, f)
#         loaded_data_product = test_instance.load_data_from_pk1_file_product('product_mapping.pk1')

#         self.assertEqual(loaded_data_product, sample_data_product)
#         expected_entries = len(sample_data_product)
#         actual_entries = len(loaded_data_product)
#         self.assertEqual(actual_entries, expected_entries, 'failed actual entries')
#         print('here')
#         os.remove('product_mapping.pk1')


# class vendor_database_test(unittest.TestCase):
# # assert ideas 
# #  [] check make sure same length/ same aount of entries --> checks to make sure it exists
# #  [] 
#      def test_vendor(self):
#          make_vendor_database()
#          return 
#      def load_data_from_pk1_file_vendor(self,file_path):
#         with open(file_path, 'rb') as f:
#             data = pickle.load(f)
#         return data
     
#      def test_load_data_from_pk1_file_vendor(self):
#         test_instance = vendor_database_test()
#         sample_data_vendor = {'key': 'value'}
#         with open('vendor_mapping.pk1', 'wb') as f:
#             pickle.dump(sample_data_vendor, f)
#         loaded_data_vendor = test_instance.load_data_from_pk1_file_vendor('vendor_mapping.pk1')

#         self.assertEqual(loaded_data_vendor, sample_data_vendor, 'failed equal data')
#         expected_entries = len(sample_data_vendor)
#         actual_entries = len(loaded_data_vendor)
#         self.assertEqual(actual_entries, expected_entries,'failed equal vendor')
#         os.remove('vendor_mapping.pk1')

# class convert_unit(unittest.TestCase):
# # assert ideas 
# #  [] make sure converted correctly <-- get example JSON output and compare
# #  [] Check all the ambigous reciepts if classified correctly
# #          [] look through reciepts to determine the hard ones 
# # 
#      def test_vendor(self):
#         #  make_vendor_database()
#          return 
#      def load_data_from_pk1_file_vendor(self,file_path):
#         # with open(file_path, 'rb') as f:
#         #     data = pickle.load(f)
#         return data

# class search_unit(unittest.TestCase): 
# # assert ideas 
# #  - [] check to make sure get expected search result for items
# #         - check all categories
#     def test_vendor(self):
#         #  make_vendor_database()
#          return 
#     def load_data_from_pk1_file_vendor(self,file_path):
#         # with open(file_path, 'rb') as f:
#         #     data = pickle.load(f)
#         return data 

# class search_unit(unittest.TestCase): 
# #  - [] check to make sure get expected search result for vendors
# #         - check all categories
# #         
#     def test_vendor(self):
#          # make_vendor_database()
#          return 
#     def load_data_from_pk1_file_vendor(self,file_path):
#         # with open(file_path, 'rb') as f:
#         #     data = pickle.load(f)
#         return data 

# # convert
# # assert ideas:
# #  - check number of entries in txt files against # of files in folder
# #  - check converted correctly with example JSON from reciepts
