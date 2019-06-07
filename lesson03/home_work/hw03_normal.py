import math
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# def fibonacci(n, m, f):
#     a = 0
#     b = 1
#     x = list()
#     if f == 0:
#         return 0
#     elif f < 3:
#         return 1
#     else:
#         for i in range(f):
#             a, b = b, a + b
#             x.append(a)
#     return x[n:m]
# f = int(input("Введите ряд Фибоначчи"))
# n = int(input("Начальная координата для вывода числа Фибоначчи"))
# m = int(input("Конечная координата для числа Фибоначчи"))
#
#
# print(fibonacci(n, m, f))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# def sort_to_max(origin_list):
#     for i in range(len(origin_list) - 1):
#         for j in range(len(origin_list) - i - 1):
#             if origin_list[j] > origin_list[j + 1]:
#                 origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
#
#     return origin_list
#
# print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(func, num):
    my_list = []
    for i in num:
        if i == func:
           my_list.append(i)
    print(my_list)

n = int(input("Enter"))
a = [1,5,8,11,22,2,4,97,5,1,2,8,8,8,11,22,22]
a = my_filter(n, a)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# A1 = (int(input("введите х для первой вершины")), int(input("введите y для первой вершины")))
# A2 = (int(input("введите х для второй вершины")), int(input("введите y для второй вершины")))
# A3 = (int(input("введите х для третьей вершины")), int(input("введите y для третьей вершины")))
# A4 = (int(input("введите х для четвертой вершины")), int(input("введите y для четвертой вершины")))
#
# def parallelogramm(a, b, c, d):
#     ab = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
#     dc = math.sqrt((c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2)
#     ad = math.sqrt((d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2)
#     bc = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
#     print(f"{ab} {dc} {ad} {bc}")
#     if ab == dc and bc == ad:
#         print("Точки являются вершинами параллелограмма")
#     else:
#         print("Точки не являются вершинами")
#
#
# parallelogramm(A1, A2, A3, A4)