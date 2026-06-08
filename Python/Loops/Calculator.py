# 10.Menu Driven Calculator 

print("--- Calculator --- ")
print("*** MENU *** ")

while True:
    print("\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit ")
    ch=int(input(("Enter your choice : ")))

    match ch:
            case 1:
             num1=int(input("Enter a 1st number : "))
             num2=int(input("Enter a 2nd number : "))
             print("Addition : ",num1 + num2 )

            case 2:
             num1=int(input("Enter a 1st number : "))
             num2=int(input("Enter a 2nd number : "))
             print("Subtracton : ",num1 - num2 )

            case 3:
             num1=int(input("Enter a 1st number : "))
             num2=int(input("Enter a 2nd number : "))
             print("Multiplication : ",num1 * num2 )
    
            case 4:
             num1=int(input("Enter a 1st number : "))
             num2=int(input("Enter a 2nd number : "))
             print("Division : ",num1 / num2 )
    
            case 5:
             exit()

            case _:
             print("Invalid Choice!!!")
    
