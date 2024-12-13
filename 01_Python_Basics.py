Python Basics
Author: Ritesh Gangwar / gangwar428
Date: 13/12/2024
Description: A simple introduction to Python syntax, variables, and basic concepts.

What is Python?
Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and released in 1991. Python is widely used for:

Web Development (e.g., Django, Flask)
Data Analytics(e.g., Numpy, Pandas, Matplotlib, Seaborn)                                                                                                                                                                                
Data Science and Machine Learning (e.g., Pandas, NumPy, Scikit-learn)
Automation (e.g., scripting tasks)
Game Development
Desktop Applications
Python is popular because:

Easy to Learn: The syntax is straightforward and beginner-friendly.
Versatile: It works for small scripts as well as complex projects.
Extensive Libraries: A rich ecosystem of libraries and frameworks.  
  

Python Syntax:
Python syntax is simple and clean, making the code easy to read and write. Key elements include:

1. Indentation
Python uses indentation (spaces or tabs) to define blocks of code, unlike other languages that use braces {}.
Indentation is mandatory, and the number of spaces must be consistent within a block.

print("Welcome to Python!")
                   
                   
# Print a message in Python
print("Welcome to Python Programming!")
print("Hello! Duniya")  

# Variables and Data Types
x = 10         # Integer
y = 3.14       # Float
z = "Hello"    # String

print(x, y, z) 
# Output all variables (10 3.14 Hello)


# Taking input
name = input("What's your name? ")
print("Hello,", name)

# Output is (Hello What's your name?)

# Conditional Example
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

# Loop Example
for i in range(3):
    print("This is loop iteration number:", i)

# Simple Function
def greet_user(username):
    print("Welcome,", username)

greet_user(name)  # Calling the function


Key Points Covered:
Printing: Use print() to display output.
Variables: Assign values directly, e.g., x = 10.
Input: Use input() to take user input.
Conditionals: Use if and else for decisions.
Loops: for loop example included.
Functions: A simple reusable function.
