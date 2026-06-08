# 9.Decimal to Binary Conversion
# Convert decimal number to binary using loop

num=int(input("Enter any decimal number : "))
binary=""
while(num>0):
    rem=num%2
    binary=str(rem)+binary
    num=num//2

print("Binary : ",binary)
