class p1:
    def xyz(self):
        print("From p1 xyz")

    def show(self):
        print("Show from p1 ")

    def __init__(self,name):
        self.name=name
        print("p1 consructor ")
        print(self.name)

class p2:
    def abc(self):
        print("From p2 abc")

    def show(self):
        print("Show from p2")

    def call_p2_show(self):
        return p2.show(self)
    
    def __init__(self,age):
        self.age=age
        print("p2 constructor ")
        print(self.age)

class c(p1,p2):
    def pqr(self):
        print("I am from child pqr ")


    def __init__(self,name,age):
        print("C constructor")
        p1.__init__(self,name)
        p2.__init__(self,age)

obj=c("Sharayu",17)
# obj.xyz()
# obj.abc()
# obj.pqr()
# obj.show()
# obj.call_p2_show()
