from fractions import Fraction
# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
def classic_float(n):
    n = n.split()
    z = Fraction(n[0])
    x = Fraction(n[2])
    operator = n[1]
    if operator == '+':
        fr_sum = x + z
        if fr_sum > 1:
            num = int(Fraction(fr_sum).numerator / Fraction(fr_sum).denominator)
            fr_sum = fr_sum - num
            print(f'{num} {fr_sum}')
    elif operator == '-':
        fr_sum = x - z
        if fr_sum > 1:
            num = int(Fraction(fr_sum).numerator / Fraction(fr_sum).denominator)
            fr_sum = fr_sum - num
            print(f'{num} {fr_sum}')




n = "-4/6 - -2"
classic_float(n)


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

def money_per_hour(money, hours):
    return round(money / hours, 2)

path_workers = os.path.join('data', 'workers')
path_hours = os.path.join('data', 'hours_of')

with open(path_workers, 'r', encoding='UTF-8') as f:
    f = f.readlines()[1:]
with open(path_hours, 'r', encoding='UTF-8') as d:
    d = d.readlines()[1:]
for i in f:
    workers = i.split()
    for j in d:
        hours = j.split()
        if workers[0] == hours[0] and workers[1] == hours[1]:
            print(workers[0], workers[1], hours[0], hours[1])
            if workers[4] >= hours[2]:
                money_score = money_per_hour(int(workers[2]), int(workers[4])) * int(hours[2])
                print(money_score)
            elif workers[4] < hours[2]:
                over_work = int(hours[2]) - int(workers[4])
                money_score = int(workers[2]) + over_work * money_per_hour(int(workers[2]), int(workers[4]))
                print(money_score)

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))



with open('data/fruits.txt', 'r', encoding='UTF-8') as fruits_list_txt:
    for fruit in fruits_list_txt.readlines():
        if fruit[0].isalpha():
            with open(f'data/fruits_{fruit[0].capitalize()}.txt', 'a', encoding='UTF-8') as  file_name:
                file_name.write(fruit)

