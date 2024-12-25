# WAP to accept Selling Price and Cost Price of an Item and Display it is Profit or Loss.

print("Display Item Profit and Loss")

cost_price = float(input("Enter the cost price of the Item => "))
selling_price = float(input("Enter the selling price of the Item => "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("The Item is Profitable with a Profit of", profit)
elif selling_price == cost_price:
    print("The Item is neither Profitable nor Loss, it is at the Cost Price")
else:
    loss = cost_price - selling_price
    print("The Item is in Loss with a Loss of", loss)