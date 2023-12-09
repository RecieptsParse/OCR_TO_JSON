example_1_input = '''H
MART <UNKNOWN>
http://www.hmart.com
458 Keawe st
Honolulu, <UNKNOWN> 96813
TEL <UNKNOWN>
Your Cashier was
SY RAMEN HOT MULTI
8.99 B
IND MI GORENG NOOD
4.99 B
HT BEEF DUMPLING D
19.99 B
NS SHRIMP HOT SNCK
1.99 B
ME AZUKI ICE CREAM
6.49 B
TAX
2.00
**** BALANCE
44.45
Discover Credit - C
ACCOUNT <UNKNOWN>
***********1153
APPROVAL CODE: 01669R
SEQUENCE NUMBER: 33790
No CVM
Amount:USD $44.45
CARD:Discover CREDIT XXXX1153 EMV
APPROVAL CODE 01669R
AID:A0000001523010
TVR: 0000008000
<UNKNOWN>
TSI: E800
APPLICATION CRYPTOGRAM A433DC30B1FE402
APPLICATION PREFERRED NAME:Discover Cr
APPLICATION LABEL:Discover
<UNKNOWN>
ARC:00
RespDate: 07152023
Resp <UNKNOWN> 201640
<UNKNOWN>
TOTAL AMOUNT: $44.45
RESPONSE CODE: APPROVED
07/15/23 08:16pm 103 2
Discover
44.45
CHANGE
0.00
TOTAL NUMBER OF ITEMS SOLD =
5
07/15/23 08:17pm 81 2 281 103
** RETURN POLICY **
Unused product can be exchanged or
refunded with receipt within 7 days of
purchase unless otherwise noted below
Meat, fish, produce and refrigerated
food items must be returned with
receipt within 24 hours.
Electronics and <UNKNOWN> Must be
returned with receipt within 14 days
of purchase and must be unused.
If you are unable to <UNKNOWN> item to
store. please call customer service.
00008100202812307152017
<UNKNOWN> Thank You and Please Come Again **'''

example_1_output='''{{"merchant":"H MART","address":"458 Keawe st","city":"Honolulu","state":"HI","phoneNumber":"","tax":"2.00","total":"44.45","receiptDate":"07/15/23","receiptTime":"08:16pm","totalItems":"5","paymentType":"credit","diningOptions":"","creditCardType":"Discover","totalDiscount":"0.00","ITEMS":[{{"description":"SY RAMEN HOT MULTI","unabbreviatedDescription":"Sy Ramen Hot Multi","includedItems":[],"quantity":"1","unitPrice":"8.99","totalPrice":"8.99","discountAmount":"0.00"}},{{"description":"IND MI GORENG NOOD","unabbreviatedDescription":"Ind Mi Goreng Noodle","includedItems":[],"quantity":"1","unitPrice":"4.99","totalPrice":"4.99","discountAmount":"0.00"}},{{"description":"HT BEEF DUMPLING D","unabbreviatedDescription":"Hot Beef Dumpling","includedItems":[],"quantity":"1","unitPrice":"19.99","totalPrice":"19.99","discountAmount":"0.00"}},{{"description":"NS SHRIMP HOT SNCK","unabbreviatedDescription":"Shrimp Hot Snack","includedItems":[],"quantity":"1","unitPrice":"1.99","totalPrice":"1.99","discountAmount":"0.00"}},{{"description":"ME AZUKI ICE CREAM","unabbreviatedDescription":"Azuki Ice Cream","includedItems":[],"quantity":"1","unitPrice":"6.49","totalPrice":"6.49","discountAmount":"0.00"}}]}}'''

example_2_input ='''<UNKNOWN> PURCHASE **
Panda Express #2150
Honclulu, HI
(808)956-7229
6/9/2023 11:02:50 AM
-TO GO-
Order: 260527
Server: LamTan T
1 Plate
10.60
FRIED RICE-1/2
FRIED <UNKNOWN>
STR BN CKN BRST
ORANGE CKN
1 XTRA ENTREE
1.50
VEG SPRING <UNKNOWN>
<UNKNOWN>
12.10
TAX
0.57
Total
12.67
Visa
12.67
Acct XXXXXXXX9212
<UNKNOWN> 060248
*Card details below
EMV: Contactless
APL: VISA DEBIT
AID: A0000000031010
Panda Rewards has arrived!
<UNKNOWN>
Sign Up at <UNKNOWN>
*
* Enter Unique Rewards Code to earn *
PANDA POINTS on this order!
*
*Code valid for 7 days from purchase*
Unique Rewards Code:
558844128417
WE'D LOVE TC HEAR FROM YOU!
Share your thoughts and receive
a Free Small A La Carte Entree
*
w/purchase of a 2-entree Plate.
*
<UNKNOWN> 2 days, go to
*
<UNKNOWN>
<UNKNOWN>
*
<UNKNOWN>
*
*
*
Survey Code:
<UNKNOWN>
*
*
Email <UNKNOWN> quired to receive coupon
*
*
*General Manager with $100K potential
Join the Panda team!
PandaCareers.com'''

example_2_output ='''{{"merchant":"Panda Express","address":"","city":"Honclulu","state":"HI","phoneNumber":"(808)956-7229","tax":"0.57","total":"12.67","receiptDate":"6/9/2023","receiptTime":"11:02:50 AM","totalItems":"2","paymentType":"Debit","diningOptions":"TO GO","creditCardType":"Visa","totalDiscount":"0.00","ITEMS":[{{"description":"Plate","unabbreviatedDescription":"Plate","includedItems": ["FRIED RICE-½", "FRIED","STR BN CKN BREAST","ORANGE CKN"],"quantity":"1","unitPrice":"10.60","totalPrice":"10.60","discountAmount":"0.00"}},{{"description":"XTRA ENTREE","unabbreviatedDescription":"Extra Entree","includedItems":["VEG SPRING"],"quantity":"1","unitPrice":"1.50","totalPrice":"1.50","discountAmount":"0.00"}}]}}'''

example_3_input='''Longs Drugs <UNKNOWN>
4211 WAIALAE AVE
HONOLULU, HI 96816
808.732.0781
REG#10 TRN#4352 CSHR#0000095 STR#9220
1 CFRIO SF PEG BAG 3Z 4.59B
1 CFRIO SF PEG BAG
3Z
4.59B
1 CFRIO SF PEG BAG
3Z
4.59B
1 CR GYSR SPR WTR
33.8
1.29B
1
BOTTLE DEPOSIT
.05F
1 HI CONTAINER FEE
.01F
1 CR GYSR SPR WTR
33.8
1.29B
1 BOTTLE DEPOSIT
.05F
1 HI CONTAINER FEE
.01F
9 ITEMS
Survey ID #
4378 6100 0784 757 18
SUBTOTAL
16.47
HI 4.712% TAX
.77
TOTAL
17.24
CHARGE
17.24
************2130
RF
CHASE VISA
************2130
APPROVED# 04998D
REF# 103528
TRAN TYPE: SALE
AID: A0000000031010
TC: BD71734C41358DEE
TERMINAL# 84206407
NO SIGNATURE REQUIRED
CVM: 1F0000
<UNKNOWN> 0000000000
TSI(9B): 0000
CHANGE
.00
3509 2203 1844 3521 08
Returns with receipt, subject to
CVS Return Policy, thru 09/01/2023
Refund amount is based on price
after all coupons and discounts.
JULY 3, 2023
2:48 PM
<UNKNOWN> <UNKNOWN> <UNKNOWN> <UNKNOWN> <UNKNOWN> <UNKNOWN> <UNKNOWN>
<UNKNOWN>
GET YOUR CVS EXTRACARE CARD
We would love to hear your feedback
on your recent experience with us.
This survey will take only
1 minute to complete.
Share Your Feedback
<UNKNOWN>
Hablamos español
THANK YOU. SHOP 24 HOURS AT CVS.COM'''

example_3_output='''{{"merchant":"Longs Drugs","address":"4211 WAIALAE AVE","city":"HONOLULU","state":"HI","phoneNumber":"808.732.0781","tax":"0.77","total":"17.24","receiptDate":"JULY 3, 2023","receiptTime":"2:48 PM","totalItems":"6","paymentType":"Credit","diningOptions":"","creditCardType":"CHASE VISA","totalDiscount":"0.00","ITEMS":[{{"description":"CFRIO SF PEG BAG","unabbreviatedDescription":"CoffeeRio Peg Bag","includedItems":[],"quantity":"3","unitPrice":"4.59","totalPrice":"13.77","discountAmount":"0.00"}},{{"description": "CR GYSR SPR WTR","unabbreviatedDescription":"Crystal Geyser Spring Water","includedItems":[],"quantity":"2","unitPrice":"1.29","totalPrice":"2.58","discountAmount":"0.00"}},{{"description":"BOTTLE DEPOSIT","unabbreviatedDescription":"Bottle Deposit","includedItems":[],"quantity":"2","unitPrice":"0.05","totalPrice":"0.10","discountAmount":"0.00"}},{{"description":"HI CONTAINER FEE","unabbreviatedDescription":"HI Container Fee","includedItems":[],"quantity":"2","unitPrice":"0.01","totalPrice":"0.02","discountAmount":"0.00"}}]}}'''

example_4_input='''129
For question comments or concerns
Call McDonald's Hotline
800-683-5587
Now Delivering with
Door Dash
Survey Code:
14616-01290-70423-16249-00085-
McDonald's Restaurant #14616
3549 RUSSETT GREEN E (WM#1985)
MD
ANNE
<UNKNOWN> 20724
TEL# 301-7767980
Thank You Valued Customer
KS# 1
07/04/2023 04:24 PM
Sidel
Order 29
1 Happy Meal Ch Burger
4.39
1 Cheeseburger
NO Pickle
1 Extra Kids Fry
1 Apple Juice
1 S Apl Jc Surcharge
1 ELEMENTAL
1 S Grimace Bday Shake
3.69
1 S Shake Surcharge
Subtotal
8.08
Tax
0.48
Take-Out Total
8.56
Cashless
8.56
Change
0.00
MER# 464239
CARD ISSUER
ACCOUNT#
Visa SALE
<UNKNOWN>
TRANSACTION AMOUNT
8.56
CONTACTLESS
AUTHORIZATION CODE - 03172D
SEQ# 035443
AID: A0000000031010
Now Hiring
Text MD349 To 38000
Sign up for MyMcDonald's rewards
to earn points on future visits'''

example_4_output='''{{"merchant":"McDonald's","address":"3549 RUSSETT GREEN E","city":"LAUREL","state":"MD","phoneNumber":"800-683-5587","tax":"0.48","total":"8.56","receiptDate":"07/04/2023","receiptTime":"04:24 PM","totalItems":"2","paymentType":"CREDIT","diningOptions":"Take-Out","creditCardType":"Visa","totalDiscount":"0.00","ITEMS":[{{"description":"Happy Meal Ch Burger","unabbreviatedDescription":"Happy Meal Cheese Burger","includedItems":["Cheeseburger","NO Pickle","Extra Kids Fry","Apple Juice","S Apl Jc Surcharge","ELEMENTAL"],"quantity":"1","unitPrice":"4.39","totalPrice":"4.39","discountAmount":"0.00"}},{{"description":"S Grimace Bday Shake","unabbreviatedDescription":"Grimace Birthday Shake","includedItems":["S Shake Surcharge"],"quantity":"1","unitPrice":"3.69","totalPrice":"3.69","discountAmount":"0.00"}}]}}'''

example_5_input='''Longs Drugs <UNKNOWN>
91-919 FORT WEAVER RD
EWA BEACH, HI 96706
808.689.5860
REG#01 TRN#8020 CSHR#2262192 STR#7356
Helped by: JEFFREY
ExtraCare Card <UNKNOWN>
1858
1 OREO ORIG DBL STFF 14.0
2.93B
ORIGINAL PRICE
6.99
2/9.00
2.49 -
COUPON SAVINGS
1.57 -
1 BAUD WAFER CHOCLT <UNKNOWN>
<UNKNOWN>
ORIGINAL PRICE
2.69
3/5.00
1.02 -
COUPON SAVINGS
.57 -
1 HWNISL TEABG GVGNS <UNKNOWN>
3.60B
ORIGINAL PRICE
5.49
COUPON SAVINGS
1.89 -
COUPONS APPLIED
1 $4 OFF YOUR PURCHASE
4.00 - CVS
1 2% BACK IN <UNKNOWN> R
.03 - CVS
3 ITEMS
SUBTOTAL
7.63
HI 4.712% TAX
.36
TOTAL
7.99
DEBIT
7.99
3476
CH
US DEBIT
3476
APPROVED# 003818
REF# 010205
TRAN <UNKNOWN> SALE
AID: A0000000042203
<UNKNOWN> <UNKNOWN>
TERMINAL# 84198694
PIN VERIFIED ONLINE
CVM: 420300
<UNKNOWN> 0000048000
TSI(9B): E800
CHANGE
00
Returns Return with 0200 12
3507 3563 1998
CVS Refund amount <UNKNOWN> thru subject to
after all coupons is based and discounts. 09/16/2023 on <UNKNOWN>
JULY 18, 2023
7:38 PM
<UNKNOWN> <UNKNOWN>'''

example_5_output='''{{"merchant":"Longs Drugs","address":"91-919 FORT WEAVER RD","city":"EWA BEACH","state":"HI","phoneNumber":"808.689.5860","tax":"0.36","total":"7.99","receiptDate":"JULY 18, 2023","receiptTime":"7:38 PM","totalItems":"3","paymentType":"DEBIT","diningOptions":"","creditCardType":"","totalDiscount":"7.54","ITEMS":[{{"description":"OREO ORIG DBL STFF","unabbreviatedDescription":"Oreo Double Stuff","includedItems":[],"quantity":"1","unitPrice":"6.99","totalPrice":"2.93","discountAmount":"4.06"}},{{"description":"BAUD WAFER CHOCLT","unabbreviatedDescription":"Wafer Chocolate","includedItems":[],"quantity":"1","unitPrice":"2.69","totalPrice":"1.10","discountAmount":"1.59"}},{{"description":"HWNISL TEABG GVGNS","unabbreviatedDescription":"Teabag","includedItems":[],"quantity":"1","unitPrice":"5.49","totalPrice":"3.60","discountAmount":"1.89"}}]}}'''

example_6_input='''
Store 215 Dir Dane Elder
Main:(808) 396-6337
377 Keahole Street
HONOLULU HI 96825
00021505202752310131927
YOUR CASHIER TODAY WAS SELF
GROCERY
Price
You Pay
7889530002 OYSTER SAUCE 180Z
6.79
6.79 B
BAKED GOODS
22381100000 QRT CK LEMON
8.99
8.99 B
MEAT
4262900325 NY STYLE GRND PORK
6.49
6.49 B
PRODUCE
4069
GREEN CABBAGE
7.98
7.98 B
WT
4.46 <UNKNOWN> @ $1.79 /lb
4238
REDUCED BANANAS
4.49
4.49 B
WT
3.23 <UNKNOWN> @ $1.39 /lb
TAX
1.64
****
BALANCE
36.38
Credit Purchase 10/13/23 19:27
<UNKNOWN> # ************1301
<UNKNOWN> <UNKNOWN> AUTH: <UNKNOWN>
PAYMENT AMOUNT
36.38
AL VISA CREDIT
AID A0000000031010
TVR 0000000000
TSI 0000
Visa
36.38
CHANGE
0.00
YOUR REWARDS
Points Towards Next Reward 34 of 100
TOTAL NUMBER OF ITEMS SOLD =
5
10/13/23 19:27 215 52 275
8852
Thank you for shopping <UNKNOWN>
For SAFEWAY FOR <UNKNOWN> questions call
877-276-9637 or Safeway.com/foru'''

example_6_output='''{{"merchant":"SAFEWAY","address":"377 Keahole Street","city":"HONOLULU","state":"HI","phoneNumber":"(808) 396-6337","tax":"1.64","total":"36.38","receiptDate":"10/13/23","receiptTime":"19:27","totalItems":"5","paymentType":"Credit","diningOptions":"","creditCardType":"Visa","totalDiscount":"0.00","ITEMS":[{{"description":"OYSTER SAUCE 18OZ","unabbreviatedDescription":"Oyster Sauce 18oz","includedItems":[],"quantity":"1","unitPrice":"6.79","totalPrice":"6.79","discountAmount":"0.00"}},{{"description":"QT CK LEMON","unabbreviatedDescription":"Quart Chicken Lemon","includedItems":[],"quantity":"1","unitPrice":"8.99","totalPrice":"8.99","discountAmount":"0.00"}},{{"description":"NY STYLE GRND PORK","unabbreviatedDescription":"New York Style Grand Pork","includedItems":[],"quantity":"1","unitPrice":"6.49","totalPrice":"6.49","discountAmount":"0.00"}},{{"description":"GREEN CABBAGE","unabbreviatedDescription":"Green Cabbage","includedItems":["4.46 lb @ $1.79 /lb"],"quantity":"1","unitPrice":"7.98","totalPrice":"7.98","discountAmount":"0.00"}},{{"description":"REDUCED BANANAS","unabbreviatedDescription":"Reduced Bananas","includedItems":["3.23 lb @ $1.39 /lb"],"quantity":"1","unitPrice":"4.49","totalPrice":"4.49","discountAmount":"0.00"}}]}}'''

example_7_input='''Longs <UNKNOWN> <UNKNOWN>
2470 S KING ST
HONOLULU, HI 96826
808.947.2651
REG#13 TRN#4266 CSHR#0000092 STR#9954
ExtraCare Card <UNKNOWN>
********7703
F 1 CVS LINER UNSC DB
135S
3.99N
F 1 CVS LINER UNSC DB 135S 3.99N
F 1 HALLS COOL BRRY CD 70CT 6.49T
3 ITEMS
SUBTOTAL
14.47
HI 4.712% TAX
.31
TOTAL
14.78
CASH
20.00
CHANGE
5.22
3509 9543 2884 2661 38
Returns with receipt, subject to
CVS Return Policy, thru 12/14/2023
Refund amount is based on price
after all coupons and <UNKNOWN>
OCTOBER 15, 2023
11:34 AM
Feeling sick? We offer COVID+FLU testing
in select CVS Locations, two tests in
one swab. Appointments are required.
Results available in 1 to 3 days. Make
your appointment today at CVS.com. Flu
test recommended within 1-2 days of
symptom onset.
The sales tax on period products is $0.38,
which CVS paid on your behalf.
F=FLEXIBLE SPENDING ACCT SUMMARY (FSA)
Health Care Eligible Total 14.78
FSA summary above includes items
<UNKNOWN> tax) that may be eligible for plan
reimbursement. Restrictions may apply.
THANK YOU. OPEN 24 HOURS 7 DAYS A WEEK
ExtraCare Card balances as of 09/12
Year to Date Savings
93.93
Fill 10 prescriptions Get $5EB
Pharmacy and Health ExtraBucks
Quantity Toward this Reward
15
Quantity Needed to Earn Reward
5
Pharmacy & Health Rewards Enrollment Status
Active Members
2
Access all coupons & rewards, and
track your 2% earnings in the CVS
Pharmacy app!'''

example_7_output='''{{"merchant":"Longs","address":"2470 S KING ST","city":"HONOLULU","state":"HI","phoneNumber":"808.947.2651","tax":"0.31","total":"14.78","receiptDate":"OCTOBER 15, 2023","receiptTime":"11:34 AM","totalItems":"3","paymentType":"CASH","diningOptions":"","creditCardType":"","totalDiscount":"0.00","ITEMS":[{{"description":"CVS LINER UNSC DB","unabbreviatedDescription":"CVS Liner Unscented Double","includedItems":["135S"],"quantity":"2","unitPrice":"3.99","totalPrice":"7.98","discountAmount":"0.00"}},{{"description":"HALLS COOL BRRY CD 70CT","unabbreviatedDescription":"Halls Cool Berry Cough Drops","includedItems":[],"quantity":"1","unitPrice":"6.49","totalPrice":"6.49","discountAmount":"0.00"}}]}}'''

# prompt examples to train model
def get_prompt_examples():
    return [
    {"ExampleInput": example_1_input, "ExampleOutput": example_1_output},
    {"ExampleInput": example_2_input, "ExampleOutput": example_2_output},
    {"ExampleInput": example_3_input, "ExampleOutput": example_3_output},
    {"ExampleInput": example_4_input, "ExampleOutput": example_4_output},
    {"ExampleInput": example_5_input, "ExampleOutput": example_5_output},
    {"ExampleInput": example_6_input, "ExampleOutput": example_6_output},
    {"ExampleInput": example_7_input, "ExampleOutput": example_7_output},
]