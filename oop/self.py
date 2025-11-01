"""self argument in python"""

class Fruit:
    def __init__(self,name,quantity=10 ):  #__init__ is initialize 
        self.name=name
        self.quantity=quantity

    #method
    def describe(self):
        print(f"name of the fruit is {self.name} and I have {self.quantity} {self.name}")



mango=Fruit("mango")

mango.describe() #calling method using object
# Fruit.describe() won't work
Fruit.describe(mango) #we will need to pass an instance as self reference to an object(instance)
