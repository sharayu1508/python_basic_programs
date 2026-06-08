# 15. Bank Loan Eligibility System 

salary = float(input("Enter Salary : "))
cibil = int(input("Enter CIBIL Score : "))
loan = float(input("Enter Existing Loan Amount : "))
age = int(input("Enter Age : "))

if salary > 25000 and cibil > 750 and loan < 500000 and 21 <= age <= 60:

    print("Loan Status : Eligible")

    if salary >= 100000 and cibil >= 800:
        print("Premium Customer Loan Offer")

else:
    print("Loan Status : Not Eligible")
