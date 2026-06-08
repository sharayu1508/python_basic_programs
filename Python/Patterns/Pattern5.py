n=3
# for upper half
for i in range(1,n+1):
    num=2*i-1  #generates odd numbers

    print(" " * (n-i),end="") #Create the left spaces

    for j in range(num):     # prints the number num exactly num times 
        print(num,end="")
    print()

# for lower half
for i in range(n-1,0,-1):             #prints the pattern in reverse order to complete the diamond 
    num=2*i-1
    print(" " * (n-i),end="")

    for j in range(num):
        print(num,end="")
    print()
