from Bank import Bank 
class Account(Bank):

    def __init__(self,bname,ifsc,ano,name):

        self.ano=ano
        self.name=name
        super().__init__(bname,ifsc)
        
    def display_Account(self):
        acc_info=super().display_Bank()
        return f"{acc_info} \n Account Holder Name : {self.name} \n Account Number : {self.ano}"

        
    