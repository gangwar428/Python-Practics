# WAP to accept a number and display it is a multiple of 8 or not.
print("Check your Number is multiple of 8 or not.")

num = int(input("Enter a Number: "))

if num % 8 == 0:
    print("Number is divisible by 8=>", num)
else:
    print("Number is not divisible by 8=>", num)    
    
    