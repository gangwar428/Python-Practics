# WAP to accept two dates (Current and Date of Birth) in DD MM YYYY format. 
# Calculate and display the age of person on Current Date in years ,
# months and days.( Hint: 30 days = 1 month and 12 month=1 year)

print("Age Calculator...")

print("Enter the current age of person")
curr_year = int(input("Enter year YYYY => "))
curr_month = int(input("Enter month MM => "))
curr_date = int(input("Enter date DD => "))

print("Enter the date of birth of person")

dob_year = int(input("Enter year YYYY => "))
dob_month = int(input("Enter month MM => "))
dob_date = int(input("Enter date DD => "))

# Initialize the variables

age_years = curr_year - dob_year
age_months = curr_month - dob_month
age_days = curr_date - dob_date

# Adjust the age if the date of birth is in the future

if age_days < 0:
    age_months -= 1
    age_days += 30

if age_months < 0:
    age_years -= 1
    age_months += 12
    
print(f"the Person is {age_years} years {age_months} months and {age_days} days")

