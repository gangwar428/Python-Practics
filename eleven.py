# WAP to accept a number from user. If number is greater than 20,
# display its Square otherwise display its Cube.

num = int(input("Enter a Number: "))

if num > 20:
    square = num * num
    print(f"The square of {num} is: {square}")
elif num <= 20:
    cube = num * num * num
    print(f"The cube of {num} is: {cube}")
else:
    print("Invalid number!.")