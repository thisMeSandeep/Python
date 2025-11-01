x = "Global X"  # Global namespace

def outer():
    y = "Enclosing Y"  # Enclosing namespace

    def inner():
        z = "Local Z"  # Local namespace
        print(x)  # from Global
        print(y)  # from Enclosing
        print(z)  # Local

    inner()

outer()


print(globals())  # global namespace
print(locals())   # if inside function → local namespace
