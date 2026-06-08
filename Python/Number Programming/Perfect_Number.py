num=int(input("Enter any number : "))
print("Orignal Number : ",num)
orignal=num
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+=i

if(orignal==sum):
    print(orignal,"is a Perfect Number")
else:
    print(orignal,"is not a Perfect Number")
