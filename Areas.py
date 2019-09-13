import math
import tkinter as tk

class Shape:
    def __init__ (self, x1, y1, x2, y2):
        pass

    def getarea(self, x1, y1, x2, y2):
        pass

    def getperimeter(self, x1, y1, x2, y2):
        pass

class Circle(Shape):
    def __init__ (self, x1, y1, x2, y2):
        self.r = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def getarea(self):
        return math.pi*(self.r**2)

    def getperimeter(self):
        return 2*math.pi*self.r

class Square(Shape):
    def __init__ (self, x1, y1, x2, y2):
        self.l1 = abs(x2 - x1) 
        self.l2 = abs(y2 - y1)

    def getarea(self):
        return abs(self.l1 * self.l2)

    def getperimeter(self):
        return abs((self.l1 * 2) + (self.l2 * 2))

class Triangle(Shape):
    def __init__ (self, x1, y1, x2, y2):
        self.l1 = abs(x2 - x1) 
        self.l2 = abs(y2 - y1)

    def getarea(self):
        return abs(self.l1 * self.l2)/2
    
    def getperimeter(self):
        return abs(self.l1 + self.l2 + math.sqrt(self.l1**2 + self.l2**2))

def calculate(f):
    print("   area: "+str(f.getarea()))
    print("   perimetro: "+str(f.getperimeter()))
    print()

f = Circle(0,0,1,0)
calculate(f)
f = Square(0,0,1,1)
calculate(f)
f = Triangle(0,0,1,1)
calculate(f)


frame = tk.Tk()
frame.title("Areas y Perimetros")
frame.geometry('500x500')
frame.configure(background='black')
frame.mainloop()