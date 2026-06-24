from Animal import Animal
class Dog(Animal):
    pass

    def __init__(self, name,weight,color):
        self.color=color
        super().__init__(name,weight)

    def abc(self):
        print("Hello i am from child class ")


    def dog_details(self):
        super().greet()
        print(f"{self.name},{self.color}")




obj=Dog("lab","7kg","black")
# print(obj.type)
# print(obj.name)
# print(obj.weight)
# print(obj.color)
# obj.xyz()
# obj.abc()
obj.dog_details()
