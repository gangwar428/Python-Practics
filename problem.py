"""a = int(input('1='))
b = int(input('2='))
print(a*b)"""

'''num = int(input('Enter a number:'))
if type(num) == int:
    print("Yes it is int")
elif type(num) == float:
    print("No. is float")'''
    
'''guessed = 5
second_g = 4

user = int(input("Enter a number"))
if (user == guessed or user == second_g):
     print("Congratulations! You guessed correctly.")'''
     
num1 = int(input("Enter first number: "))
num2 = int(input("Enter another number: "))   
operator = input("operator + - * >")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
else:
    print("Invalid operator")    
            