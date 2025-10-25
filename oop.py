class Square:
    def __init__(self,x):
        self.x=x


    def area(self):
        print(f'area of the square is {self.x*self.x}')



class Rect(Square):
    def __init__(self , x , y):
        super().__init__(x) # calling the constructor of super class
        self.y=y

    def area(self):
        super().area()
        print(f"area of rectangle is {self.x*self.y}")


r=Rect(5,4)

r.area()
