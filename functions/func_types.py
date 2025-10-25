"""Different types of function """

# value=5  #global variable

""" Pure function - don't modify the global variable and return the result """
# def pure_fun(value):
#     return value+1

"""Impure function - modify the global variable and return the result """
# def impure_fun():
#     global value
#     value+=1
#     return value

# print(pure_fun(value))
# print(value)

# print(impure_fun())
# print(value)


"""Lambda function """
f= lambda x,y : x+y
print(f(5,6))