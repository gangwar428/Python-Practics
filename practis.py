# Welcome message

print("Welcome to BMI Calculator")
# user input
hight = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in Kilograms: "))
# NOW CALCULATE THE BMI

bmi = weight / (hight**2)
value = ("%.2f" % bmi)
# now print the BMI

print("Your BMI is: ", value)