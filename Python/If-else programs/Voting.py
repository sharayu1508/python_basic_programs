# 10. Online Voting System 
# Input: 
# ● Age 
# ● Citizenship (Indian or not) 
# ● Criminal record (Yes/No) 
# Eligible only if: 
# ● Age ≥ 18 
# ● Indian citizen 
# ● No criminal record

age=int(input("Enter your age : "))
citizenship=input("Enter your citizenship : ").lower()
criminal_record=input("Criminal Record (Yes/No) : ").lower()

if(age>=18 and citizenship=="indian" and criminal_record=="no"):
           print("You are eligible for voting ")
 
else:
    print("You are not eligible for voting ")
