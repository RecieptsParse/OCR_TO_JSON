import vendor_database
import product_database
import search

'''
saves faiss index and mapping to directory 
model for embeddings & descriptions can be updated in config.py
'''
vendor_database.make_vendor_database()
product_database.make_product_database()

# Example usage for vendors
vendor_query = "mcDonalds hamburger meal take-out fries"
top_vendor = search.query_classification(vendor_query, 5, search.vendor_classifier)

# Example usage for products
product_query = "organic apples"
top_product = search.query_classification(product_query, 10, search.product_classifier)
