# A Shopkeeper offers discount as per the given criteria on Purchase Amount
# Purchase Amount    Discount rate
#   <=5000              5 %
# >5000 and <=10000     8 %
# >10000 and <=25000    12%
# >25000 and <=50000    17%
#   >50000              23 %
# WAP to accept purchase amount from user. 
# Calculate and display Discount in Rs. Also display the Amount to pay after discount.

purchase_amount = int(input("Enter the purchase amount in RS. "))

if purchase_amount <= 0:
    print("Invalid purchase amount! Amount must be positive.")
    exit()

if purchase_amount <= 5000:
    discount = purchase_amount * 5 / 100
    discount_amount = purchase_amount * (5 / 100)
    amount_to_pay = purchase_amount - discount_amount
    print("Discount Amount:", discount_amount, "Amount to pay:", amount_to_pay)
elif 5000 < purchase_amount <= 10000:
    discount = purchase_amount * 8 / 100
    discount_amount = purchase_amount * (8 / 100)
    amount_to_pay = purchase_amount - discount_amount
    print("Discount Amount:", discount_amount, "Amount to pay:", amount_to_pay)
elif 10000 < purchase_amount <= 25000:
    discount = purchase_amount * 12 / 100
    discount_amount = purchase_amount * (12 / 100)
    amount_to_pay = purchase_amount - discount_amount
    print("Discount Amount:", discount_amount, "Amount to pay:", amount_to_pay)
elif 25000 < purchase_amount <= 50000:
    discount = purchase_amount * 17 / 100
    discount_amount = purchase_amount * (17 / 100)
    amount_to_pay = purchase_amount - discount_amount
    print("Discount Amount:", discount_amount, "Amount to pay:", amount_to_pay)
else:
    discount = purchase_amount * 23 / 100
    discount_amount = purchase_amount * (23 / 100)
    amount_to_pay = purchase_amount - discount_amount
    print("Discount Amount:", discount_amount, "Amount to pay:", amount_to_pay)