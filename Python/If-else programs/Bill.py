# 3. Electricity Bill Generator 
# Create a program to calculate electricity bill based on units: 
# Units Rate 
# 0–100 ₹5/unit 
# 101–20
# 0 
# ₹7/unit 
# 201+ ₹10/unit 
# Add 18% GST at the end.
unit=int(input("Enter a Unit : "))

if(unit>0 and unit<=100):
    unit=unit*5
elif(unit>=101 and unit<=200):
    unit=500+(unit-100)*7
elif(unit>=201):
    unit=500+700+(unit-200)*10

bill=unit*1.18
print("Electricity bill : ",bill)
