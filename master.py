import vendor_database
import product_database
import search
import convert
import os
import json
import pandas as pd
import csv


'''
saves faiss index and mapping to directory 
model for embeddings & descriptions can be updated in config.py
'''
vendor_database.make_vendor_database()
product_database.make_product_database()

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
#     print('Done Converting Reciept Text')


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

def classify(json_receipts):
    with open('output.txt', 'a') as file:

        #loops thru receipt objects 
        for i, receipt in enumerate(json_receipts):
            merchant_name = receipt['merchant']
            dining_option = receipt['diningOptions']
            vendor_query = [f"{merchant_name} {dining_option}"]

            #loops thru items in receipt
            for item in receipt['ITEMS']:
                items_unabbr = item['unabbreviatedDescription']
                item_description = item['description']
                vendor_query.append(f"{items_unabbr} {item_description}")
            
            #processes query string, then classifies vendor, writes to file
            query_string = " ".join(vendor_query)
            top_vendor = search.query_classification(query_string, 5, "vendor")
            file.write(f"- {i} Vendor Prediction {top_vendor}\nQuery: {query_string}\n")

            #process query string, then classifies product, write to file
            for j, item in enumerate(receipt['ITEMS']):
                product_query = f"{item['unabbreviatedDescription']} {item['description']} {merchant_name}"
                top_product = search.query_classification(product_query, 10, "product")
                file.write(f" {j} Item: {product_query} category: {top_product}\n")


# write to txt
# def read_one(json_object):
#     with open('output.txt', 'a') as file:
#         for i in range(len(json_object)):
#             query_string = ""
#             one_reciept = json_object[i]
#             merchant_name = one_reciept['merchant']
#             query_string += f'{merchant_name} '
#             dining_option = one_reciept['diningOptions']
#             query_string += f'{dining_option} '
#             for j in range(len(one_reciept['ITEMS'])):
#                 items_unabbre = one_reciept['ITEMS'][j]['unabbreviatedDescription']
#                 item_abbre = one_reciept['ITEMS'][j]['description']
#                 query_string += f' {items_unabbre} {item_abbre} '

#             top_vendor = search.query_classification(query_string, 5, "vendor")
#             file.write(f'- {i} Vendor Prediction {top_vendor}\n')
#             file.write(f'Query: {query_string}\n')
#             items_for_receipt = one_reciept['ITEMS']
#             for j in range(len(one_reciept['ITEMS'])):
#                 product_query = items_for_receipt[j]['unabbreviatedDescription']
#                 descr = items_for_receipt[j]['description']
#                 product_query += f' {descr} {merchant_name}' 
#                 top_product = search.query_classification(product_query, 10, "product")
#                 file.write(f' {j} Item: {product_query} category: {top_product}\n')

json_obj = read_json_receipts('all_receipts_json.json')
classify(json_obj)
#read_one(json_onj)
print("PROGRAM END")