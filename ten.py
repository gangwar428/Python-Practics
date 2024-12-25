# WAP to accept an alphabet from user. If it is Capital, 
# convert it to small and if small then convert to capital.

print("Convert Capital to small and Small to Capital")

char = input("Enter a character => ")

if char.isupper():
    print("Convert lowerCase: ",char.lower())
else:
    print("Convert UpperCase ",char.upper())    