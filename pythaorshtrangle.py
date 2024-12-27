# WAP to accept three sides of a Triangle and display it is a Pythagoras Triplet or not.

a = int(input("Enter the first triplet => "))
b = int(input("Enter the second triplet => "))
c = int(input("Enter the third triplet => "))

# a**2 + b**2 = c**2

if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("The given triplet is a Pythagorean Triplet")
else:
    print("The given triplet is not a Pythagorean Triplet")
