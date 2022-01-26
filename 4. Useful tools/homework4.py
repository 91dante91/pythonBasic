from sys import argv
from functools import reduce
from itertools import count, cycle
# --------------------------------------1---------------------------------#
# script_name, production_in_hours, rate_in_hour, prize = argv
#
#
# def salary():
#     try:
#         time, rate, bonus = map(float, argv[1:])
#         print (f"Salary - {time * rate + bonus}")
#     except ValueError:
#         print("Enter all 3 numbers. Not string or empty character.")
#
#
# salary()

# --------------------------------------2---------------------------------#
# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el -1]]
# print(new_list)

# --------------------------------------3---------------------------------#
#
# my_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
# print(my_list)

# --------------------------------------4---------------------------------#
#
# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_list = [el for el in my_list if my_list.count(el) == 1]
# print(f"Source list\n{new_list}\nNo repetition list\n{new_list}")

#Вариант решения
# print(my_list:= [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11], '\n', [i for i in my_list if my_list.count(i) == 1], sep="")

# --------------------------------------5---------------------------------#
#
#
# def multiply_elem(prev_el, el):
#     return prev_el * el
#
#
# my_list = [el for el in range(100, 1001, 2)]
# print(f"List\n{my_list}\nMultiplication of numbers\n{reduce(multiply_elem, my_list)}")

#Вариант решения
# print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))
# --------------------------------------6---------------------------------#
# a)
# print('Программа генерирует целые числа начиная с указанного. Для генерации следующего числа необходимо нажать Enter,'
#       'для выхода из программы - "q"')
# for el in count(int(input("Введите стартовое число: "))):
#     print(el, end='')
#     quit = input()
#     if quit == 'q':
#         break
# # b)
# print('Программа повторяет эелементы списка. Для генерации следующего повторения необходимо нажать Enter,'
#       'для выхода из программы - "q"')
# u_list = input('Введите список, разделяя элементы пробелом: ').split()
# iter = cycle(u_list)
# quit = None
#
# while quit != 'q':
#     print(next(iter), end='')
#     quit = input()


# --------------------------------------7---------------------------------#
#
#
# def fact_gen(number):
#     f_num = 1
#     if number == 0:
#         yield f"{number}! = 1"
#     for i in range(1, number + 1):
#         f_num *= i
#         yield f'{i} = {f_num}'
#
# for el in fact_gen(int(input('Factorial number: '))):
#     print(el)


#Вариант решения
def fact(n):
    try:
        yield reduce(lambda x, y: x * y, list(el if el > 0 else 1 for el in range(n + 1)))
    except TypeError:
        yield 0

for i in fact(4):
    print(i)