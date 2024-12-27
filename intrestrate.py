# A Banker offers an Interest rate as per the given Criteria
# Time in Years    Interest Rate
#    <=5              6.5 %
#  >5 and <=10        9.0 %
#  >10 and <=20       12.0 %
#   >20               18.0 %
#WAP to accept amount deposited and time in years of depositing. 
# Calculate and display the Interest earned in Rs. Also Display the Amount received after the specified time.

print("Calculate the Interest and Amount after specified years")
principal_amt = float(input("Enter the amount deposited => "))
years = int(input("Enter the time in years => "))

if years <= 0 or principal_amt <= 0:
    if years <= 0 and principal_amt <= 0:
        print("Invalid input! Both time and amount must be positive.")
    elif years <= 0:
        print("Invalid input! Time must be positive.")
    elif principal_amt <= 0:
        print("Invalid input! Amount must be positive.")
    exit()

if years <= 5:
    interest_rate = 6.5
    interest = (principal_amt * interest_rate * years) / 100
    total_amt = interest + principal_amt
    print(f"Amount Received after {years} years: Rs.{total_amt:.2f}")
elif 5 < years <= 10:
    interest_rate = 9.0
    interest = (principal_amt * interest_rate * years) / 100
    total_amt = interest + principal_amt
    print(f"Amount Received after {years} years: Rs.{total_amt:.2f}")
elif 10 < years <= 20:
    interest_rate = 12.0
    interest = (principal_amt * interest_rate * years) / 100
    total_amt = interest + principal_amt
    print(f"Amount Received after {years} years: Rs.{total_amt:.2f}")
else:
    interest_rate = 18.0
    interest = (principal_amt * interest_rate * years) / 100
    total_amt = interest + principal_amt
    print(f"Amount Received after {years} years: Rs.{total_amt:.2f}")