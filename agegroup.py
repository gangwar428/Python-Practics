# WAP to accept age of a person and display the Age Group as per the given condition.
# AGE            AGE GROUP
# <5                Baby
# >5 and <=12       Child
# >12 and <=19    Teenager
# >19 and <=30     Youth
# >30 and <=45     Young
# >45 and <=59     Adult
# >59            Senior Citizen

age = int(input("Enter the age of the Person: "))

if age < 5:
    print("The person must be Baby")
elif 5 < age <= 12:
    print("The person must be a child")        
elif 12 < age <= 19:
    print("The person must be a Teenager")
elif 19 < age <= 30:
    print("The person must be a Youth")
elif 30 < age <= 45:
    print("The person must be a Young")
elif 45 < age <= 59:
    print("The person must be an Adult")
else:
    print("The person must be a Senior Citizen")                    