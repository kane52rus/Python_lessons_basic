import hw05_easy as easy
import sys
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
result = 0
def help():
    print("Добро пожаловать в консольную утилиту!")
    print("В вашем распоряжении следующие функции:")
    print("cd <dir_name> - переход в папку")
    print("mkdir <dir_name> - создание директории")
    print("rm <dir_name> - удаление директории")
    print("ls - получить список файлов")
    print("help - получить подсказку")
    print("q - для выхода")

menu = {
    "cd": easy.cd,
    "mkdir": easy.mkdir,
    "rm": easy.remove_file,
    "ls": easy.current_dir_list,
    "help": help
}
help()
while result != "q":
    result = input("Укажите, что хотите сделать: ")
    result = result.split(" ")
    try:
        key = result[0]
        print(key)
    except IndexError:
        key = None
    try:
        dir_name = result[1]
        print(dir_name)
    except IndexError:
        dir_name = None

    if key:
        if menu.get(key) == help or menu.get(key) == easy.current_dir_list:
            menu[key]()
        elif menu.get(key):
            menu[key](dir_name)
        elif key == "q":
            print("Вы вышли из программы, до свидания!")
            break
        else:
            print("Задан неверный ключ")


