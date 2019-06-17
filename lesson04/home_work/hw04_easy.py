# Все задачи текущего блока решите с помощью генераторов списков!
import random
# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


number_list = [random.randint(0, 100) for _ in range(10)]
number_list_square = []
print(number_list)
for i in number_list:
    i = i ** 2
    number_list_square.append(i)

print(number_list_square)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

first_list = ["яблоко", "бутерброд", "киви", "арбуз", "ананас"]
second_list = ["яблоко", "банан", "киви", "арбуз", "грейпфрут", "киви"]
sorted_list = [x for x in first_list if x in second_list]

print(sorted_list)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

number_list = [random.randint(-100, 100) for _ in range(10)]
sorted_list = []
for i in number_list:
    if i > 0 and i % 3 == 0 and not i % 4 == 0:
        sorted_list.append(i)

print(f"Дан список: {number_list}")
print(f"Сортирован по условиям: {sorted_list}")


