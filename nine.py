# WAP to input Year from user. Display whether the year is a leap year or not.

print("Checking if the Year is a Leap Year or Not..")

year = int(input("Enter a Year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Year is leap year", year)
else:
    print("Year is not a leap year", year)