import math
__author__ = 'Табункин Андрей Алексеевич'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?
a = math.inf
if a > 999999:
    print(True)
else:
    print(False)
if a == a ** 2:
    print(True)
else:
    print(False)
if a == a * 2:
    print(True)
else:
    print(False)

print("Неизвестное число равно: ", a)
# Подсказка: это значение точно есть ;)
