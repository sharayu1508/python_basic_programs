num=(int(input("Enter any Number : ")))
orignal=num
rev=0
while(num!=0):
    digit=num%10
    rev=rev*10+digit
    num=num//10

if(orignal==rev):
    print(orignal,"is Palindrome number")
else:
    print(orignal,"is not Palindrome number")
