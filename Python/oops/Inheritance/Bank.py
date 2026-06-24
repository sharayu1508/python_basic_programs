class Bank:

    def __init__(self,bname,ifsc):
            self.bname=bname
            self.ifsc=ifsc
    
    def display_Bank(self):
        return f"Bank Name : {self.bname} \n IFSC Code : {self.ifsc}"