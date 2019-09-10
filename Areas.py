import math

class figura:
    def area(self, dist):
        pass
    def perimetro(self,dist):
        pass

class circulo(figura):
    def area(self, dist):
        return 2*3.1415*dist**2
    def perimetro(self, dist):
        return 2*3.1415*dist

class circulo(figura):
    def area(self, dist):
        return math.cos(dist)*math.sin(dist)

    def perimetro(self, dist):
        return (math.cos(dist) * 2) + (math.sin(dist)*2)

f = circulo()

print(f.area(5))