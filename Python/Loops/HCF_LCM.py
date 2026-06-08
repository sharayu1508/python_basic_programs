# 7.Find HCF
# and LCM Find HCF
# and LCM of two numbers using loops. 

num1=int(input("Enter any number : "))
num2=int(input("Enter any number : "))

hcf=1
for i in range(1,min(num1,num2),+1):
    if(num1%i==0 and num2%i==0):
        hcf=i

print("HCF : ",hcf)

lcm=max(num1,num2)

while True:
    if(lcm%num1==0 and lcm%num2==0):
        break
    lcm+=1

print("LCM : ",lcm)
