# 1.Factorial of Number 
# Calculate factorial using for loop.

num=int(input("Enter any number : "))
fact=1

for i in range(1,num+1):
    fact*=i

print("Factorial of a ",num,"is : ",fact)
