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
        "Toys Board Games",
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
        "Skincare Products Anti-Aging Moisturizing Cream Essential Oil Hydrating Aloe Vera Body Lotion Dial Dove",
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
        "Home Office printer paper stapler printer paper desk monitor stand folders Office Depot"
    ],
    "Outdoor Goods": [
        "Gardening Tools Watering Can Garden Gloves hose nozzle rake wheelbarrow shovel pruning shears",
        "Plants potting soil flower pots compost bin hanging fern fertilizer seedlings mulch",
        "Outdoor Furniture patio lounge chair picnic table fire pit swing hammock bench garden shed",
        "Outdoor Decor wind chime garden gnome birdhouse bird feeder fairy LED lights",
        "Outdoor appliances BBQ Grill lawn mower lantern mosquito zapper sprinklers"
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
        "Creative Jigsaw Puzzle Building Blocks Rubik's cube strategy chess set Jenga Dominos"
    ],
    "Sporting Goods": [
        "Sports Equipment Tennis Racket Baseball Bat Golf Club Kayak Paddle Rollerblades Archery Bow",
        "Nike Dri-FIT Running Shoes Under Armour Compression Leggings Speedo Swim Goggles Knee Pads Boxing Gloves",
        "Fitness Gear Climbing Harness Resistance Band Cardio Jump Rope Cycling Helmet Yoga Mat Dumbbell",
        "Weight Bench Medicine Ball Training Cone Set Basket Ball Hoop Volleyball Net Indoor Table Tennis Table"
    ],
    "Books And Stationery": [
        "Books Magazines Hardcover Journal Poetry Classic Novels Literature Fantasy Sci-fi Romance Mystery Memoir Barnes & Noble",
        "Stationery Items Mechanical Pencils Sticky Notes Pencil Case Fountain Pen Flashcards Origami Kit Markers Weekly Planner",
        "Paint Art Supplies Coloring Book Watercolor Sketchbook Top Spiral Oil Pastels Canvas Pad"
    ],
    "Pharmacy And Health Products": [
        "Medications Supplements Chewable Tablets Pain Relief Tablets Vitamins Omega-3 Fish Oil Capsules Probiotic",
        "First Aid Supplies Band-Aids Antiseptic Wipes Sterile Gauze Pads Cold Packs Compress Hand Sanitizer",
        "DayQuil Severe Cold & Flu Relief Robitussin Maximum Strength Cough and Chest Congestion Kleenex Halls Cough Drops",
        "Medical Equipment Blood Pressure Monitor Digital Thermometer Crutches Folding Walker Medical Scale"
    ],
    "Pet Supplies": [
        "Pet Food Treats Dry dog canned food CHEW STICKS Puppy Formula",
        "Pet Toys Squeaky Plush Chew Toy Rubber Ball Fetch Frisbee Teething Ring",
        "Pet Grooming Products Flea and Tick Shampoo Deodorizing Pet Wipes Brush Clippers",
        "Pet Enclosures FISH TANK HAMSTER CAGE CAT LITTER REPTILE HEAT LAMP Scratching Posts Perches Pet Bed Bowl",
        "Pet Accessories DOG COLLAR Leash Pet ID Tag"
    ],
    "Baby Products": [
        "Baby Care Items Monitor Baby Wipes HUGGIES Pampers BABY FORMULA Diaper Rash Cream Bottles Sippy Cup",
        "INF CAR SEAT infant STROLLER Carrier baby High Chair Changing Pad Booster Seat NURSERY CRIB",
        "Baby Toys Plush Rattle Teething Rings BBY Swaddle BLANKET Play Mat Rolly Cars Pacifier"
    ],
    "Cleaning Supplies": [
        "Cleaning Products LYSOL Wipes WINDEX Spray CLOROX BLCH GAIN 2X TIDE LQ PODS Disinfectants",
        "GLAD Trash Bags MR. CLEAN Magic Eraser SWIFFER Surface Cleaners OXICLEAN Stain Remover Floor Cleaners",
        "Laundry Detergents Dishwashing Supplies DAWN sponge Hand soap dispenser wash sanitizer",
        "Cleaning Tools cloth paper towels broom WONDER MOP dustpan Odor Eliminator air freshener glade"
    ],
    "Gifts And Miscellaneous": [
        "Gifts Wrapping Paper Gift Bags cardboard Boxes ribbons tape",
        "Greeting Cards Envelopes HLMRK Hallmark Seasonal Items Christmas Ornaments Scented Candles",
        "Souvenirs keychain snowglobe magnet postcard stamps"
    ],
    "Event Tickets": [
        "Movie Tickets Cinema Theatre Regal Consolidated Film Festival General Admission",
        "Honolulu Aquarium Tickets Zoo Museum Art Exhibition Planetarium Sports game",
        "Amusement Park Tickets Wet n Wild Season Pass Carnival Cirus Comedy Night",
        "Event Tickets Blaisdell Symphony Concert Hall Ballet Dance Performance Opera Live music Band"
    ]
}
