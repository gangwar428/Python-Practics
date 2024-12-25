# WAP to accept a number from user and display it is a Negative number or Positive number.
print("Display a number Negative or Positive ")

num = int(input("Enter a Number: "))

if num > 0:
    print("Number is Positive", num)
elif num < 0:
    print("Number is Negative", num)
else:
    print("Number is Zero", num)        