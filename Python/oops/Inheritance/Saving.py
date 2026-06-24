from Bank import Bank 
from Account import Account 
class Saving(Account):

    def __init__(self,bal,fd,bname, ifsc, ano, name,):

        self.bal=bal
        self.fd=fd
        super().__init__(bname, ifsc, ano, name)

    def display_Saving(self):
      saving_info=super().display_Account()
      return f" {saving_info} \n Balance : {self.bal} \n Fixed Deposit : {self.fd} "
    

    def deposit_money(self):
       dep=int(input("Enter amount to be deposit : "))
       self.bal=self.bal+dep
       print("New Balance : ",self.bal)

    
    def withdraw_money(self):
       wit=int(input("Enter the amount to be withdraw : "))
       if(self.bal<2500):
          print("Insufficient Balance!!!")
       else:
          self.bal=self.bal-wit
          print("Withdraw Successful!!!")
          print("New Balance : ",self.bal)


    def F_D(self,rate):
       maturity_amount=self.fd + (self.fd*rate/100)
       return f"Fixed Deposit Amount : {self.fd} \n Maturity Amount : {maturity_amount}"
       

n=input("Enter your name : ")
ac=int(input("Enter your account number : "))
bn=input("Enter bank name : ")
i=int(input("Enter ifsc code : "))
b=int(input("Enter your account balance : "))
fd=int(input("Enter fixed deposit : "))


S=Saving(b,fd,bn,i,ac,n)

print("*** MENU **** ")
print("\n1. Account Details \n 2. Deposit Money \n 3. Withdraw Monney \n 4. Fixed Deposit ")
ch=int(input("Enter your choice : "))

match ch:
   case 1:
      print(S.display_Saving())

   case 2:
      print(S.deposit_money())

   case 3: 
      print(S.withdraw_money())

   case 4:
      print("Select the duration of Fixed Deposit (FD) ")
      month=int(input(("select 3/6/9 months :  ")))
      if(month==3):
         rate=5
      elif(month==6):
         rate=7
      elif(month==9):
         rate=9
      else:
         print("Invalid Duration!!!")

      print(S.F_D(rate))
