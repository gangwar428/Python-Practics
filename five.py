# WAP to accept a number and display it is a factor of 48 or not.

num = int(input("Enter a Number => "))

if 48 % num == 0:
    print(num,"Number is factor of 48")
else:
    print(num,"Number is not factor of 48")   
 