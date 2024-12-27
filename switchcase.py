# WAP to accept a number from 1 to 7 and display corresponding week starting from SUNDAY.

print("Display corresponding week Days...")

num = int(input("Enter a number (1-7): "))

# Dictionary mapping numbers to days of the week
week_days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

if num in week_days:
    print(f"The corresponds to {week_days[num]}.")
else:
    print("Invalid number! Please enter a number between 1 and 7.")    

