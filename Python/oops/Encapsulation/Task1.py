import random
import time


class insta:
    def __init__(self,name,username,password):
        self.name=name
        self.username=username
        self.__password=password

   

    def login(self,username,password):
        if self.username==username and self.__password==password:
            print("Login Successfull...")
            self.generate_otp()

        else:
            print("Inavlid Credential!!!")

    def generate_otp(self):
           self.__otp=random.randint(100000,999999)
           self.otp_sent_time=time.time()
           print("OTP Sent to your registered mobile number ")
           print(self.__otp)
           u_otp=int(input("Enter your OTP : "))
           self.current_time=time.time()
           self.verify_otp(u_otp)


    def verify_otp(self,u_otp):  

        if self.current_time - self.otp_sent_time <=30:
            if self.__otp==u_otp:
                print("OTP Matched...")
            else:
                print("Invalid OTP!!!")  
        else:
            print("OTP Expired!!!")

obj=insta("sharayu","sharayu@15",150823)
user=input("Enter your username : ")
pwd=int(input("Enter your password : "))
obj.login(user,pwd)
