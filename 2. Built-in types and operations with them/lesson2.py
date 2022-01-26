# -----------------------------Strings-------------------------#
# my_string = "abracadabra"

# --------------------------Обратная итеррация------------------#
# for el in reversed(my_string):
#     print(el)

# -----------------------------Реверс на месте------------------#
# str_reverse = ""
# symbols = list(my_string)
# print(symbols)
# for el in range(len(my_string) // 2):
#     tmp = symbols[el]
#     symbols[el] = symbols[len(my_string) - el - 1]
#     symbols[len(my_string) - el - 1] = tmp
# str_reverse = ''.join(symbols)
# print(str_reverse)

# -----------Объединение списков разной длины без цикла. Ф-я sum()---#
# my_list = [[10, 20, 30], [40, 50], [60], [70, 80, 90]]
# print(sum(my_list, []))

# ------------------Удаление дубликатов в списке---------------------#
# my_list = [10, 10, 3, 4, 5, 9, 30, 30]
# print(list(set(my_list)))

# ------------------Обмен значениями через кортежи---------------------#
# var_1, var_2 = 20, 30
# print(var_1, var_2)
# var_1, var_2 = var_2, var_1
# print(var_1, var_2)

# ------------------Поиск самых часто встречающихся элементов списка---------------------#
# my_list = [10, 20, 20, 20, 30, 50, 70, 30]
# print(max(set(my_list), key=my_list.count))

# ------------------Распаковка последовательностей при неизвестном количестве элементов---------------------#
# my_list = [20, 30, 40, 50]
# *el_1, el_2, el_3 = my_list
# print(el_1, el_2, el_3)
# el_1, *el_2, el_3 = my_list
# print(el_1, el_2, el_3)
# el_1, el_2, *el_3 = my_list
# print(el_1, el_2, el_3)
# el_1, el_2, el_3, *el_4 = my_list
# print(el_1, el_2, el_3, el_4)
# el_1, el_2, el_3, el_4, *el_5 = my_list
# print(el_1, el_2, el_3, el_4, el_5)

# ------------------Сортировка словаря по значениям---------------------#
# my_dict = {'python': 1991, 'java': 1995, 'c++': 1983}
# print(sorted(my_dict))  # по умолчанию сортировка по ключам
# print(sorted(my_dict, key=my_dict.get))

# ------------------Нумерованные списки---------------------#
# for ind, el in enumerate(['ноль', 'один', 'два', 'три']):
#     print(ind, el)
#
# for ind, el in enumerate(['один', 'два', 'три'], 1):
#     print(ind, el)

# ------------------Транспонирование матрицы---------------------#
old_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(old_list)
new_list = zip(*old_list)
print(list(new_list))
