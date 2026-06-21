# try:
#         num1=int(input("Enter number 1 : "))
#         num2=int(input("Enter number 2 : "))
#         def add():
#             print(f"Addition is {num1+num2}")

# except Exception as e:
#     print(e)

# else:
#     add()



try:
    num1=int(input("Enter number 1 : "))
    num2=int(input("Enter number 2 : "))
    def add(num1,num2):
         return num1+num2
    print(f"Addition is {add(num1,num2)}")

except ValueError:
     print("Value Error")
