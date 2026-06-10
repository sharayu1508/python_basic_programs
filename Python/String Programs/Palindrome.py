name=input("Enter any string : ")

rev=""
orignal=name

for ch in name:
    rev=ch+rev

if rev==orignal:
    print(orignal,"is palindrome")
else:
    print(orignal,"is not palindrome")
