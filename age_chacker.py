# Write a program that takes a user’s birth year and current year,
# then calculates their age and checks if they are 18 or older.

print("---- Age Chacker ----")
# get the user input of current year and birth year 
Current_year = int(input("Enter the current Year: "))
birth_year = int(input("Enter the birth Year: "))

# calculate the age

age = Current_year - birth_year

# Check conditions
if age > 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")
# print age
print(f"You are {age} years old.")            