import vendor_database
import product_database
import search
import convert
import os

'''
FIX DOCUMENTATION LATER: JSON OBJECT CONVERSION PHASE
This code has not been tested yet.
'''
receipts_folder = "data/receipts/text_1" # the receipt folder should have two subfolders of images and text
# ^currently running batches of raw txt files, in the same folder as the complete data/receipts/text folder

openai_api_key="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"


receiptParser = convert.make_receiptParser()
fewshot_prompt = convert.make_fewshot_prompt(receiptParser.get_format_instructions())
model = convert.make_model(model="gpt-3.5-turbo-16k", temperature=1.00, openai_api_key=openai_api_key)
chain = convert.make_chain(fewshot_prompt, model, receiptParser)

for filename in os.listdir(receipts_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(receipts_folder, filename)) as f:
            data = f.read()
            # IF DEBUGGING IS NEEDED
            # print()
            # print(f'reading from {filename}')
            # print(data)
            response = chain.invoke({"input": data})
            with open('receipts_json.text', 'w') as fp: # Write each JSON object as it gets parsed
                    # write each receipt JSON on a new line
                    fp.write(response.model_dump_json() + "\n")
    print('Done')

            
'''
saves faiss index and mapping to directory 
model for embeddings & descriptions can be updated in config.py
'''
vendor_database.make_vendor_database()
product_database.make_product_database()


"""
Get JSON and search for fields (Merchant, First Item, DiningOption, Second Itemm) -- Similar to Assignment 1
"""
# {Merchant} {First Item} {diningOptions} {SecondItem}
vendor_query = "mcDonalds hamburger meal take-out fries"
top_vendor = search.query_classification(vendor_query, 5, "vendor")

"""
Get JSON and search for items (iterate through all items) -- Simlilar to Assignmnet 1
"""
# Items in JSON 
product_query = "organic apples"
top_product = search.query_classification(product_query, 10, "product")

print(top_product,top_vendor,sep="\n")
