class Account:
    def __init__(self,bal):
        self.__bal=bal

    def get_bal(self):
        return self.__bal
    
    def set_bal(self,amt):
        self.__bal=amt
        print("Bal Updated")

    def __private_method(self):
        return "Hello I Am Private !"
    
    def access_pm(self):
        return self.__private_method()
    
    def call__deposit(self,amt):
        print("Balance : ",self.__bal)
        if amt>0:
            self.__bal+=amt
            print("Amount Deposited")
            print("New Balance after deposit : ",self.__bal)


    def call__withdraw(self,amt):
        if amt<self.__bal:
            print("Balance : ",self.__bal)
            self.__bal-=amt
            print("Debited Amount : ",amt)
            print("Remaining Balance : ",self.__bal)
        else:
            print("Insufficient balance!!!")





obj=Account(500)
# print(obj.get_bal())
# obj.set_bal(500)
# print(obj.get_bal())
# print(obj.access_pm())
# obj.deposit(500)
obj.call__withdraw(100)
obj.call__deposit(500)