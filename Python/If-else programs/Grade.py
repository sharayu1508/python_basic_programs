# 4. Grade System 
# Input marks of 5 subjects and calculate percentage. 

C=int(input("Enter your marks of C: "))
Java=int(input("Enter your marks of Java : "))
Python=int(input("Enter your marksof Python  : "))
HTML=int(input("Enter your marks of HTML : "))
JS=int(input("Enter your marks of JS : "))

marks=C+Java+Python+HTML+JS
percentage=marks/5
print("Percentage : ",percentage)

if(percentage>=90):
    print("A Grade ")
    print("Distinction")

elif(percentage>=75 and percentage<90):
    print("B Grade ")
    print("Pass")

elif(percentage>=50 and percentage<75):
    print("C Grade ")
    print("Pass")
elif(percentage<50):
    print("Fail!!! ")
