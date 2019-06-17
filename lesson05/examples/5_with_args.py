# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
import hw05_easy as easy
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy_file():
    src_file_name_temp = dir_name.split(".")
    dst_file_name = src_file_name_temp[0] + "_copy." + src_file_name_temp[1]
    if not dir_name:
        print("Вы не указали файл для копирования")
    try:
        shutil.copy(dir_name, dst_file_name)
        print(f"Бэкапирование прошло успешно. {dst_file_name}")
    except FileNotFoundError:
        print(f"{dir_name} не существует. Проверьте написание имени файла")

def rm_file():
    if not dir_name:
        print("Необходимо задать имя директории")
        return
    try:
        os.remove(dir_name)
        print(f"Директория {dir_name} успешно удалена!")

    except FileNotFoundError:
        print(f"Такой директории не существует")

def cd_dir():
    if not dir_name:
        print("Необходимо задать имя директории")
        return
    try:
        os.chdir(dir_name)
        print(f"Вы перешли в директорию {os.getcwd()}")
    except FileNotFoundError:
        print(f"Директории {dir_name} не существует")

def dir_list():
    print(os.listdir(path="."))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": rm_file,
    "cd": cd_dir,
    "ls": dir_list,

}

try:
    dir_name = sys.argv[2]
    print(dir_name)
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
