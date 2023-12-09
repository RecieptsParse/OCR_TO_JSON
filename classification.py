import search
import json
import pandas as pd

def read_json_receipts(file_path):
    with open(file_path, 'r') as f:
         lines = f.readlines()
    json_objects = []
    for line in lines:
         json_object = json.loads(line)
         json_objects.append(json_object)
    return json_objects

def classify(json_receipts):
    # Loops through receipt objects
    for receipt in json_receipts:
        merchant_name = receipt['ReceiptInfo']['merchant']
        dining_option = receipt['ReceiptInfo']['diningOptions']

        # Initialize vendor query with merchant name and dining option
        vendor_query = f"{merchant_name} {dining_option}"

        # Append item descriptions to the vendor query
        for item in receipt['ReceiptInfo']['ITEMS']:
            vendor_query += f" {item['description']} {item['unabbreviatedDescription']}"
        # Classify the vendor
        top_vendor = search.query_classification(vendor_query, 5, "vendor")
        #print(vendor_query, "\n", top_vendor)

        # Insert the vendor classification into the receipt
        receipt['ReceiptInfo']['vendorClassification'] = top_vendor

        # Loops through items in receipt
        for item in receipt['ReceiptInfo']['ITEMS']:
            product_query = f"{item['unabbreviatedDescription']} {item['description']} {merchant_name}"
            top_product = search.query_classification(product_query, 10, "product")
            #print(product_query, "\n", top_product)

            # Insert the product classification into the item
            item['productClassification'] = top_product

    # Return modified receipts
    return json_receipts

# def classify(json_receipts):
#     with open('output.txt', 'a') as file:

#         #loops thru receipt objects 
#         for i, receipt in enumerate(json_receipts):
#             merchant_name = receipt['merchant']
#             dining_option = receipt['diningOptions']
#             vendor_query = [f"{merchant_name} {dining_option}"]

#             #loops thru items in receipt
#             for item in receipt['ITEMS']:
#                 items_unabbr = item['unabbreviatedDescription']
#                 item_description = item['description']
#                 vendor_query.append(f"{items_unabbr} {item_description}")
            
#             #processes query string, then classifies vendor, writes to file
#             query_string = " ".join(vendor_query)
#             top_vendor = search.query_classification(query_string, 5, "vendor")
#             print(query_string)
#             print(top_vendor)
#             file.write(f"- {i} Vendor Prediction {top_vendor}\nQuery: {query_string}\n")

#             #process query string, then classifies product, write to file
#             for j, item in enumerate(receipt['ITEMS']):
#                 product_query = f"{item['unabbreviatedDescription']} {item['description']} {merchant_name}"
#                 top_product = search.query_classification(product_query, 10, "product")
#                 print(product_query)
#                 print(top_product)
#                 file.write(f" {j} Item: {product_query} category: {top_product}\n")


processed_receipts = read_json_receipts('receipts_json.json')
classified_receipts = classify(processed_receipts)

with open('classified_receipts.json', 'w') as f:
    json.dump(classified_receipts, f, indent=4)