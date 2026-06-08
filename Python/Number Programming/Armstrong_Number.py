num=int(input("Enter any number :"))
orignal=num
sum=0 
temp=len(str(orignal))


while(num!=0):
    digit=num%10
    number=digit**temp
    sum=sum+number
    num=num//10

if(orignal==sum):
    print(orignal,"is Armstrong Number")
else:
    print(orignal,"is Not Armstrong Number")