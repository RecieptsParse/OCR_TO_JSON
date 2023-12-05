import vendor_database
import product_database
import search
import convert
import os
import json
import pandas as pd

'''
FIX DOCUMENTATION LATER: JSON OBJECT CONVERSION PHASE
This code has not been tested yet.
'''

receipts_folder = "data/receipts/text_3and4" # the receipt folder should have two subfolders of images and text
# ^currently running batches of raw txt files, in the same folder as the complete data/receipts/text folder

# receipts_folder = "data/receipts/text_1" # the receipt folder should have two subfolders of images and text
# # ^currently running batches of raw txt files, in the same folder as the complete data/receipts/text folder


# openai_api_key="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"


receiptParser = convert.make_receiptParser()
fewshot_prompt = convert.make_fewshot_prompt(receiptParser.get_format_instructions())
model = convert.make_model(model="gpt-3.5-turbo-16k", temperature=1.00, openai_api_key=openai_api_key)
chain = convert.make_chain(fewshot_prompt, model, receiptParser)

for filename in os.listdir(receipts_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(receipts_folder, filename)) as f:
            data = f.read()
            # IF DEBUGGING IS NEEDED
            print()
            print(f'reading from {filename}')
            # print(data)
            response = chain.invoke({"input": data})

# receiptParser = convert.make_receiptParser()
# fewshot_prompt = convert.make_fewshot_prompt(receiptParser.get_format_instructions())
# model = convert.make_model(model="gpt-3.5-turbo-16k", temperature=1.00, openai_api_key=openai_api_key)
# chain = convert.make_chain(fewshot_prompt, model, receiptParser)

# for filename in os.listdir(receipts_folder):
#     if filename.endswith('.txt'):
#         with open(os.path.join(receipts_folder, filename)) as f:
#             data = f.read()
#             # IF DEBUGGING IS NEEDED
#             # print()
#             # print(f'reading from {filename}')
#             # print(data)
#             response = chain.invoke({"input": data})
#             # with 'a' in open it will create or append to current file
#             with open('all_receipts_json.json', 'a') as fp: # Write each JSON object as it gets parsed
#                     # write each receipt JSON on a new line
#                     fp.write(response.model_dump_json() + "\n")
#     print('Done')

            
'''
saves faiss index and mapping to directory 
model for embeddings & descriptions can be updated in config.py
'''
vendor_database.make_vendor_database()
product_database.make_product_database()


"""
Get JSON and search for fields (Merchant, First Item, DiningOption, Second Itemm) -- Similar to Assignment 1
"""

"""
NEED TO TEST
"""
def read_json_receipts(file_path):
    with open(file_path, 'r') as f:
         lines = f.readlines()
    json_objects = []
    for line in lines:
         json_object = json.loads(line)
         json_objects.append(json_object)
    return json_objects

def read_one(json_object):
    dataframe = pd.DataFrame()
    for i in range(len(json_object)):
        print(i)
        query_string = ""
        one_reciept = json_object[i]
        merchant_name = one_reciept['merchant']
        query_string += f'{merchant_name} '
        diining_option = one_reciept['diningOptions']
        query_string += f'{diining_option} '
        for j in range(len(one_reciept['ITEMS'])):
            query_string += one_reciept['ITEMS'][j]['unabbreviatedDescription']

        top_vendor = search.query_classification(query_string, 5, "vendor")
        print(f'{top_vendor}')
        items_for_receipt = one_reciept['ITEMS']
        for j in range(len(one_reciept['ITEMS'])):
             product_query = items_for_receipt[j]['unabbreviatedDescription']
             top_product = search.query_classification(product_query, 10, "product")
             print(f' {j} Item: {product_query} category: {top_product}')

"""
Proposed: Data Structure

|      | Vendor Category | Item1_Product category | Item2_Product Category | Item2_ Product Category |  
|   1  |                 |                        |                        |                         | 
|   2  |                 |                        |                        |                         |
"""         


# {Merchant} {First Item} {diningOptions} {SecondItem}

json_obj = read_json_receipts('all_receipts_json.json')
print(json_obj)

read_one(json_obj)

# vendor_query  = "mcDonalds hamburger meal take-out fries"
# top_vendor = search.query_classification(vendor_query, 5, "vendor")

"""
Get JSON and search for items (iterate through all items) -- Simlilar to Assignmnet 1
"""
# Items in JSON 
# product_query = "organic apples"
# top_product = search.query_classification(product_query, 10, "product")

# print(top_product,top_vendor,sep="\n")
