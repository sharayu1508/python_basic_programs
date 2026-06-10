name=input("Enter any string : ")

for ch in name:
    a=ord(ch)
    if(a>=65 and a<=90):
        lower=chr(a+32)
        print(lower,end="")
    else:
        print(ch,end="")
