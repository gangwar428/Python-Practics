# WAP to accept two distances in feet and inches. Add the two distances 
# to give total distance in feet and inches.(Hint: 12 inches = 1 feet)

print("Distance Calculator...")
print("Enter the first distance")
feet1 = int(input("Enter the first distance in feet for the first object => "))
inches1 = int(input("Enter the first distance inches for the second object => "))

print("Enter the second distance")
feet2 = int(input("Enter the Second distance in feet for the first object => "))
inches2 = int(input("Enter the Second distance inches for the second object =>"))

# tatal inches 

total_inches = inches1 + inches2

# Convert total inches to feet and inches

extra_feet = total_inches // 12
remaining_inches = total_inches % 12
total_feet = feet1 + feet2 + extra_feet

print("Total Distance in feet and inches: ", total_feet, "feet", remaining_inches, "inches")

