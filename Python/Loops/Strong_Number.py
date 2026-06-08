# 6.Strong Number 
# Check whether number is Strong Number.

num=int(input("Enter any number : "))
print("orignal Number : ",num)
orignal=num
sum=0
while(num!=0):
    fact=1
    digit=num%10
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    num=num//10

print("Sum : ",sum)
if(orignal==sum):
    print(orignal,"is a strong number")
else:
    print(orignal,"is not a strong number")
