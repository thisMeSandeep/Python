"""Parent class """
class BaseUser:
    role="user"

    def __init__(self , name):
        self.name=name

    def getName(self):
        return self.name  
        

"""Child class"""
class User(BaseUser):  #extending BaseUser class , User have now constuctor and getName method of BaseUser
    def setGender(self, gender):
        self.gender=gender

    def getGender(self):
        return self.gender


user=User('Sandeep') 
print(user.getName())
user.setGender("Male")
print(user.getGender())



"""Composition way"""
# class SubUser:
#     base = BaseUser

#     def __init__(self, name):
#         self.user = self.base(name)  # object of BaseUser

#     def getName(self):
#         return self.user.getName()   # call on the object

# user=SubUser("Sandeep")

# print(user.getName())