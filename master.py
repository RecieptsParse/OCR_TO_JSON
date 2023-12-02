import vendor_database
import product_database
import search
import convert

'''
FIX DOCUMENTATION LATER: JSON OBJECT CONVERSION PHASE
This code has not been tested yet.
'''
receipts_folder = "receipts/text" # the receipt folder should have two subfolders of images and text

openai_api_key="INSERT_OPENAI_API_KEY_HERE"

receiptParser = convert.make_receiptParser()
fewshot_prompt = convert.make_fewshot_prompt(receiptParser)
model = convert.make_model(model="gpt-3.5-turbo-16k", temperature=1.00, openai_api_key=openai_api_key)
chain = convert.make_chain(fewshot_prompt, model, recieptParser)

# Iterate through each receipt txt file
# This also has not been tested yet
for filename in os.listdir(receipts_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(receipts_folder, filename)) as f:
            print(f.readline()) # currently only read the first line of each receipt text file
            # response = chain.invoke(f.read())

'''
saves faiss index and mapping to directory 
model for embeddings & descriptions can be updated in config.py
'''
vendor_database.make_vendor_database()
product_database.make_product_database()

# Example usage for vendors
vendor_query = "mcDonalds hamburger meal take-out fries"
top_vendor = search.query_classification(vendor_query, 5, "vendor")

# Example usage for products
product_query = "organic apples"
top_product = search.query_classification(product_query, 10, "product")

print(top_product,top_vendor,sep="\n")
