# vendor_query  = "mcDonalds hamburger meal take-out fries"
# top_vendor = search.query_classification(vendor_query, 5, "vendor")

"""
Get JSON and search for items (iterate through all items) -- Simlilar to Assignmnet 1
"""
# Items in JSON 
# product_query = "organic apples"
# top_product = search.query_classification(product_query, 10, "product")

# print(top_product,top_vendor,sep="\n")

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

