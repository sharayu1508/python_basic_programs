# 12. Income Tax Calculator 
# Calculate tax based on income slabs: 
# Income 
# Tax 
# Up to ₹2.5L 0% 
# ₹2.5L–₹5L 
# ₹5L–₹10L 
# 5% 
# 20% 
# Above ₹10L 30% 
# Add 4% cess.

income=int(input("Enter your income : "))
tax=0
if(income<=250000):
    print("No tax ")
elif(income>250000 and income<=500000):
    tax=income*5/100
    income+=tax
elif(income>500000 and income<=1000000):
    tax=income*20/100
    income+=tax
elif(income>1000000):
    tax=income*30/100
    income+=tax

cess=tax*4/100
total_tax=tax+cess
print("tax : ",total_tax)
print("Income including all taxes : ",(income+cess))
