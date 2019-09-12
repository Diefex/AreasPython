import math
import tkinter as tk

class figura:
    def area(self, x1, y1, x2, y2):
        pass
    def perimetro(self, x1, y1, x2, y2):
        pass

class circulo(figura):
    def __init__ (self, x1, y1, x2, y2):
        self.r = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def area(self):
        return math.pi*(self.r**2)
    def perimetro(self):
        return 2*math.pi*self.r

class cuadrado(figura):
    
    def area(self, x1, y1, x2, y2):
        l1 = abs(x2 - x1)
        l2 = abs(y2 - y1)
        return abs(l1 * l2)

    def perimetro(self, x1, y1, x2, y2):
        l1 = abs(x2 - x1)
        l2 = abs(y2 - y1)
        return abs((l1 * 2) + (l2 * 2))

class triangulo(figura):
    def area(self, x1, y1, x2, y2):
        l1 = abs(x2 - x1)
        l2 = abs(y2 - y1)
        return abs(l1 * l2)/2
    
    def perimetro(self, x1, y1, x2, y2):
        l1 = abs(x2 - x1)
        l2 = abs(y2 - y1)
        return abs(l1 + l2 + math.sqrt((x2-x1)**2 + (y2-y1)**2))

dist = 2*math.sqrt(2)
print(dist)
f = circulo(0,0,1,0)

print("Circulo")
print("   area: "+str(f.area()))
print("   perimetro: "+str(f.perimetro()))
print()

f = cuadrado()

print("Cuadrado")
print("   area: "+str(f.area(0,0,1,1)))
print("   perimetro: "+str(f.perimetro(0,0,1,1)))
print()

f = triangulo()

print("triangulo")
print("   area: "+str(f.area(0,0,1,1)))
print("   perimetro: "+str(f.perimetro(0,0,1,1)))
print()

#frame = tk.Tk()
#frame.title("ventana")
#frame.geometry('500x500')
#frame.configure(background='black')
#frame.mainloop()