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

vendor_categories = {
    "Grocery and Supermarkets": [
        "fresh produce and vegetables",
        "dairy and eggs",
        "meat and seafood",
        "canned goods",
        "bakery items",
        "beverages and drinks",
        "snacks and confectionery",
        "health and wellness food",
        "international cuisine ingredients",
        "organic and natural foods",
        "baby food and supplies",
        "bulk food items",
        "spices and seasonings",
        "specialty food items",
        "vegan and vegetarian options",
        "gluten-free products",
        "local and artisanal food items",
        "ethnic food markets",
        "bottle deposit",
        "HI container fee",
        "market mart"
    ],
    "Restaurants and Food Services": [
        "fine dining restaurants",
        "casual dining spots",
        "fast casual eateries",
        "ethnic cuisines",
        "vegan and vegetarian restaurants",
        "seafood restaurants",
        "steakhouses",
        "pizzerias",
        "burger joints",
        "cafes and bistros",
        "ice cream and dessert parlors",
        "food trucks and street food",
        "buffet and all-you-can-eat",
        "brunch and breakfast spots",
        "barbecue and grill",
        "gastropubs and bars",
        "food courts",
        "catering services"
        "plate lunch",
        "dining establishment",
        "take-out",
        "for-here", 
        "delivery",
        "tip"
    ],
    "Clothing and Apparel": [
        "menswear and women's wear",
        "sportswear and activewear",
        "formal and evening wear",
        "casual and streetwear",
        "baby and kids' apparel",
        "maternity wear",
        "lingerie and undergarments",
        "shoe stores",
        "boutiques and specialty clothing",
        "eco-friendly and sustainable fashion",
        "plus-size clothing",
        "vintage and retro clothing",
        "fashion accessories",
        "department stores",
        "online clothing retailers",
        "bespoke and custom clothing",
        "uniforms and workwear",
        "swimwear and beachwear"
    ],
    "Health and Beauty": [
        "hair care and styling products",
        "skin care and treatments",
        "nail care and salons",
        "spa and wellness centers",
        "optical and eyewear stores",
        "dietary supplements",
        "organic and natural health products",
        "men's grooming products",
        "health and fitness stores",
        "dental care products",
        "therapeutic and massage services",
        "dermatology and skin clinics",
        "holistic and alternative medicine",
        "vitamins and minerals",
        "personal hygiene products",
        "beauty and makeup tutorials",
        "health and wellness apps",
        "yoga and meditation centers",
        "pharmacies",
        "Longs Drugs",
        "CVS store"
    ],
    "Electronics and Appliances": [
        "home automation and smart devices",
        "office and school electronics",
        "electronic repair services",
        "drone and aerial photography equipment",
        "virtual reality and augmented reality devices",
        "wearable technology",
        "kitchen and cooking appliances",
        "personal care and grooming electronics",
        "lighting and electrical supplies",
        "home security systems",
        "weather and outdoor devices",
        "portable and wireless devices",
        "refurbished and second-hand electronics",
        "electronics rental services",
        "online electronics retailers",
        "electronic parts and components",
        "car electronics and accessories",
        "robotics and automation equipment",
        "consumer electronics",
        "Best Buy",
        "Apple Store",
        "AT&T Phone Service Provider"
    ],
    "Home and Garden": [
        "interior design services",
        "lawn and garden care",
        "patio and outdoor decor",
        "kitchenware and utensils",
        "bathroom fixtures and accessories",
        "bedding and linens",
        "window treatments and draperies",
        "storage and organization solutions",
        "home safety and security",
        "flooring and carpets",
        "paint and wall coverings",
        "lighting and fixtures",
        "plumbing and fixtures",
        "home automation products",
        "eco-friendly and sustainable home products",
        "seasonal and holiday decorations",
        "pest control products",
        "home repair and maintenance services",
        "City Mill",
        "Home Depot",
        "Lowe's Store"
    ],
    "Entertainment and Leisure": [
        "live music venues",
        "theater and performing arts",
        "museums and galleries",
        "sports events and venues",
        "clubs and nightlife",
        "libraries and reading rooms",
        "parks and recreational areas",
        "fitness and gym facilities",
        "yoga and pilates studios",
        "dance studios and classes",
        "arcades and game centers",
        "escape rooms and interactive experiences",
        "water parks and theme parks",
        "outdoor and adventure activities",
        "cultural and historical tours",
        "craft and hobby classes",
        "leisure and hobby stores",
        "sports equipment and apparel"
    ]
}


'''
Product categories for making product database in product_database.py
'''

product_categories = {
    "Food Products": [
        "Fresh Apple slices Bananas Carrot Watermelon cantalope grapes Cucumber Peas Corn Green Beans Mixed Vegetables Foodland", 
        "Poultry chicken Breast lamb beef shrimp bacon hamburger spam fish salmon ahi poke roll steak ribs oyster",
        "Grain cereal rice wheat millet potato granola bars oatmeal sweet bread loaf crackers eggs",
        "salt vinegar mayonase mayo ketchup pepper mustard pickels lettuce tomato Soy Sauce Teriyaki Sauce Hot Sauce Barbecue Sauce Honey",
        "ORG – Organic VG – Vegetable PK – Pack GF - gluten free SF - sugar free Whole Foods PC LCL", 
        "GRK YGRT SNCK CKN BRST RSTD PNUT BTTR SR CRM OR CCNUT SLD SHRT RIBS MSH POT BURG STK PBJ FRT CP",
        "ice cream Meadow Gold twix jolly rancher milky way gummy bears goldbears KitKat lillipop sour gummy peg bag chocolate See's Candy",
        "Packaged Frozen Canned Foods Campbell's Soup Lunchables Microwaveable Instant Ramen Safeway bento curry peg bag",
        "Samyang Hot Ramen Turtle Chips Kimchi Miso Matcha Pocky Soy Sauce H-mart Don Quijote Kellogs",
        "Cheese Yogurt Butter Cream Eggs Flour Sugar Yeast Baking Powder Vanilla Extract Cocoa Powder"      
    ],
    "Beverages": [
        "Mineral Water Lemonade Boba Tea Green Tea Black Tea Chamomile Tea Peppermint Tea Coffee Milk Shake Juice Box POG Starbucks",
        "SPR SPRKL WTR BTL Icd AMER ORG JCE GRN T ALM MLK SFTDK DK CHAI OJ BLK C ESP LEM deposit fee handling fee",
        "Diet Soda Coca Cola Pepsi Dr Pepper Mountain Dew Sprite Fanta Soft Drinks 7UP Root Beer Ginger Ale Cream Soda",
        "Alcoholic Beverages Rum Wine Craft Beer Cocktails Liquor Vodka Whiskey Gin Sangria Mixers Tonic Water Club Soda Ginger Beer",
        "Energy Sports Drinks Red Bull Monster Rockstar 5-hour Energy Powerade Gatorade XTEND Protein Shake Electrolyte Hydration Drinks",
        "milk tea boba smoothie slush Green Smoothie Detox Juice Fruit Juices Orange Juice Apple Juice Cranberry Juice",
        "Sparkling Water Sparkling Lemonade Iced Matcha Latte Hibiscus Tea Lassi Coconut Smoothie Ginger Lemon Detox Shot",
        "Specialty Coffees Mocha Americano Flat White Hot Beverages Hot Chocolate Cappuccino Espresso Latte"
    ],
    "Health And Beauty": [
        "Cosmetics Lipstick Eyeshadow Palette Mascara Makeup Remover Eyeliner Blush concealer foundation Sephora",
        "Facecare products Serum Mineral Sunscreen SPF 50 Face Mask face wash toner acne cream ",
        "Skincare Products Moisturizing Cream Essential Oil Hydrating Aloe Vera Body Lotion Dial Dove Hand Cream",
        "Haircare Products Curl Mousse Heat Protectant Spray Dry Shampoo Scalp Scrub Conditioner Hairspray Wax Gel",
        "Fragrance Cologne Spray Scented Perfume Body Mist deodorant Therapeutic Oils Eucalyptus Oil Lavender Oil Tea Tree Oil",
        "Oral Care Colgate CREST 3D WHT LISTERIN Mouthwash ORAL-B TOOTHBRUSH Whitening Toothpaste Dental Floss Waterpik",
        "Nail Care Clippers Cuticle Oil Polish Remover Manicure Spa Nail polish cotton balls nail polish remover acetone showercap tissue",
        "Eye Care Contact Lens Solution Eye Drops eye wash Eye Heat Compress Mask Eyelid Cleansing Wipes",
        "Baby Care Baby Shampoo Baby Lotion Baby Powder Diaper Rash Cream baby oil Baby Bubble Bath"    
    ],
    "Clothing And Accessories": [
        "Top Turtleneck ribbed knit long sleeve sweater Graphic print oversized tee V-neck striped cropped Tank tops ROSS",
        "Bottoms High-Waisted Skinny Jeans Cargo Pants Pleated Midi Skirt Denim Capris Leggings Old Navy",
        "Dresses Floral Maxi Dress Sundress Strapless Slip Evening Gown Macys robe pajamas apron Onesies Rompers",
        "coat jacket jumper Parkas Raincoats vest sweatshirt blazer Suits Tuxedos",
        "Activewear Compression Joggers TechMesh Breathable Workout DriFit TankTop Sneaker cleats FootLocker swimsuit ProCat Puna Swimwear Bikinis Swim Trunks Rash Guards",
        "Headwear Knit Beanie Hat Baseball Cap Sun Visor Fedora Snapback party hat helmet crown hair-tie scrunchy",
        "Accessories Eyewear Sunglasses Jewelry Rings Necklace pendant Scarves Gloves Belts Watches Tie Leather Bag Claire's Handbags Totes Clutches Backpacks Wallets Cufflinks Pocket Squares",
        "Footwear Sneakers Boots Sandals Heels Flats Athletic shoes Flip-flops Wedges Ankle boots Platform shoes Combat boots Ballet",
        "Undergarments Bras Underwear Boxers Briefs Boyshorts Camisoles Lingerie Push-up Bras Sports Bras Sleepwear (Nightgowns, Pajamas)",
        "Winter Accessories Scarves Gloves Hats Ear Muffs Summer Accessories Sun Hats Sunglasses Beach Towels"
    ],
    "Electronics": [
        "Mobile Devices SAMSUNG GALAXY S20 ULTRA 128GB COSMIC GRAY IPHONE 13 PRO NOKIA BLACKBERRY KEY3 64GB Bestbuy",
        "Consumer Electronics LG 55-INCH 4K OLED SMART TV SONY WIRELESS HEADPHONES GAMING MONITOR PORTABLE BLUETOOTH SPEAKER Audio Equipment Speakers Headphones Earbuds Microphones",
        "Gaming Consoles NINTENDO SWITCH 3DS XL SONY PLAYSTATION 3 XBOX 360 SEGA GENESIS Gamecube controllers Gamestop",
        "Apple IPHONE AIRPODS PRO CHARGING CASE IPAD PRO MACBOOK AIR USB-C LIGHTNING CABLE Tablets E-Readers MP3 Players",
        "Computers HP Pavilion Laptop Graphics Card Keyboard Mousepad C4000 Router Microsoft Surface Wifi Computer Accessories Keyboards Mice Webcams USB Hubs",
        "Appliances Coffee Maker Refrigerator Blu-ray Player Streaming Devices Air Conditioner Microwave Batteries lightbulb Toasters Blenders Juicers",
        "keyboard laptop screen earbuds Video Game Accessories Controllers Headsets Cables Photography Cameras Lenses Tripods Memory Cards",
        "Televisions LED LCD Plasma Smart TVs Smart Home Devices Thermostats Security Cameras Smart Plugs Smartwatches Fitness Trackers"     
    ],
    "Home": [
        "Furniture coffee table wooden chair Beds vanity dresser nightstand sofa bookshelf plastic storage bins fan Armchairs TV Stands",
        "Home Decor clock ceramic vase picture frame mirror curtains art wallpaper indoor succulent plants Lamps Chandeliers",
        "Queen-sized memory foam mattress comforter Bedding throw blanket body throw pillow cover Microfiber towel area rug table cloth",
        "Dining Ware Kitchenware Kettle Stainless Steel kitchen knife pot pan porcelain dinner plate china set fork chopsticks ZIPLOC Utensils Cutting Boards",
        "Home appliances blender stove microwave lamp refrigerator air fryer toaster air conditioner TV Cable Wifi fire-extinguisher",
        "Home Office printer paper stapler printer paper desk monitor stand folders Office Depot Shelves Cabinets Bins",
        "envelopes pillow bed sheet pillow cover curtains plates bowls Ironing board Alarm clock Hangers Tablecloth",
        "wrech screw driver flat head philip drill bit DIY Tools Hammers Locks Safes Alarm Systems",
        "Bathroom Accessories Shower Curtains Bath Mats Towels mirror Bathroom Scale Soap Dispenser Shower Caddy"
    ],
    "Outdoor Goods": [
        "Gardening Tools Watering Can Garden Gloves hose nozzle rake wheelbarrow shovel pruning shears weeder Insect Repellent",
        "Plants potting soil flower pots compost bin hanging fern fertilizer seedlings mulch concrete Watering Can",
        "Outdoor Furniture patio lounge chair picnic table Picnic Baskets Coolers Blankets fire pit swing hammock bench garden shed ",
        "Outdoor Decor wind chime garden gnome birdhouse bird feeder fairy LED lights decorations Outdoor String Lights",
        "Outdoor appliances BBQ Grill lawn mower lantern mosquito zapper sprinklers rope Hammock Outdoor Speaker Solar Lights",
        "Camping Gear Tents Sleeping Bags Backpacks Beach Chairs Umbrellas Surfboards Hiking Equipment Hiking Boots Compass Maps",
        "Outdoor Accessories Binoculars Compass Portable Power Bank Outdoor First Aid Kit GPS Device Folding Table Motion Sensor",
        "Camping Cookware Portable Stove Camping Lantern Camp Chairs Camping Table Cooler Sleeping Pad Inflatable Pillow Mosquito Net",
        "Bird Bath Sundial Rain Gauge Outdoor Clock Solar Fountain Weather Vane Planter Boxes Outdoor Mirrors Garden Flags",
        "Backyard Games Cornhole Set Lawn Darts Bocce Ball Badminton Set Croquet Set Giant Jenga Frisbee"       
    ],
    "Automotive": [
        "Car Parts Windsheild Wipers Break Pads engine oil fuel injector Car Wax Oil Gas Leaded Unleadead Exhaust Systems",
        "car care kit tire pressure gauge Tire Sealant Transmission Fluid brake fluid tire chains Car Wash Fluids Lubricants",
        "car fuel system cleaner dashboard cleaner exhaust pipe polish seat covers Air Filter car freshener Pumper Seat Covers Floor Mats",
        "car battery jumper cables spark plugs headlight bulbs Car Stereos GPS Navigation",
        "Toyota Honda Subaru Hyundai Tesla BMW Ford Nissan Volkswagen Mercedes ford Benz Chrysker Budget Avis Enterprise Hertz Alamo Sedan Van Hatchbacks Electric Cars Compact Sports convertible wagon coupe limousine hybrid",
        "scooter motorcycle van car caravan bus motor race car electric bike moped truck",
        "Valvoline Royal Purple Lucas Oil Pennzoil Gasoline Beretania Texaco Shell Aloha Petroleum Shell Costco Gasoline",
        "Motorcycle Parts Helmets Jackets Gloves Tires and Wheels Tires Rims Hubcaps Jacks Wrenches Diagnostic Tools"
    ],
    "Toys And Games": [
        "Children's Toys my little pony Barbie doll LEGO CITY TRANSFORMERS ACTION FIG NERF N-STRIKE ELITE BLASTER dinosaur clown",
        "Board Games MONOPOLY Scrabble Battleship naval combat Catan Risk Clue Checkers Chess",
        "stuffed animal cuddly plush toy Teddy Bear Pillow Pet Squishmallow Webkinz TY Beanie Bears Rabbits Elephants",
        "Card Games Pokemon trading Yugi-oh deck Uno magic exploding kittens cards against humanity",
        "Costume wand sword knight princess magic broomstick unicorns goblins werewolves troll staff action figures Role Play Costumes Play",
        "lightsaber spaceship alien figure starwars plushies Star Wars beyblade Lego Action Figures Superheroes Dinosaurs Robots",
        "Creative Jigsaw Puzzle Building Blocks Rubik's cube strategy chess set Jenga Dominos plane model Educational Toys Puzzles Learning Tablets",
        "Outdoor Play Swing Sets Slides Trampolines Water Guns pool floats water slides  ",
        "Electronic Toys RC Cars Drones Video Games Science Kits Chemistry Sets Microscopes",

#         "Role Play Costumes Play Kitchens Dollhouses",
#         "Water Toys Pool Floats Water Guns Sprinklers",

        "Sports Toys Basketballs Footballs Soccer Balls"
    ],
    "Sporting Goods": [
        "Sports Equipment Tennis Racket Baseball Bat Golf Club Kayak Paddle Rollerblades Archery Bow boat bike",
        "Nike Dri-FIT Running Shoes Under Armour Compression Leggings Speedo Swim Goggles Knee Pads Boxing Gloves",
        "Fitness Gear Climbing Harness Resistance Band Cardio Jump Rope Cycling Helmet Yoga Mat Dumbbell",
        "Weight Bench Medicine Ball Training Cone Set Basket Ball Hoop Volleyball Net Indoor Table Tennis Table",
        
#         "Outdoor Recreation Tents Sleeping Bags Hiking Gear",
#         "Team Sports Equipment Balls Bats Gloves",
#         "Water Sports Gear Surfboards Wetsuits Paddleboards",
#         "Winter Sports Ski Snowboard Ice Skates",
#         "Fitness Accessories Yoga Mats Resistance Bands",
#         "Cycling Bicycles Helmets Locks Accessories",
#         "Golf Equipment Golf Clubs Balls Gloves",
#         "Running Gear Running Shoes Apparel Trackers",
#         "Combat Sports Boxing Gloves Punching Bags",
#         "Racket Sports Tennis Badminton Squash",
#         "Sportswear Jerseys Shorts Socks Caps",
#         "Fishing Gear Rods Reels Lures Tackle",
        "Hunting Equipment Rifles Ammo Camouflage"
    ],
    "Books And Stationery": [
        "Books Magazines Hardcover Journal Poetry Classic Novels Literature Fantasy Sci-fi Romance Mystery Memoir Barnes & Noble Comic Books",
        "Stationery Items Mechanical Pencils Sticky Notes Pencil Case Fountain Pen Flashcards Origami Kit Markers Weekly Planner",
        "Paint Art Supplies Coloring Book Watercolor Sketchbook Top Spiral Oil Pastels Canvas Pad",
        "Packet envelope letter tape",
        "Fiction Non-Fiction Biography Autobiographies Science Philosophy Cookbooks Graphic Novels Adventures",
        "Highlighters Ballpoint Pens Calligraphy Charcoal Pencils Art Paper Clips Sticky Tabs Glitter Colored Pencils Stencils",
        
#         "Educational Books Textbooks Encyclopedias Dictionaries",
#         "Stationery Items Notebooks Pens Pencils Erasers",
#         "Art Supplies Paints Brushes Canvases Easels",
#         "Office Supplies Staplers Tape Dispensers",
#         "Travel Books Guides Maps Phrasebooks",
#         "Children's Books Picture Books Storybooks",
#         "Cookbooks Recipes Techniques Tips",
#         "Self-Help Books Motivational Inspirational",
#         "Biographies Famous Figures Historical Accounts",
#         "Science Books Physics Chemistry Biology",
#         "Technology Books Computing Programming",
        "Religious Texts Bibles Qurans Torahs"
    ],
    "Pharmacy And Health Products": [
        "Medications Supplements Chewable Tablets Pain Relief Tablets Vitamins Omega-3 Fish Oil Capsules Probiotic",
        "First Aid Supplies Band-Aids Antiseptic Wipes Sterile Gauze Pads Cold Packs Compress Hand Sanitizer",
        "DayQuil Severe Cold & Flu Relief Robitussin Maximum Strength Cough and Chest Congestion Kleenex Halls Cough Drops",
        "feminine hygiene products pads tampon tampax menstrual cups plan-b birth-control morning after pills panty liners",
        "percription glasses contacts cough drops",
        "Medical Equipment Blood Pressure Monitor Digital Thermometer Crutches Folding Walker Medical Scale wheelchair cane",
        
#         "Over-the-counter medications pain relievers",
#         "Prescription drugs antibiotics antivirals",
#         "Health supplements vitamins minerals",
#         "First aid kits bandages antiseptics",
#         "Personal care items toothbrushes razors",
#         "Skin care lotions creams sunscreens",
#         "Eye care contacts solutions glasses",
#         "Women's health products sanitary pads tampons",
#         "Men's health products shaving creams",
#         "Baby health products diapers creams",
#         "Oral care toothpaste mouthwash floss",
#         "Senior care aids walkers canes",
#         "Allergy relief antihistamines decongestants",
#         "Digestive health antacids probiotics",
        "Sleep aids melatonin valerian"
    ],
    "Pet Supplies": [
        "Pet Food Treats Dog snacks Dry dog canned food CHEW STICKS Puppy Formula",
        "Pet Toys Squeaky Plush Chew Toy Rubber Ball Fetch Frisbee Teething Ring",
        "Pet Grooming Products Flea and Tick Shampoo Deodorizing Pet Wipes Brush Clippers",
        "Pet Enclosures FISH TANK HAMSTER CAGE CAT LITTER REPTILE HEAT LAMP Scratching Posts Perches Pet Bed Bowl",
        "Pet Accessories DOG COLLAR Leash Pet ID Tag Treat Leash",
        "Aquarium Supplies Fish food Water conditioner Filter Tank decorations",
#         "Bird Care Seed mix Cage liner Aviary toys Beak conditioner",
#         "Reptile Supplies Terrarium substrate Heat mat UVB light",
#         "Small Animal Bedding Guinea pig food Hamster wheel Rabbit hutch",
        "Veterinary Supplies Pet medication Flea collar Dewormer Heartworm prevention"
    ],
    "Baby Products": [
        "Baby Care Items Monitor Baby Wipes HUGGIES Pampers BABY FORMULA Diaper Rash Cream Bottles Sippy Cup",
        "INF CAR SEAT infant STROLLER Carrier baby High Chair Changing Pad Booster Seat NURSERY CRIB",
        "Baby Toys Plush Rattle Teething Rings BBY Swaddle BLANKET Play Mat Rolly Cars Pacifier",
        "Diapers diaper-bag Pasifier",
        "Baby Clothing Onesies Socks Bibs Baby shoes Sleepwear",
#         "Feeding Supplies Breast pump Nursing cover Baby food Bibs Spoons",
#         "Healthcare Thermometer Nasal aspirator Baby toothbrush Vitamin drops",
#         "Safety Gates Baby monitors Outlet covers Corner guards",
        "Nursery Decor Mobiles Wall decals Night lights Bedding sets"
    ],
    "Cleaning Supplies": [
        "Cleaning Products LYSOL Wipes WINDEX Spray CLOROX BLCH GAIN 2X TIDE LQ PODS Disinfectants",
        "GLAD Trash Bags MR. CLEAN Magic Eraser SWIFFER Surface Cleaners OXICLEAN Stain Remover Floor Cleaners",
        "Laundry Detergents Dishwashing Supplies DAWN sponge Hand soap dispenser wash sanitizer sponge dish towel",
        "Cleaning Tools cloth paper towels broom WONDER MOP dustpan Odor Eliminator air freshener glade",
        "Bathroom Cleaners Toilet bowl cleaner Grout brush Shower spray",
#         "Kitchen Cleaners Degreaser Oven cleaner Dishwasher pods",
#         "Floor Care Vacuum bags Mop refill Hardwood floor polish",
        "Window Cleaning Glass cleaner Squeegee Microfiber cloth"
    ],
    "Gifts And Miscellaneous": [        
        "Gifts Wrapping Paper Gift Bags cardboard Boxes ribbons tape sewing kit",
        "Greeting Cards Envelopes HLMRK Hallmark Seasonal Items Christmas Ornaments Scented Candles advent calendar",
        "Musical instruments acoustic guitar Fender piano violin sheet music trumpet drum bass microphone Yamaha",
        "DRIVER LICENSE permit state ID certificate notarized",
        "Souvenirs keychain snowglobe magnet postcard stamps compass",
        "Piano Guitar Ukulele"
#         "Craft Supplies Yarn Paint Brushes Glue Beads",
#         "Party Supplies Balloons Streamers Tableware Confetti",
#         "Books Fiction Non-fiction E-books Magazines",
#         "Office Supplies Pens Notebooks Stapler Paper clips"
    ],
    "Event Tickets": [        
        "Movie Tickets Cinema Theatre Regal Consolidated Film Festival General Admission Child",
        "Honolulu Aquarium Tickets Zoo Museum Art Exhibition Planetarium Sports game",
        "Amusement Park Tickets Wet n Wild Season Pass Carnival Cirus Comedy Night Plane Ticket",
        "Event Tickets Blaisdell Symphony Concert Hall Ballet Dance Performance Opera Live music Band",
        "Seat Number Time Showing Taylor Swift Iam Tongi",
#         "Ticket Master LiveNation",
#         "Concert Tickets Rock Pop Jazz Festival Seating",
#         "Theater Broadway Plays Musicals Drama Comedy",
#         "Sports Events Soccer Baseball Basketball Hockey Tickets",
        "Festival Passes Music Food Wine Arts Crafts"
    ]
}

