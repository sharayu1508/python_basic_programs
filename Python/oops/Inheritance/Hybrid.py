class A:
    def xyz(self):
        print("From xyz A ")

    def __init__(self,name):
            print("A Constructor")
            self.name=name
            print("Name : ",self.name)

class B(A):
    def abc(self):
        print("From abc B ")
    
    def __init__(self,age,name):
            print("B Constructor")
            self.age=age
            print("Age : ",self.age)
            # A.__init__(self)
            super().__init__(name)

class C(A):
    def pqr(self):
        print("From pqr C ")

    def __init__(self,rollno,age):
            print("C Constructor")
            self.rollno=rollno
            print("Roll Number : ",self.rollno)
            # A.__init__(self)
            super().__init__(age)

class D(B,C):
    def mno(self):
        print("From mno D ") 

    def __init__(self,branch,rollno,age):
            print("D Constructor")
            self.branch=branch
            print("Department : ",self.branch)
            # B.__init__(self)
            # C.__init__(self)
            super().__init__(branch,rollno,age)


obj=D("Sharayu",17,232,"Computer")
# obj.xyz()
# obj.abc()
# obj.pqr()
# obj.mno()
