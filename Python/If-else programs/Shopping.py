# 9. E-Commerce Discount System 
# Create a shopping bill program. 
# Conditions: 
# ● Above ₹5000 → 20% discount 
# ● Above ₹2000 → 10% discount 
# ● VIP customer → extra 5% 
# Add GST after discount.


bill=int(input("Enter your shopping bill : "))
customer=input("Enter type of customer : ").upper()

discunt=0
if(bill>5000):
    discount=bill*20/100
    bill=bill-discount
elif(bill>2000):
    discount=bill*10/100
    bill=bill-discount

if(customer=="VIP"):
    discount=bill*5/100
    bill=bill-discount

GST=bill*18/100
bill+=GST
print("Total shopping bill including gst is : ",bill)
