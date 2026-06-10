name=input("Enter any string : ")

for  ch in name:
    a=ord(ch)
    if(a>=97 and a<=122):
        upper=chr(a-32)
        print(upper,end="")
    else:
        print(ch,end="")
