# WAP to accept a number from 1 to 12 and display Corresponding month.

# def display_month(month_num):
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#     if month_num >= 1 and month_num <= 12:
#         return months[month_num - 1]
#     else:
#         return "Invalid month number"
    
# month_num = int(input("Enter a month number (1 - 12): "))
# print(display_month(month_num))    

# Using Another method

print("Display month name...")

month_num = int(input("Enter a month number (1 - 12): "))

month_name = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

if month_num in month_name:
    print(f"Month {month_num} is: {month_name[month_num]}")
else:
    print("Invalid month number! please Enter a number between (1 - 12)")    
