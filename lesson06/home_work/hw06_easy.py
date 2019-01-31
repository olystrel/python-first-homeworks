# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle():
    def __init__(self,ax,ay,bx,by,cx,cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.ab = math.sqrt((ax-bx)**2 + (ay-by)**2)
        self.bc = math.sqrt((bx-cx)**2 + (by-cy)**2)
        self.ca = math.sqrt((ax-cx)**2 + (ay-cy)**2)

    def perimeter(self):
        self.perimeter = self.ab + self.bc + self.ca
        return self.perimeter

    def square(self):
        self.perimeter /= 2
        self.square = math.sqrt(self.perimeter*(self.perimeter-self.ab)*(self.perimeter-self.bc)*(self.perimeter-self.ca))
        return self.square

    def height(self):
        self.height = self.square * 2 / self.ab
        return self.height

my_triangle = Triangle(0,0,3,0,0,4)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze():
    def __init__(self,ax,ay,bx,by,cx,cy,dx,dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy
        self.ab = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
        self.bc = math.sqrt((bx - cx) ** 2 + (by - cy) ** 2)
        self.cd = math.sqrt((dx - cx) ** 2 + (dy - cy) ** 2)
        self.da = math.sqrt((ax - dx) ** 2 + (ay - dy) ** 2)
        self.ah = (self.da - self.bc) / 2
        self.height = math.sqrt(self.ab ** 2 - self.ah ** 2)

    def check(self):
        if self.ab == self.cd:
            return "Трапеция равнобочная"
        else:
            return "Трапеция не равнобочная"

    def perimeter(self):
        self.perimeter = self.ab + self.bc + self.cd + self.da
        return self.perimeter

    def square(self):
        self.square = (self.bc + self.da) * self.height / 2
        return self.square

my_trapeze = Trapeze(0,0,3,4,9,4,12,0)

print("AB = ",my_trapeze.ab)
print("BC = ",my_trapeze.bc)
print("CD = ",my_trapeze.cd)
print("DA = ",my_trapeze.da)
print(my_trapeze.check())
print("Периметр трапеции равен ",my_trapeze.perimeter())
print("Площадь трапеции равна ",my_trapeze.square())
