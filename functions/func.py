"""global and nonlocal variable"""

# def outer():
#     fruit="Apple"
#     def inner():
#         nonlocal fruit
#         fruit="Banana"
#         print(fruit)
#     inner()
#     print(fruit)    

# outer()    


fruit="Apple"


def outer():
    fruit="Oranges"
    print(fruit)
    def inner():
        global fruit
        fruit="Banana"
        print(fruit)
    inner()


outer()
print("Outer var:",fruit)