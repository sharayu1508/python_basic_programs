from abc import ABC , abstractmethod

class A(ABC):

    def xyz(self):
        print("hello xyz")

    @abstractmethod
    def show(self):
        pass

class B(A):
    pass
    def show(self):
        print("hii i am fom show ")


obj=B()
obj.xyz()
obj.show()
