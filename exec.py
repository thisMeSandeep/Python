
try:
    a,b=[int(x) for x in input("Enter two number : ").split()]
    div=a//b
    print(div)
except Exception:
    print("divide by zero is not possible")
finally:
    print("I always execute")    