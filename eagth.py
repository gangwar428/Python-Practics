# WAP to accept Selling Price and Cost Price of an Item. In case of Profit, 
# display Profit Amount and Profit Percent otherwise display Loss amount and Loss Percent.
print("Display profit amount and Loss amount with percentage")
cost_price = float(input("Enter the cost price => "))
selling_price = float(input("Enter the Selling price => "))

if selling_price > cost_price:
    profit_amount = selling_price - cost_price
    profit_percent = (profit_amount / cost_price) * 100
    print("Profit Amount:", profit_amount)
    print(f"profit percentage: {profit_percent:.2f}%.")

elif selling_price < cost_price:
    loss_amount = cost_price - selling_price
    loss_percent = (loss_amount / cost_price) * 100
    print("Loss Amount:", loss_amount)
    print(f"Loss Percent: {loss_percent:.2f}%.")
    
else:
    print("The cost price and selling price are equal.")