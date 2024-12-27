# WAP to accept marks of 5 subjects out of 100 each and display the grade scored as per the given condition
#  Percentage      Grade
#    >=90           A
# <90 and >=75      B
# <75 and >=60      C
# <60 and >=33      D
#     <33           E

print("---Grade Score ---")

hindi = int(input("Enter the Hindi marks: "))
maths = int(input("Enter the  Math marks: "))
computer = int(input("Enter the Computer marks: "))
english = int(input("Enter the English marks: "))
science = int(input("Enter the Science marks: "))

total_marks = hindi + maths + computer + english + science

percentage_score = (total_marks / 500) * 100

if percentage_score >= 90:
    print("Grade A")
elif 75 <= percentage_score < 90:
    print("Grade B")  
elif 60 <= percentage_score < 75:
    print("Grade C")    
elif 33 <= percentage_score < 60:
    print("Grade D")
else:
    print("Grade E")
 