import math
import re
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         self.p = (self.a + self.b + self.c) / 2
#         print(self.p)
#     def square(self):
#         self.s = math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
#         print(self.s)
#     def height(self):
#         self.hA = (2 * self.s) / a
#         self.hB = (2 * self.s) / b
#         self.hC = (2 * self.s) / c
#         print("Высота точки А: ", self.hA)
#         print("Высота точки B: ", self.hB)
#         print("Высота точки C: ", self.hC)
#
# coords = input("Введите координаты по маске А1:А2 B1:B2 C1:C2 - ")
# x1, y1, x2, y2, x3, y3 = list(map(int, re.split("\D", coords)))
# a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# b = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
# c = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
#
#
# triange = Triangle(a, b, c)
# triange.perimeter()
# triange.square()
# triange.height()



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium:
    def __init__(self, coords):
        self.coords = coords

    def perimeter(self):
        self.p = self.a + self.b + self.c + self.d
        return self.p
    def square(self):
        self.s = ((self.a+self.b)/2)*(math.sqrt((self.c**2)-((((self.b-self.a)**2)+(self.c**2)-(self.d**2))/(2*(self.b-self.a)))))
        return self.s
    def side_length(self):
        self.x1,  self.y1,  self.x2,  self.y2,  self.x3,  self.y3, self.x4, self.y4 = list(map(int, re.split("\D", self.coords)))
        self.c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        self.d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        self.a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        self.b = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        print("Длина сторон: " + "\nAB: ", self.a, "\nBC: ", self.c, "\nCD: ", self.d, "\nDC: ", self.b)


    def check(self):
        if self.c == self.d:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")

coords = input("Введите координаты по маске А1:А2 B1:B2 C1:C2 D1:D2 - ")

t = Trapezium(coords)
t.side_length()
print(f"Площадь равна: {t.square()}")
print(f"Периметр равен: {t.perimeter()}")
t.check()
