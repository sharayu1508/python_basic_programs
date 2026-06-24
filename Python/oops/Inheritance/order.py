from payment import payment
from product import product

class order(product,payment):
    def bill(self):
        
        qty=int(input("Enter the quantity : "))
        total=self.price*qty
        print(self.show_product())
        print("Total Price : ",total)
        print(self.amount1())


obj=order("car",5000)
obj.bill()
