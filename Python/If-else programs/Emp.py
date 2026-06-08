# 8. Employee Salary Bonus System 
# Input: 
# ● Salary 
# ● Years of experience 
# ● Performance rating 
# Conditions: 
# ● Experience > 5 years → 20% bonus 
# ● Rating A → Extra 10% 
# ● Rating B → Extra 5% 
# ● Otherwise no extra bonus 
# Print final salary.

salary=int(input("Enter your salary : "))
experience=int(input("Enter your experience : "))
rating=input("Enteer the rating : ")

if(experience>5):
    salary=salary+(salary*20/100)
if(rating=='A'):
    salary=salary+(salary*10/100)
elif(rating=='B'):
    salary=salary+(salary*5/100)
else:
    print("No extra bonus")

print("Employee salary : ",salary)
