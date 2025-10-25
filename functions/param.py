""" Argumnet type - args """
# def func(*values):
#     print(values)
#     print(type(values))



# func(1,2,3,"Apple",True)


""" Argument type kwargs """
def fun(**kvp):
    print(kvp)
    print(type(kvp))


fun(Name="Sandeep" , age=23 , isMarried=False)