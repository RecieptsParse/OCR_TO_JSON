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
        "apple", 
        "cucumber"
        "beef", 
        "chicken", 
        "pork", 
        "lamb", 
        "fish", 
        "turkey", 
        "shrimp", 
        "cheese",
        "yogurt",
        "GRK",
        "YGRT",
        "ice cream",
        "twix", 
        "kit kat",
        "jolly rancher", 
        "milky way", 
        "gummy bears", 
        "lollipop",
        "sour gummy",
        "soup",
        "SNCK",
        "CKN BRST",
        "orange CKN",
        "GF",
        "SF",
        "peg bag",
        "RSTD Peanuts",
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
        "Lemonade",
        "SPR WTR",
        "WTR",
        "Pepsi",
        "Grn Tea",
        "Icd Amer",
        "Org Jce",
        "Sprkl Wtr",
        "Alm Milk",
        "Diet Col",
        "Hot Choc"
        "Juice",
        "Alcoholic Beverages",
        "Tea",
        "Coffee",
        "Milk",
        "MLK",
        "Whole MLK",
        "Energy Drinks",
        "Sports Drinks"
    ],
    "Health And Beauty": [
        "Cosmetics",
        "Revitalizing Vitamin C Serum",
        "Mineral Sunscreen SPF 50",
        "Bamboo Charcoal Detoxifying Face Mask",
        "Organic Lavender Essential Oil",
        "Anti-Aging Moisturizing Cream",
        "Skincare Products",
        "Haircare Products",
        "Fragrance",
        "Oral Care",
        "Nail Care",
        "Personal Hygiene"
    ],
    "Clothing And Accessories": [
        "Tops",
        "Women's Striped V-Neck Sweater",
        "Knit Beanie Hat",
        "Graphic T-Shirt",
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
        "SAMSUNG GALAXY S20 ULTRA 128GB COSMIC GRAY",
        "LG 55-INCH 4K OLED SMART TV",
        "SONY WIRELESS NOISE-CANCELING HEADPHONES"
        "NINTENDO SWITCH",
        "PORTABLE BLUETOOTH SPEAKER",
        "APPLE WATCH",
        "Computers",
        "Consumer Electronics",
        "Appliances",
        "Gaming Consoles"
    ],
    "Home": [
        "Furniture",
        "Coffee Table",
        "Home Decor",
        "Queen-sized Bedding",
        "Throw Blanket",
        "Pillow Covers",
        "Wall Clock",
        "Stainless Steel Kitchen Knife",
        "Kitchenware",
        "Dining Ware",
        "Home Office",
        "Storage",
        "Wall Shelves",
        "Bins",
        "Area Rug"
    ],
    "Outdoor Goods": [
        "Gardening Tools",
        "Watering Can",
        "Garden Gloves",
        "Plants",
        "Outdoor Furniture",
        "BBQ Grill",
        "Outdoor Decor",
        "Outdoor Lighting",
        "Outdoor Cooking",
        "Outdoor Storage"
    ],
    "Automotive": [
        "Car Accessories",
        "Windsheild Wipers",
        "Break Pads",
        "Transmission Fluid",
        "Air Filter",
        "Tire Sealant",
        "Car Wax",
        "Car Parts",
        "Oil",
        "Gas"
    ],
    "Toys And Games": [
        "Children's Toys",
        "LEGO CITY",
        "PIKACHU PLUSH TOY",
        "MY LITTLE PONY PLAYSET",
        "TRANSFORMERS ACTION FIG",
        "NERF N-STRIKE ELITE BLASTER",
        "MONOPOLY CLASSIC BOARD GAME",
        "Plush Toys",
        "Board Games",
        "Card Games",
        "Video Games"
    ],
    "Sporting Goods": [
        "Sports Equipment",
        "Baseball Bat",
        "Soccer Ball",
        "Fitness Gear"
    ],
    "Books And Stationery": [
        "Books",
        "Sketchbook Top Spiral",
        "Magazines",
        "Hardcover Journal",
        "Stationery Items",
        "Mechanical Pencils",
        "Paint",
        "Sticky Notes",
        "Art Supplies"
    ],
    "Pharmacy And Health Products": [
        "Medications",
        "Supplements",
        "First Aid Supplies",
        "Medical Equipment",
        "Blood Pressure Monitor",
        "Chewable Tablets",
        "Digital Thermometer",
        "Band-Aids",
        "Pain Relief Tablets",
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
        "HLMRK",
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
