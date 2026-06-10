name=input("Enter any string : ")

v=0
c=0
for ch in name:
    
    if('a'<=ch <='z')or('A'<=ch <='Z'):
        if(ch=='a' or ch=='e' or ch=='i'or ch=='o' or ch=='u'or ch=='A' or ch=='E'or ch=='I' or ch=='O'or ch=='U'):
          v+=1
        else:
            c+=1

print("Number of vowels : ",v)
print("Number of consonants : ",c)
