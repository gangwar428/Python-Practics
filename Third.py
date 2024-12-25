# WAP to accept two numbers and display the Greater one out of two.

# def greater_number(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# result = greater_number(num1, num2)
# print(f"The greater number is: {result}")
    
first_num  = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

if first_num > second_num:
    print("First is greater than Second: ", first_num,  second_num)
elif first_num < second_num:
    print("Second is greater than First: ", second_num,  first_num)    
else:
    print("Number is Equal :", first_num,  second_num)   
     