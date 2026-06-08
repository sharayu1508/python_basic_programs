num=int(input("Enter any  number : "))
print("Orignal Number : ",num)
orignal=num
while(num!=1 and num!=4):
    sum=0
    while(num!=0):
        digit=num%10
        sum=sum+(digit*digit)
        num//=10

    num=sum

if(num==1):
    print(orignal,"is  Happy")
else:
    print(orignal,"is Sad")
