name=input("Enter any string : ")
ch=input("Enter any charecter from the string : ")

count=0
for c in name:
    if(c==ch):
        count+=1
    else:
        continue

print(f"Occurance of charecter {ch} is : ",count)
