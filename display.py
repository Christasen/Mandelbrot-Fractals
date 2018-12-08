# Guangyu Yan yanxx630
# Defined a Display class

from complex import Complex
from mandelbrot import Mandelbrot
import turtle

class Display:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.screen = self.turtle.getscreen()
        self.widhalf = 400
        self.heihalf = 400
        self.bound = [-2, -2, 2, 2]
        self.center = [0,0]
        self.turtle.hideturtle()
        self.screen.tracer(2000,0)
        self.turtle.pensize(1)
        self.screen.screensize(400, 400)
        for i in range(-self.widhalf,self.widhalf):
            self.turtle.pu()
            self.turtle.goto(i,-self.heihalf)
            self.turtle.pd()
            for j in range(-self.heihalf,self.heihalf):
                c = Complex(i*2/self.widhalf, j*2/self.heihalf)
                M = Mandelbrot(c,50)
                color = M.get_color()
                self.turtle.pencolor(color)
                self.turtle.goto(i,j)
        self.screen.onclick(self.click)
        self.screen.listen()
        self.screen.mainloop() 
        print("here");

    def click(self,x,y):
        if x > -self.widhalf and x < self.widhalf and y > -self.heihalf and y < self.heihalf \
        and self.turtle.position != (self.widhalf, self.heihalf):
            self.zoom(x,y)
            self.draw()

    def zoom(self,x,y):
        mwid = self.bound[2] - self.bound[0]
        mhei = self.bound[3] - self.bound[1]
        mx = x*mwid/(self.widhalf*2) + self.center[0]
        my = y*mhei/(self.heihalf*2) + self.center[1]
        self.center = [mx, my]
        self.bound = [mx-mwid/4, my-mwid/4, mx+mwid/4, my+mhei/4]

    def draw(self):
        self.turtle.clear()
        for i in range(-self.widhalf,self.widhalf):
            self.turtle.pu()
            self.turtle.goto(i,-self.heihalf)
            self.turtle.pd()
            for j in range(-self.heihalf,self.heihalf):
                mwidhalf = (self.bound[2] - self.bound[0])/2
                mheihalf = (self.bound[3] - self.bound[1])/2
                a = i*mwidhalf/self.widhalf + self.center[0]
                b = j*mheihalf/self.heihalf + self.center[1]
                c = Complex(a, b)
                M = Mandelbrot(c,50)
                color = M.get_color()
                self.turtle.pencolor(color)
                self.turtle.goto(i,j)

def main():
    Display()

if __name__=="__main__":
    main()
