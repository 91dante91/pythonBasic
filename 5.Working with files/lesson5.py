import json
import shutil
import sys

out_f = open("out_file.txt", 'w')
out_f.write("String string string")
out_f.close()

#-----------------------Менеджеры контекста-----------------------#
with open("text.txt") as f_obj:
    for line in f_obj:
        print(line, end="")

#---------------------Выявление ошибок при работе с файлами-------#
#Вариант 1
try:
    f_obj = open("text.txt")
    for line in f_obj:
        print(line, end="")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f_obj.close()

#Вариант 2
try:
    with open("text.txt") as f_obj:
        for line in f_obj:
            print(line, end="")
except IOError:
    print("Произошла ошибка ввода-вывода!")

#--------------------- Режим + ----------------------------------#
with open("file.dat", 'r+') as f_obj:
    f_obj.write("another string")
    f_obj.seek(0)
    content = f_obj.read()
    print(content)
#--------------------- Параметры файлового объекта ----------------#
f_obj = open("new_file.txt", 'w')
f_obj.close()
print("Файл. Имя: ", f_obj.name)
print("Файл. Закрыт: ", f_obj.closed)
print("Файл. Режим: ", f_obj.mode)
#--------------- Определение позиции указателя в файле ----------#
f_obj = open("new_file.txt", 'r')
content = f_obj.read(3)
print("Текущая позиция: ", f_obj.tell())
# print(content)
# content = f_obj.read()
# print(content)
f_obj.seek(0)
print(f_obj.read(11))
f_obj.close()
#---------------------------- Print в файл ------------------------#
with open("python.txt", 'w', encoding='utf-8') as f_obj:
    print("Необычная работа функции print", file=f_obj)

#---------------------------- Json в Python ------------------------#
#Сериализация
data = {
"income" : {
"salary" : 50000 ,
"bonus" : 20000
}
}

with open("my_file.json",  "w") as write_f:
    json.dump(data, write_f, indent=4)

json_str = json.dumps(data)
print(json_str)
print(type(json_str))

# Десериализация
with open("my_file.json") as read_f:
    data = json.load(read_f)

print(data)
print(type(data))

json_str = """{"income": {"salary": 50000, "bonus": 20000}}"""
data = json.loads(json_str)
print(data)
print(type(data))

#---------------------------- Модуль shutil ------------------------#
# 1) Копирование содержимого одного файлового объекта ( f_obj_1 ) в другой ( f_obj_2 ).

shutil.copyfileobj(f_obj_1, f_obj_2)

# 2) Копирование содержимого (но не метаданных) одного файла ( f_1 ) в другой ( f_2 ).

shutil.copyfile(f_1, f_2)

# 3) Копирование содержимого файла my_f в файл или папку my_target . Если копирование
# выполняется в директорию, файл копируется с исходным именем ( my_f ).

shutil.copy(my_f, my_target)

# 4) Рекурсивное копирование дерева директорий my_tree в папку my_target .

shutil.copy(my_tree, my_target)

# 5) Удаление текущей директории и всех поддиректорий.

shutil.rmtree(path)

# 6) Рекурсивное перемещение файла или директории ( my_obj ) в нужную директорию ( my_target ).

shutil.move(my_obj, my_target)

#---------------------------- Модуль sys ------------------------#

print(sys.executable)
sys.exit(0)
print(sys.path)
print(sys.platform)