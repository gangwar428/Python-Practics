# WAP to accept a number from user and display it is an Even number or Odd number.
print("Display number is Even or Odd")
num = int(input("Enter a Number: "))

if num % 2 == 0:
    print("Numver is Even ", num)
elif num % 2 == 1:
    print("Number is Odd ", num)
else:
    print("Invalid number, enter a valid number")
        