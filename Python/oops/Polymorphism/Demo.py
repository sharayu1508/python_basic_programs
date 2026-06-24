class Payment:

    def Pay(self):
        pass
    print(" Payment process started....")

class UPI(Payment):
    def Pay(self):
        return " \n Payment done by UPI "
    
class GPay(Payment):
    def Pay(self):
        return " Payment done by GPay "
    
class Payment_Module:
    def Payment_Process(self,obj):
        print(obj.Pay())

print("-------------------------Payment----------------")
print("\n 1. UPI \n 2. GPay \n 3. Card \n 4. Exit")
choice = int(input("enter your choice: "))

match choice:

    case 1:
        obj=UPI()
        
    case 2:
        obj=GPay()

    case 3:
        pass

    case 4:
        exit()

    case _:
        print(" Invalid choice !!!")


p=Payment_Module()
p.Payment_Process(obj)


#Multiple object
obj=[UPI(),GPay()]

print("-----------------------------------------------------------------------")
for i in obj:
    print(i.Pay())