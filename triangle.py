# WAP to check whether a triangle is valid or not,
# when the three angles of the triangle are entered through the keyboard.
# A triangle is valid if the sum of all the three angles is equal to 180 degrees.

print("Checking Validity of a Triangle...")
angle1 = float(input("Enter the first angle of the triangle => "))
angle2 = float(input("Enter the second angle of the triangle => "))
angle3 = float(input("Enter the third angle of the triangle => "))

sum  = angle1 + angle2 + angle3

if sum == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("The Triangle is Valid")
else:
    print("The Triangle is Invalid")            