# 4.Sum of Digits 
# Find sum of digits of a number. 

num=int(input("Enter any number : "))
sum=0
while(num!=0):
    digit=num%10
    sum+=digit
    num=num//10

print("Sum of digits : ",sum)
