class Point :
    def __init__(self,xx,yy):
        self.xx = xx
        self.yy = yy
    def draw(self):
        print(f'draw from point x::{self.xx} to point y::{self.yy}')


    def move(self,newyy):
        print(f'move cursor from point x::{self.xx} to point y::{self.yy} :: Newyy :: {newyy}')

xpoint = input("Please enter value of x :: ")
ypoint = input("Please enter value of y :: ")
pt = Point(xpoint,ypoint)
print(pt.xx)
print(pt.yy)
pt.draw()
pt.yy = 11
pt.move(23)