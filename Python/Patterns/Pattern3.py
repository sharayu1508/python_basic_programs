ch="a"
for i in range(3):
    print(" " * i ,end="")

    for j in range(3-i):
        print(ch,end="")

    ch=chr(ord(ch)+1)
    print()
