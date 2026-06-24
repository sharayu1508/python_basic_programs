class Animal:
    type="animaltype"

    def __init__(self):
        print("Default animal con ")

    def __init__(self, name,weight):
        self.name=name
        self.weight=weight

    def xyz(self):
        print("Hello i am from parent class ")


    def greet(self):
        print("Hello i am Animal ")