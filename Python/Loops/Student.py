# 11.Student Result System 

total = 0

for i in range(1, 6):
    marks = int(input(f"Enter marks of Student {i} : "))
    total += marks

percentage = total / 5

print("Total Marks :", total)
print("Percentage :", percentage)

if percentage >= 75:
    print("Grade : Distinction")

elif percentage >= 60:
    print("Grade : First Class")

elif percentage >= 50:
    print("Grade : Second Class")

elif percentage >= 35:
    print("Grade : Pass")

else:
    print("Grade : Fail")
