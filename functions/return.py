""" return nothing - implicit return- None"""
# def fun():
#     print("Hello")

# print(fun())      # None


"""Return a single value"""
# def fun():
#     return "Hello"

# print(fun())

"""Return early"""

# def fun(age):
#     if age<18:
#         return "You are not allowed"
#     return "You are allowed"

# print(fun(15))    


"""Return multiple values"""
def fun():
    return "Hello" , "Sandeep"

#unpacking
greet , name = fun()
print(greet)
print(name)




