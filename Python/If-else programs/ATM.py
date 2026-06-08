# 5. ATM Withdrawal System 
# Input: 
# ● Account balance 
# ● Withdrawal amount 
# Conditions: 
# ● Minimum balance should remain ₹1000 
# ● Withdrawal should be multiple of 100 
# ● Print success/failure message 
balance=int(input("Enter your account balance : "))
withdraw=int(input("Enter the withdraw amount "))

if(withdraw%100==0):
    if(balance-withdraw >=1000):
        print("Success")
    else:
        print("Failure: minimum balnce should remain ₹1000")
else:
    print("Failure: withdrawal amount should be the multiple of 100")
