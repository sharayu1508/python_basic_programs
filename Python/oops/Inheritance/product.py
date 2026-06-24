class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    
    def show_product(self):
        return f"Product Name : {self.name} \t Price : {self.price}"
        