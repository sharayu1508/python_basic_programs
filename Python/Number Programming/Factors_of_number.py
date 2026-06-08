num=int(input("Enter any number : "))
print("Factors of : ",num)
for i in range(1,num+1):
    if(num%i==0):
        print(i)
