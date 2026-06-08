# 6. Login Authentication System 
# Create a simple login system. 
# Correct credentials: 
# ● Username: admin 
# ● Password: 1234 
# Use nested if-else.

user=input("Enter your username : ")
password=input("Enter  the password : ")

if(user=="admin"):
    if(password=='1234'):
        print("Login Successful")
    else:
        print("Wrong password")
else:
    print("Invalid username!!!")
