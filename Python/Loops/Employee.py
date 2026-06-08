# 12.Employee Salary System 

n = int(input("Enter number of employees : "))

for i in range(1, n + 1):

    salary = float(input(f"\nEnter salary of Employee {i} : "))

    if salary < 30000:
        bonus = salary * 0.10
        tax = salary * 0.05

    else:
        bonus = salary * 0.15
        tax = salary * 0.10

    final_salary = salary + bonus - tax

    print("Salary :", salary)
    print("Bonus :", bonus)
    print("Tax :", tax)
    print("Final Salary :", final_salary)
