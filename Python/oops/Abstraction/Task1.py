from abc import ABC,abstractmethod

class Login(ABC):
    @abstractmethod 
    def authenticate(self):
        pass

class User(Login):

    def __init__(self):
      self.username="sharayu"
      self.password=150823

    def authenticate(self):
        username=input("Enter your username : ")
        password=int(input("Enter your password : "))

        if username==self.username and password==self.password:
            print("Login Successful...")
        else:
            print("Invalid Credential!!!")

class Admin(Login):

    def __init__(self):
        self.email="shourya15@gmail.com"
        self.password=150823

    def authenticate(self):
        email=input("Enter your email : ")
        password=int(input("Enter your password : "))

        if email==self.email and password==self.password:
            print("Admin Login Successful...")
        else:
            print("Invalid Credential!!!")

obj1=User()
obj1.authenticate()
obj2=Admin()
obj2.authenticate()
