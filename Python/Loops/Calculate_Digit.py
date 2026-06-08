# 3.Count Digits 
# Input a number and count total digits using loop.

num=int(input("Enter any number : "))
print("Number = ",num)
print("Digits are : ")
while(num!=0):
    digit=num%10
    print(digit)
    num=num//10
