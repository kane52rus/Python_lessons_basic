import os
import shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def mkdir(file_name):
    os.mkdir(file_name)





n = 9
#for i in range(n):
    #os.mkdir(f"directory{i + 1}")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
current_list = os.listdir(path=".")
print(current_list)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
copied_script = shutil.copy("hw05_easy.py", "hw05_easy_copied.py")