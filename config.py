# Global variables 

'''
 Transformer model for classification 
 Modules use SentenceTransformer to process the string variable
 Used in vendor_database.py, product_database.py, and search.py

 Dimensions is used in making the faiss database
 The dimensions value should match that of the model used
'''

transformer_model = "BAAI/bge-large-en-v1.5"
dimensions = 1024


'''
Vendor categories for making vendor database in vendor_database.py
'''

vendor_categories  = {
    "Grocery and Supermarkets": [
        "food products.",
        "various household items.",
        "personal care products."
    ],
    "Restaurants and Food Services": [
        "places to eat.",
        "fast food.",
        "dining establishment.",
        "take-out, for-here, delivery."
    ],
    "Clothing and Apparel": [
        "Stores selling a variety of clothing.",
        "footwear.",
        "fashion.",
        "clothing styles."
    ],
    "Health and Beauty": [
        "pharmacies.",
        "beauty supply stores.",
        "health products.",
        "personal care products."
    ],
    "Electronics and Appliances": [
        "consumer electronics.",
        "household appliances.",
        "accessories for electronics and appliances."
    ],
    "Home and Garden": [
        "home improvement.",
        "gardening supplies.",
        "furniture.",
        "home decor."
    ],
    "Entertainment and Leisure": [
        "movie theaters.",
        "bookstores.",
        "hobby shops.",
        "various entertainment goods and services."
    ]
}


'''
Product categories for making product database in product_database.py
'''

product_categories = {
    "Food Products": [
        "Fruits",
        "Vegetables",
        "Meats",
        "Dairy Products",
        "Candy",
        "Bakery Products",
        "Grains",
        "Cereals",
        "Snacks",
        "Condiments",
        "Canned Goods",
        "Frozen Foods",
        "Packaged Foods"
    ],
    "Beverages": [
        "Water",
        "Soda",
        "Juice",
        "Alcoholic Beverages",
        "Tea",
        "Coffee",
        "Milk",
        "Energy Drinks",
        "Sports Drinks"
    ],
    "Health And Beauty": [
        "Cosmetics",
        "Skincare Products",
        "Haircare Products",
        "Fragrance",
        "Oral Care",
        "Nail Care",
        "Personal Hygiene"
    ],
    "Clothing And Accessories": [
        "Tops",
        "Bottoms",
        "Dresses",
        "Activewear",
        "Outerwear",
        "Sleepwear",
        "Swimwear",
        "Footwear",
        "Headwear",
        "Eyewear",
        "Jewelry",
        "Scarves",
        "Gloves",
        "Belts",
        "Watches"
    ],
    "Electronics": [
        "Mobile Devices",
        "Computers",
        "Consumer Electronics",
        "Appliances",
        "Gaming Consoles"
    ],
    "Home": [
        "Furniture",
        "Home Decor",
        "Bedding",
        "Kitchenware",
        "Dining Ware",
        "Home Office",
        "Storage"
    ],
    "Outdoor Goods": [
        "Gardening Tools",
        "Plants",
        "Outdoor Furniture",
        "Outdoor Decor",
        "Outdoor Lighting",
        "Outdoor Cooking",
        "Outdoor Storage"
    ],
    "Automotive": [
        "Car Accessories",
        "Car Parts",
        "Oil",
        "Gas"
    ],
    "Toys And Games": [
        "Children's Toys",
        "Plush Toys",
        "Board Games",
        "Card Games",
        "Video Games"
    ],
    "Sporting Goods": [
        "Sports Equipment",
        "Fitness Gear"
    ],
    "Books And Stationery": [
        "Books",
        "Magazines",
        "Stationery Items",
        "Art Supplies"
    ],
    "Pharmacy And Health Products": [
        "Medications",
        "Supplements",
        "First Aid Supplies",
        "Medical Equipment",
        "Vitamins"
    ],
    "Pet Supplies": [
        "Pet Food",
        "Pet Toys",
        "Pet Grooming Products",
        "Pet Accessories",
        "Pet Enclosures"
    ],
    "Baby Products": [
        "Baby Food",
        "Baby Toys",
        "Diapers",
        "Baby Care Items"
    ],
    "Cleaning Supplies": [
        "Cleaning Products",
        "Surface Cleaners",
        "Disinfectants",
        "Floor Cleaners",
        "Laundry Detergents",
        "Dishwashing Supplies",
        "Trash Bags",
        "Cleaning Tools"
    ],
    "Gifts And Miscellaneous": [
        "Gifts",
        "Wrapping Paper",
        "Gift Bags",
        "Greeting Cards",
        "Seasonal Items",
        "Souvenirs"
    ],
    "Event Tickets": [
        "Movie Tickets",
        "Aquarium Tickets",
        "Amusement Park Tickets",
        "Event Tickets"
    ]
}
