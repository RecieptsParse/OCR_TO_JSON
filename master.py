import vendor_database
import product_database
import search
import convert
import os
import json
import pandas as pd
import csv

'''
Convert raw receipt text to JSON objects and store the JSON objects as strings in 
'''

# receipts_folder = "data/receipts/ner_evaluate" # the folder that contains raw receipt text files to convert to JSON

# openai_api_key="INSERT_OPENAI_API_KEY"

# # Set up the main components of the JSON conversion process
# receiptParser = convert.make_receiptParser()
# fewshot_prompt = convert.make_fewshot_prompt(receiptParser.get_format_instructions())
# model = convert.make_model(model="gpt-3.5-turbo-16k", temperature=1.00, openai_api_key=openai_api_key)
# chain = convert.make_chain(fewshot_prompt, model, receiptParser)

# # Iterate through receipts_folder, and convert each receipt to a JSON object
# print(os.listdir(receipts_folder)) # DELETE ME LATER
# for filename in os.listdir(receipts_folder):
#     if filename.endswith('.txt'):
#         with open(os.path.join(receipts_folder, filename)) as f:
#             data = f.read()
#             print()
#             print(f'reading from {filename}')
#             response = chain.invoke({"input": data})
#             # with 'a' in open() it will create or append to current file
#             with open('receipts_json.json', 'a') as fp: # Write each JSON object as it gets parsed
#                     # write each receipt JSON on a new line
#                     fp.write(json.dumps({"ReceiptInfo": json.loads(response.model_dump_json())}) + "\n")
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

# def read_one(json_object):
#     dataframe = pd.DataFrame()
#     for i in range(len(json_object)):
#         query_string = ""
#         one_reciept = json_object[i]
#         merchant_name = one_reciept['merchant']
#         query_string += f'{merchant_name} '
#         diining_option = one_reciept['diningOptions']
#         query_string += f'{diining_option} '
#         for j in range(len(one_reciept['ITEMS'])):
#             query_string += one_reciept['ITEMS'][j]['unabbreviatedDescription']

#         top_vendor = search.query_classification(query_string, 5, "vendor")
#         print(f'- {i} Vendor Prediction {top_vendor}')
#         print(f'Query: {query_string}')
#         items_for_receipt = one_reciept['ITEMS']
#         for j in range(len(one_reciept['ITEMS'])):
#              product_query = items_for_receipt[j]['unabbreviatedDescription']
#              top_product = search.query_classification(product_query, 10, "product")
#              print(f' {j} Item: {product_query} category: {top_product}')

# write to txt

def read_one(json_object):
    with open('output.txt', 'a') as file:
        for i in range(len(json_object)):
            query_string = ""
            one_reciept = json_object[i]
            merchant_name = one_reciept['merchant']
            query_string += f'{merchant_name} '
            dining_option = one_reciept['diningOptions']
            query_string += f'{dining_option} '
            for j in range(len(one_reciept['ITEMS'])):
                items_unabbre = one_reciept['ITEMS'][j]['unabbreviatedDescription']
                item_abbre = one_reciept['ITEMS'][j]['description']
                query_string += f' {items_unabbre} {item_abbre} '

            top_vendor = search.query_classification(query_string, 5, "vendor")
            file.write(f'- {i} Vendor Prediction {top_vendor}\n')
            file.write(f'Query: {query_string}\n')
            items_for_receipt = one_reciept['ITEMS']
            for j in range(len(one_reciept['ITEMS'])):
                product_query = items_for_receipt[j]['unabbreviatedDescription']
                descr = items_for_receipt[j]['description']
                product_query += f' {descr} {merchant_name}' 
                top_product = search.query_classification(product_query, 10, "product")
                file.write(f' {j} Item: {product_query} category: {top_product}\n')

# write to csv
"""DID NOT TEST YET"""
# def read_one(json_object):
#     with open('output.csv', 'a',newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Number','Vendor','Item'])
#         for i in range(len(json_object)):
#             query_string = ""
#             one_reciept = json_object[i]
#             merchant_name = one_reciept['merchant']
#             query_string += f'{merchant_name} '
#             dining_option = one_reciept['diningOptions']
#             query_string += f'{dining_option} '
#             for j in range(len(one_reciept['ITEMS'])):
#                 items = one_reciept['ITEMS'][j]['unabbreviatedDescription']
#                 query_string += f'{items} '

#             top_vendor = search.query_classification(query_string, 5, "vendor")
#             items_for_receipt = one_reciept['ITEMS']
#             for j in range(len(one_reciept['ITEMS'])):
#                 arr = [i,top_vendor]
#                 product_query = items_for_receipt[j]['unabbreviatedDescription']
#                 descr = items_for_receipt[j]['description']
#                 product_query += f' {descr} {merchant_name}' 
#                 top_product = search.query_classification(product_query, 4, "product")
#                 arr.append(top_product)
#                 writer.writerow(arr)     


# {Merchant} {First Item} {diningOptions} {SecondItem}

json_obj = read_json_receipts('all_receipts_json.json')

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
print("PROGRAM END")