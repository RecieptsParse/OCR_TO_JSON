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
        "frozen foods.",
        "packaged foods.",
        "bottle deposit.",
        "HI container fee",
        "Safeway",
        "baking Cooking ingredients.",
        "various household items.",
        "pet supplies.",
        "cleaning laundry essentials.",
        "personal care products.",
        "market mart."
    ],
    "Restaurants and Food Services": [
        "places to eat.",
        "plate lunch",
        "no side.",
        "McDonald's.",
        "Coffee shop.",
        "tip.",
        "Chinese takeout",
        "fast food.",
        "dining establishment.",
        "take-out.",
        "for-here.", 
        "delivery."
    ],
    "Clothing and Apparel": [
        "Stores selling a variety of clothing.",
        "footwear.",
        "ROSS.",
        "Old Navy",
        "T&C Surf",
        "designer brands.",
        "children's clothing.",
        "accessories and jewelry.",
        "second-hand and thrift stores.",
        "custom tailoring and alterations.",
        "fashion.",
        "clothing styles."
    ],
    "Health and Beauty": [
        "pharmacies.",
        "Longs Drugs.",
        "Cosmetics and makeup.",
        "Medical devices and aids.",
        "Natural and organic beauty products.",
        "Perfumes and fragrances.",
        "CVS store.",
        "beauty supply stores.",
        "Sephora.",
        "health products.",
        "personal care products."
    ],
    "Electronics and Appliances": [
        "consumer electronics.",
        "Best Buy.",
        "Apple Store",
        "AT&T Phone Service Provider",
        "Cameras and photography gear.",
        "Audio equipment.",
        "Mobile phones and tablets.",
        "Computers and peripherals.",
        "TVs and home theater systems.",
        "Gaming consoles and accessories.",
        "household appliances.",
        "accessories for electronics and appliances."
    ],
    "Home and Garden": [
        "home improvement.",
        "gardening supplies.",
        "furniture.",
        "home decor.",
        "DIY and hardware tools.",
        "Building materials.",
        "Home Depot.",
        "Lowe's Store",
        "City Mill",
        "Outdoor furniture.",
        "Plants and flowers."

    ],
    "Entertainment and Leisure": [
        "movie theaters.",
        "Barnes & Noble",
        "Consolidated Theatres",
        "Regal Cinemas",
        "Card Shop",
        "Amusement Parks",
        "Zoo or Aquarium or Musuem",
        "Craft art supply stores.",
        "bookstores.",
        "Concert Hall Ballet Performance Theatre",
        "hobby shops.",
        "various entertainment goods and services."
    ]
}


'''
Product categories for making product database in product_database.py
'''

product_categories = {
    "Food Products": [
        "Fresh Apple slices Bananas Carrot Watermelon Lettuce Tomato Cucumber Foodland", 
        "Poultry chicken lamb beef shrimp bacon hamburger spam fish salmon ahi poke steak ribs",
        "Grain cereal rice wheat millet potato granola oatmeal bread crackers",
        "ORG – Organic VG – Vegetable PK – Pack GF - gluten free SF - sugar freeWhole Foods", 
        "GRK YGRT SNCK CKN BRST RSTD PNUT BTTR SR CRM",
        "ice cream twix jolly rancher milky way gummy bears KitKat lillipop sour gummy peg bag chocolate See's Candy",
        "Packaged Frozen Canned Foods Campbell's Soup Lunchables Microwaveable Instant Ramen Safeway",
        "Samyang Hot Ramen Turtle Chips Kimchi Miso Matcha Pocky Soy Sauce H-mart Don Quijote"
    ],
    "Beverages": [
        "Mineral Water Lemonade Boba Tea Coffee Milk Shake Juice Box POG Starbucks",
        "SPR SPRKL WTR BTL Icd AMER ORG JCE GRN T ALM MLK",
        "Diet Soda Coca Cola Pepsi Dr Pepper Mountain Dew Sprite Fanta",
        "Alcoholic Beverages Rum Wine Beer Cocktails Liquor Vodka Whiskey Gin Sangria",
        "Energy Sports Drinks Red Bull Monster Rockstar 5-hour Energy Powerade Gatorade XTEND"
    ],
    "Health And Beauty": [
        "Cosmetics Velvet Matte Lipstick Eyeshadow Palette Volumizing Mascara Makeup Remover Sephora",
        "Facecare products Revitalizing Vitamin C Serum Mineral Sunscreen SPF 50 Bamboo Charcoal Detoxifying Face Mask",
        "Skincare Products Anti-Aging Moisturizing Cream Essential Oil Hydrating Aloe Vera Body Lotion",
        "Haircare Products Curl Defining Mousse Heat Protectant Spray Volume-Boosting Dry Shampoo Scalp Scrub Conditioner",
        "Fragrance Cologne Spray Lotus Blossom Scented Perfume Rose Body Mist",
        "Oral Care Colgate CREST 3D WHT LISTERIN Mouthwash ORAL-B TOOTHBRUSH Whitening Toothpaste Floss Waterpik",
        "Nail Care Clippers Cuticle Oil Polish Remover Manicure Spa"
    ],
    "Clothing And Accessories": [
        "Top Turtleneck ribbed knit long sleeve sweater Graphic print oversized tee V-neck striped cropped top ROSS",
        "Bottoms High-Waisted Skinny Jeans Cargo Pants Pleated Midi Skirt Denim Capris Leggings Old Navy",
        "Dresses Floral Maxi Dress Sundress Strapless Slip Evening Gown Macys",
        "Activewear Compression Joggers TechMesh Breathable Workout DriFit TankTop Sneaker cleats FootLocker",
        "Headwear Knit Beanie Hat Baseball Cap Sun Visor Fedora Snapback",
        "Accessories Eyewear Sunglasses Jewelry Rings Necklace Scarves Gloves Belts Watches Tie Leather Bag Claire's"
    ],
    "Electronics": [
        "Mobile Devices SAMSUNG GALAXY S20 ULTRA 128GB COSMIC GRAY IPHONE 13 PRO NOKIA BLACKBERRY KEY3 64GB Bestbuy",
        "Consumer Electronics LG 55-INCH 4K OLED SMART TV SONY WIRELESS HEADPHONES GAMING MONITOR PORTABLE BLUETOOTH SPEAKER"
        "Gaming Consoles NINTENDO SWITCH 3DS XL SONY PLAYSTATION 3 XBOX 360 SEGA GENESIS Gamecube controllers Gamestop",
        "Apple IPHONE AIRPODS PRO CHARGING CASE IPAD PRO MACBOOK AIR USB-C LIGHTNING CABLE",
        "Computers HP Pavilion Laptop Graphics Card Keyboard Mousepad C4000 Router Microsoft Surface Wifi",
        "Appliances Coffee Maker Refrigerator Blu-ray Player Air Conditioner Microwave"
    ],
    "Home": [
        "Furniture coffee table wooden chair vanity dresser nightstand sofa bookshelf plastic storage bins",
        "Home Decor clock ceramic vase picture frame mirror curtains art wallpaper indoor succulent plants",
        "Queen-sized memory foam mattress comforter Bedding throw blanket body pillow cover area rug",
        "Dining Ware Kitchenware Stainless Steel kitchen knife porcelain dinner plate china set fork chopsticks ZIPLOC",
        "Home appliances blender stove microwave lamp refrigerator air fryer toaster air conditioner TV Cable Wifi",
        "Home Office printer paper stapler printer paper desk monitor stand folders Office Depot",
    ],
    "Outdoor Goods": [
        "Gardening Tools Watering Can Garden Gloves hose nozzle rake wheelbarrow shovel pruning shears",
        "Plants potting soil flower pots compost bin hanging fern fertilizer seedlings mulch",
        "Outdoor Furniture patio lounge chair picnic table fire pit swing hammock bench garden shed",
        "Outdoor Decor wind chime garden gnome birdhouse bird feeder fairy LED lights",
        "Outdoor appliances BBQ Grill lawn mower lantern mosquito zapper sprinklers",
    ],
    "Automotive": [
        "Car Parts Windsheild Wipers Break Pads engine oil fuel injector Car Wax Oil Gas",
        "car care kit tire pressure gauge Tire Sealant Transmission Fluid brake fluid tire chains",
        "car fuel system cleaner dashboard cleaner exhaust pipe polish seat covers Air Filter car freshener",
        "car battery jumper cables spark plugs headlight bulbs"
    ],
    "Toys And Games": [
        "Children's Toys my little pony Barbie doll LEGO CITY TRANSFORMERS ACTION FIG NERF N-STRIKE ELITE BLASTER",
        "Board Games MONOPOLY Scrabble Battleship naval combat Catan Risk Clue",
        "stuffed animal cuddly plush toy Teddy Bear Pillow Pet Squishmallow Webkinz TY Beanie",
        "Card Games Pokemon trading Yugi-oh deck Uno magic exploding kittens cards against humanity",
        "Creative Jigsaw Puzzle Building Blocks Rubik's cube strategy chess set Jenga Dominos",
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
        "Treats",
        "Pet Toys",
        "Pet Grooming Products",
        "DOG COLLAR NYLON LRG",
        "FISH TANK",
        "CHEW STICKS",
        "DOG FOOD",
        "HAMSTER CAGE",
        "CAT LITTER",
        "REPTILE HEAT LAMP",
        "Pet Accessories",
        "Pet Enclosures"
    ],
    "Baby Products": [
        "Baby Wipes",
        "HUGGIES",
        "BBY BLANKET",
        "INF CAR SEAT",
        "NURSERY CRIB",
        "STROLLER",
        "BABY FORMULA",
        "Baby Toys",
        "Diapers",
        "Baby Care Items"
    ],
    "Cleaning Supplies": [
        "Cleaning Products",
        "LYSOL",
        "WINDEX",
        "WONDER MOP",
        "DUSTPAN",
        "CLOROX  BLCH",
        "GAIN 2X",
        "TIDE LQ PODS",
        "OXICLEAN Stain Remover",
        "GLAD Trash Bags",
        "MR. CLEAN Magic Eraser",
        "SWIFFER",
        "Surface Cleaners",
        "Disinfectants",
        "Floor Cleaners",
        "Laundry Detergents",
        "Dishwashing Supplies",
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
        "Season Pass",
        "Amusement Park Tickets",
        "Event Tickets"
    ]
}
