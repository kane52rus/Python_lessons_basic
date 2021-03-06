import random
import math
__author__ = 'Табункин Андрей Алексеевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
print("Первое задание\n")
x = random.randrange(10000, 100000)
print("Случайное число равно ", x)
y = 0
for i in str(x):
    i = int(i)
    if i > y:
        y = i
print("Наибольшая цифра в числе ", x, " это: ", y)



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
print("\nВторое задание\n")
a = input("Enter first number")
b = input("Enter second number")
print("Первая переменная равна ", a, ", а вторая переменная равна ", b)
a, b = b, a
print("\nПосле смены мест:\nПервая переменная равна ", a, ", а вторая переменная равна ", b)



# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("\nТретье задание\n")
print("Введите коэффициенты для квадратного уравнения вида ax^2 + bx + c = 0")
a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))
d = math.sqrt(b ** 2 - 4 * (a * c))
x1 = ((-b + d) / (2 * a))
x2 = ((-b - d) / (2 * a))

print("х1 равен ", x1, ", х2 равен ", x2)
