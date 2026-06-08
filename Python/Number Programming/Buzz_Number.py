num=int(input("Enter any number : "))
print("Orignal Number : ",num)

if(num%7==0 or num%10==7):
    print(num,"is a Buzz Number")
else:
    print(num,"is not a Buzz Number")
