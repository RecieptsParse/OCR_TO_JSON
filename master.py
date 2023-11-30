import vendor_database
import product_database
import search

receipt_folder = "" #relative folder path that contains receipt text files

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
