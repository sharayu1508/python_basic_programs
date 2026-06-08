# 2.Reverse Table 
# Print multiplication table in reverse order.

num=int(input("Enter any number : "))

for i in range(10,0,-1):
    print(num," * ",i," = ",num*i)
