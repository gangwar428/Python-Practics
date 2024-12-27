# A Company pay its employees as per the given criteria
# If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary and 
# DA = 90% of basic salary. If his salary is either equal to or above Rs. 1500, 
# then HRA = Rs. 500 and DA = 98% of basic salary. If the employee's salary is input by the user 
# write a program to find his gross salary.
# Where gross salary = basic salary + DA + HRA

print("Find Gross salary from employee...")

salary = int(input("Enter the salary from employee in RS. => "))

if salary < 1500:
    Hra = (10/100) * salary
    Da = (90/100) * salary
    gross_salary = salary + Hra + Da
    print(f"The gross salary of employee is RS. {gross_salary} .")

elif salary >= 1500:
    Hra = 500
    Da = (98/100) * salary
    gross_salary = salary + Hra + Da
    print(f"The gross salary of employee is RS. {gross_salary} .")
else:
    print("Invalid salary amount.")    