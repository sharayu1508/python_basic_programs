# 8.Perfect Number 
# Check whether a number is perfect or not

num=int(input("Enter any number : "))
print("Orignal Number : ",num)
orignal=num
sum=0

for i in range(1,num):
    if(num%i==0):
        sum+=i

if(sum==orignal):
    print(orignal,"is Pefect Number")
else:
    print(orignal,"is Not Perfect Number")
