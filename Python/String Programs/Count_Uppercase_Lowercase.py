name=input("Enter any string : ")

lo=0
up=0

for ch in name:
    a=ord(ch)
    if(a>=97 and a<=122):
        lo+=1
    if(a>=65 and a<=90):
        up+=1

print("Count of lowercase lettters : ",lo)
print("Count of uppercase letters : ",up)
