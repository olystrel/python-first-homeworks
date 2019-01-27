# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil

def create_folder(number_folder):
   i = 1
   while i <= number_folder:
        b = os.path.join(os.getcwd(), "dir_{}".format(i))
        try:
            os.mkdir(b)
            print("dir_{}, папка создана".format(i))
        except FileExistsError:
            print("Такой файл уже существует!")
        i += 1

create_folder(9)

def remove_folder(number_folder):
    i = 1
    while i <= number_folder:
        b = os.path.join(os.getcwd(), "dir_{}".format(i))
        try:
            os.rmdir(b)
            print("dir_{}, папка удалена".format(ш))
        except FileExistsError:
            print("Такого файла нет в этой директории!")
        i += 1


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show():
    way_check = os.path.join(os.getcwd())                   
    show_file= os.listdir(a)                          
    for i in b:
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_folder():
    way_cheak = os.path.realpath(__file__)                        
    rename_copy = a + ".bak"                                
    shutil.copy(a, b)
    print(a, "/n", b)  
