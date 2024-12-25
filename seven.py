# WAP to accept age of a person and display whether the person is eligible for Voting or not.
print("Checking Eligibility for Voting...")
age = int(input("Enter the age of the person => "))

if age >= 18:
    print("Eligible for Voting", age)
else:
    print("Not Eligible for Voting", age)