# WAP to accept three numbers and display the greater one.

print("Find the Greater Number...")

def greater_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


result = greater_number(num1, num2, num3)
print(f"The greater number is: {result}")