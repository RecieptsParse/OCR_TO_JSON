import search
import json
import sys

# Check if the required number of arguments is provided
if len(sys.argv) < 3:
    print("Insufficient arguments. Please provide both input and output paths.")
    sys.exit(1)

input_path = sys.argv[1]  # The path to the parsed receipts in json format, must be .json file
output_path = sys.argv[2]  # The path to the output file

# Reads in JSON objects from file, saves to an array of JSON objects
def read_json_receipts(file_path):
    with open(file_path, 'r') as f:
         lines = f.readlines()
    json_objects = []
    for line in lines:
         json_object = json.loads(line)
         json_objects.append(json_object)
    return json_objects

# Takes in array of JSON objects, processes each one
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

        # Insert the vendor classification into the receipt
        receipt['ReceiptInfo']['vendorClassification'] = top_vendor

        # Loops through items in receipt
        for item in receipt['ReceiptInfo']['ITEMS']:
            product_query = f"{item['unabbreviatedDescription']} {item['description']} {merchant_name}"
            top_product = search.query_classification(product_query, 10, "product")

            # Insert the product classification into the item
            item['productClassification'] = top_product

    # Return modified receipts
    return json_receipts

# Runs above functions
processed_receipts = read_json_receipts(input_path)
classified_receipts = classify(processed_receipts)

# saves new JSON file with classifications 
with open(output_path, 'w') as f:
    json.dump(classified_receipts, f, indent=4)