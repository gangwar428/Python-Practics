# A banker gives and Interest rate of 4.5%, if amount is deposited for up to 4 years 
# otherwise gives an Interest rate of 7.25%. WAP to accept amount Deposited and 
# time in years and Display the Amount received after specified years.

print("Calculate the Amount after specified years")
principal_amt = float(input("Enter the amount deposited => "))
years = int(input("Enter the time in years => "))

if principal_amt <= 0 and years <= 0:
    print("Invalid input! Amount and time must be positive.")
    exit()
else:
    if years <= 4:
        interest_rate = 4.5
        interest = (principal_amt * interest_rate * years) / 100
        total_amt = interest + principal_amt
        print(f"Amount Received after {years} years: Rs.{total_amt:.2f}")
    else:
        interest_rate = 7.25
        interest = (principal_amt * interest_rate * years) / 100
        total_amt = interest + principal_amt
        print(f"Amount Received after {years} years: Rs.{total_amt:.2f}")    