# 7. Triangle Validator 
# Input 3 angles. 
# Check: 
# ● Whether triangle is valid 
# ● Then print: 
# ○ Equilateral 
# ○ Isosceles 
# ○ Scalene

print("Enter the angles of tringle ")
a1=int(input("Enter the angle1 : "))
a2=int(input("Enter the angle2 : "))
a3=int(input("Enter the angle3 : "))

if( a1+a2+a3==180 ):

    if(a1==a2==a3):
        print("Equlateral Triangle ")

    elif(a1==a2 or a2==a3 or a1==a3):
        print("Isosceles Triangle ")

    elif(a1!=a2 and a2!=a3 and a1!=a3):
         print("scelene Triangle ")

else:
    print("Sum of angles should be 180 ")
