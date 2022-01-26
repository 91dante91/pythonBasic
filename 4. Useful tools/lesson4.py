from sys import argv
from functools import reduce, partial
from itertools import count, cycle
# -----------------------------1(Скрипт с параметрами)-------------------------------#
# script_name, first_param, second_param, third_param = argv
#
# print("Имя скрипта", script_name)
# print("Параметр 1", first_param)
# print("Параметр 2", second_param)
# print("Параметр 3", third_param)
# ------------------------------2(Генераторы списков)-------------------------------#
#1
my_list = [2, 4, 6]
new_list = [el + 10 for el in my_list]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")

#2
lines = [line.strip() for line in open('text.txt')]
print(lines)

#3
my_list_1 = [10, 25, 30, 45, 50]
print(my_list_1)
new_list_1 = [el for el in my_list if el % 2 == 0]
print(new_list_1)

#4
str_1 = "abc"
str_2 = "d"
str_3 = "efg"
sets = [i + j + k for i in str_1 for j in str_2 for k in str_3]
print(sets)

#5
my_tuple = (2, 4, 6)
new_obj = (el + 10 for el in my_tuple)
print(new_obj)

#6
my_list_2 = [2, 4, 6]
new_obj_1 = (el + 10 for el in my_list_2)

print(new_obj_1)
for el in new_obj_1:
    print(el)

# ------------------------------3(Генераторы словарей и множеств)-------------------------------#
#1
my_dict = {el: el*2 for el in range(10, 20)}
print(my_dict)

#2
my_set = {el**3 for el in range(5, 10)}
print(my_set)

# ------------------------------4(Конструкция yield)-------------------------------#
#1
generator = (param * param for param in range(5))
for el in generator:
    print(el)

#2
generator = (param * param for param in range(5))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

#3
def generator():
    for el in (10, 20, 30):
        yield el

g = generator()
print(g)

for el in g:
    print(el)

# ------------------------------5(Модуль functools)-------------------------------#
#reduce

def my_func(prev_el, el):
    return prev_el + el

print(reduce(my_func, [10, 20, 30]))

#partial

def my_func(param_1, param_2):
    return param_1 ** param_2

new_my_func = partial(my_func, 2)
print(new_my_func)
print(new_my_func(4))

# ------------------------------5(Модуль itertools)-------------------------------#
#count
for el in count(7):
    if el > 15:
        break
    else:
        print(el)

#cycle
c = 0
for el in cycle("ABC"):
    if c > 10:
        break
    print(el)
    c += 1

progr_lang = ["python", "java", "perl", "javascript"]
iter = cycle(progr_lang)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))