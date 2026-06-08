# 13.Online Exam Result System

n = int(input("Enter number of students : "))
for i in range(1, n + 1):
    print(f"\nEnter marks for Student {i}")
    total = 0
    fail = False
    for j in range(1, 6):
        marks = int(input(f"Subject {j} : "))
        total += marks
        if marks < 35:
            fail = True
            
    percentage = total / 5

    print("Total :", total)
    print("Percentage :", percentage)

    if percentage >= 75:
        grade = "Distinction"

    elif percentage >= 60:
        grade = "First Class"

    elif percentage >= 50:
        grade = "Second Class"

    elif percentage >= 35:
        grade = "Pass"

    else:
        grade = "Fail"
    print("Grade :", grade)
    if fail:
        print("Result : FAIL")
    else:
        print("Result : PASS")
