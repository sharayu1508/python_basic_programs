name=input("Enter any sentance : ")
count=1

for ch in name:
    if(ch!=" "):
        continue
    else:
        count+=1

print(f"Number of words in the sentance are : {count}")
