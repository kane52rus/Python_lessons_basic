import os
import shutil
import sys
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def n_mkdir(n):
    for i in range(n):
        os.mkdir(f"directory{i + 1}")
def n_rmdir(n):
    for i in range(n):
        os.rmdir(f"directory{i + 1}")

n = 9

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def current_dir_list():
    print(os.listdir(path="."))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file(src_file_name):
    src_file_name_temp = src_file_name.split(".")
    dst_file_name = src_file_name_temp[0] + "_copy." + src_file_name_temp[1]
    shutil.copy(src_file_name, dst_file_name)






def mkdir(dir_name):
    if not dir_name:
        print("Необходимо задать имя директории")
        return
    try:
        os.mkdir(dir_name)
        print(f"Директория {dir_name} успешно создана!")
    except FileExistsError:
        print(f"Директория {dir_name} уже существует!")


def remove_file(dir_name):
    if not dir_name:
        print("Необходимо задать имя директории")
        return
    try:
        os.rmdir(dir_name)
        print(f"Директория {dir_name} успешно удалена!")

    except FileNotFoundError:
        print(f"Такой директории не существует")


def cd(dir_name):
    if not dir_name:
        print("Необходимо задать имя директории")
        return
    try:
        os.chdir(dir_name)
        print(f"Вы перешли в директорию {os.getcwd()}")
    except FileNotFoundError:
        print(f"Директории {dir_name} не существует")
