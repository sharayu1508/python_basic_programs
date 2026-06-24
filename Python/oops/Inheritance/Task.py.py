while(True):
        print(f"*** MENU ***")
        print(f"\n1.Single Inheritance \n2.Multilevel Inheritance \n3.Multiple Inheritance \n4.Hierarchical Inheritance \n5.Hybrid Inheritance \n6.Exit ")
        print()
        print(f"--------------------------------------------------------")
        print()
        ch=int(input("Enter your choice : "))
        print()

        match ch:

            case 1:

                #Single inheritance 

                print("Single Inheritance")
                class product:
                    def __init__(self,name,price):
                        self.name=name
                        self.price=price

                    def display(self):
                        print(f"Product Name : {self.name}")
                        print(f"Product Price : {self.price}")
                        

                class Electronic_Product(product):
                    def __init__(self, name, price,warrenty):
                        super().__init__(name, price)
                        self.warrenty=warrenty

                    def display1(self):
                        super().display()
                        print(f"Warrenty : {self.warrenty}")



                pname=input("Enter the product name : ")
                p=int(input(("Enter the product price : ")))
                w=int(input(("Enter the product warrenty : ")))
                print()
                obj=Electronic_Product(pname,p,w)
                obj.display1()




            case 2 :

                #Multilevel Inheritance 

                print("Multilevel Inheritance")
                class Bank:
                    def __init__(self,bname):
                        self.bname=bname
                        print(f"Bank Name : {self.bname}")

                class Account(Bank):
                    def __init__(self, bname,name,password):
                        super().__init__(bname)
                        self.name=name
                        self.password=password

                        print(f"Customer Name : {self.name}")
                        print(f"Password : {self.password}")

                class Saving_Account(Account):
                    def __init__(self,bname,name,password,balance):
                        super().__init__(bname,name,password)
                        self.balance=balance
                        print(f"Balance : ",balance)

                b=input("Enter the Bank Name : ")
                n=input("Enter your name : ")
                p=int(input("Enter the Password : "))
                bal=int(input("Enter the balance : "))

                obj1=Saving_Account(b,n,p,bal)


            case 3:

                #Multiple Inheritance 

                print("Multiple Inheritance")
                class Wifi:
                    def connect(self):
                        print("Connected to Wifi...")

                class Bluetooth:
                    def connect(self):
                        print("Connected to Bluetooth...")

                class Smartspeaker(Wifi,Bluetooth):
                    def play_Music(self):
                        super().connect()
                        Bluetooth.connect(self)
                        print("Playing Music...")

                obj2=Smartspeaker()
                obj2.play_Music()


            case 4 :

                #Hierarchical Inheritance 

                print("Hierarchical Inheritance")
                class Person:
                    def __init__(self,name):
                        self.name=name

                class Student(Person):
                    def study(self):
                        print(f"{self.name} is studying")
                        
                class Teacher(Person):
                    def teach(self):
                        # Student.study(self)
                        print(f"{self.name} is Teaching")

                s=Student("Ram")
                t=Teacher("Sita")
                s.study()
                t.teach()




            case 5:

                #Hybrid Inheritance 

                class Device:
                    def Power_On(self):
                        print(f"Device power on...")

                class Camera(Device):
                    def Photo_Click(self):
                        print(f"Photo Clicked...")
                        self.Power_On()

                class Phone(Device):
                    def Make_Calls(self):
                        print("Calling...")

                class SmartPhone(Camera,Phone):
                    def Use_Apps(self):
                        self.Photo_Click()
                        self.Make_Calls()
                        print(f"Using Apps...")

                S=SmartPhone()
                S.Use_Apps()

            


            case 6:
                print("Thank You!!!")
                break
