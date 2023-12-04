# import vendor_database
# import product_database
# import search
import convert
import os
import json

'''
FIX DOCUMENTATION LATER: JSON OBJECT CONVERSION PHASE
This code has not been tested yet.
'''
receipts_folder = "data/receipts/text_0"

openai_api_key="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"

receiptParser = convert.make_receiptParser()
fewshot_prompt = convert.make_fewshot_prompt(receiptParser.get_format_instructions())
model = convert.make_model(model="gpt-3.5-turbo-16k", temperature=1.00, openai_api_key=openai_api_key)
chain = convert.make_chain(fewshot_prompt, model, receiptParser)

# data='''GAP OUTLET <UNKNOWN> 02392
# 20 CITY <UNKNOWN> SPACE 1560
# ORANGE CA 92868
# Tel. (714) 938-9970
# 03/15/2023
# 02:20:54 PM
# Trans.: 1868
# Store: 02392
# <UNKNOWN>
# Cashier: 3150109
# Valid No: 1683
# SALE
# 023923031868202303151683
# GapKids <UNKNOWN> Disney Mickey Mouse
# 17.49 T
# Graphic T-Shirt
# 597883-001-0202
# 24.99
# Item Discount 30.0%
# -7.50
# 30 %-SS LICENSE
# GapKids &#124 Disney Mickey Mouse
# <UNKNOWN>
# Graphic T-Shirt
# 597883-001-0502
# <UNKNOWN>
# Item Discount 30.0%
# -7.50
# 30 %-SS LICENSE
# Gap <UNKNOWN> Star Wars&#153 4" Boxers
# 4.19 T
# 401675-001-0002
# 1 6.99
# Item Discount 40.0%
# -2.80
# 40% MKDS
# Total Discount
# 17.80
# Subtotal
# 39.17
# T1 Taxable Amount
# 39.17
# T1 (7.75%) Tax
# 3.04
# Total Tax
# 3.04
# Total
# 42.21
# Cash
# 50.00
# Total Tender
# 50.00
# Change Due
# -7.79
# We would love to hear your feedback!
# Please take our two <UNKNOWN> survey:
# <UNKNOWN>
# Unwashed and unworn <UNKNOWN>
# accompanied by an original sales
# <UNKNOWN> may be returned to any U.S.
# store within 30 days of purchase for
# full refund in original form of <UNKNOWN>
# A one-time price adjustment may be nade
# within 14 days of purchase with an
# original receipt. Final Sale items are not eligible for
# returns or adjustments.
# Gap Outlet Store merchandise cannot
# be returned at a Gap Store.
# Valid photo ID required for unreceipted returns.
# Exchange or merchandise return card for
# current selling price. Information from
# your ID may be captured and retained by
# <UNKNOWN> third-party provider Gap Outlet
# uses to authorize returns and prevent
# fraud. For inquiries, call
# 1-800-652-2331 or visit theretailequation.com
# Additional terms and restrictions apply.
# See store for full return policy details.'''

# print(data)
# response = chain.invoke({"input": data})
# print(response)
# with open('receipts_json.text', 'a') as fp:
#     fp.write(response.model_dump_json() + "\n")
    

json_objects = []
for filename in os.listdir(receipts_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(receipts_folder, filename)) as f:
            data = f.read()
            print()
            print(f"reading from: {filename}")
            print(data)
            response = chain.invoke({"input": data})
            print()
            print(response.model_dump_json())
            # json_objects.append(response.model_dump_json())
            with open('receipts_json.txt', 'a') as fp:
                fp.write(response.model_dump_json() + "\n")
            print(f"finished reading from :{filename}")

# with open('receipts_json.txt', 'w') as fp:
#     for receipt in json_objects:
#         # write each receipt JSON on a new line
#         fp.write("%s\n" % receipt)
#     print('Done')

            
# '''
# saves faiss index and mapping to directory 
# model for embeddings & descriptions can be updated in config.py
# '''
# vendor_database.make_vendor_database()
# product_database.make_product_database()

# # Example usage for vendors
# vendor_query = "mcDonalds hamburger meal take-out fries"
# top_vendor = search.query_classification(vendor_query, 5, "vendor")

# # Example usage for products
# product_query = "organic apples"
# top_product = search.query_classification(product_query, 10, "product")

# print(top_product,top_vendor,sep="\n")
