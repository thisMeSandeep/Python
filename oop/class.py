"""Simple class"""

class User(object): #object is optional 
    role="user"  #class variable 
    #constructor
    def __init__(self, name):
        self.name=name

    def getName(self):
        return self.name
    
    #setter 
    def setAge(self,age):
        self.age=age
    
    #getter
    def getAge(self):
        return self.age    


# Create an object of User class
user1=User('Sandeep'); #pass the name to constructor

print(user1.role)
print(user1.getName())
user1.setAge(23)  #calling the setter
print(user1.getAge()) #calling the getter