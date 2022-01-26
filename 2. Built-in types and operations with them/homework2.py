# -----------------------------------№1------------------------#
# my_list = [2, 3.23, "like", [1, 2], True, None]
# for i, item in enumerate(my_list):
#     print(f"{i}) {item} - {type(item)}")

# -----------------------------------№2-------------------------#
# user_list = input("Enter number with space - ").split()
# for i in range(1, len(user_list), 2):
#     user_list[i - 1], user_list[i] = user_list[i], user_list[i - 1]
# print(user_list)
# -----------------------------------№3-------------------------#
# month_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
#               9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
# month_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
#               "Ноябрь", "Декабрь"]
# while True:
#     user_month = input("Введите интересующий вас месяц года от 1 до 12: ")
#     if user_month.isdigit() and 0 < int(user_month) <= 12:
#         user_month = int(user_month)
#         if user_month in (1, 2, 12):
#             print(f"Месяц {month_dict[user_month]} это зима")
#             print(f"Месяц {month_list[user_month - 1]} это зима")
#             break
#         elif int(user_month) in (3, 4, 5):
#             print(f"Месяц {month_dict[user_month]} это весна")
#             print(f"Месяц {month_list[user_month - 1]} это весна")
#             break
#         elif int(user_month) in (6, 7, 8):
#             print(f"Месяц {month_dict[user_month]} это лето")
#             print(f"Месяц {month_list[user_month - 1]} это лето")
#             break
#         else:
#             print(f"Месяц {month_dict[user_month]} это осень")
#             print(f"Месяц {month_list[user_month - 1]} это осень")
#             break
#     else:
#         print('Error!!!')
# -----------------------------------№4-------------------------#
# my_str = input("Введите строку из нескольких слов, разделенных пробелами: ").split()
# words_in_str = my_str.split()
# for ind, word in enumerate(words_in_str, 1):
#     print(f'{ind} {word[:10]}')
# -----------------------------------№5-------------------------#
# my_list = [7, 5, 3, 3, 2]
# print(my_list)
# number = int(input("Enter new rating item: "))
# i = 0
# for n in my_list:
#     if number <= n:
#         i += 1
# my_list.insert(i, float(number))
# print(my_list)
# -----------------------------------№6-------------------------#
my_goods = []
i = 1
while True:
    print("Меню: ")
    print('1. Добавить товар.\n'
          '2. Просмотреть аналитику о товарах.\n'
          '3. Выход')
    answer = int(input("Выберите подходящий пункт меню: "))
    if answer == 1:
        title = input('Введите название товара: ')
        price = input('Введите цену товара: ')
        count = input('Введите количество товара: ')
        unit = input('Введите единицу измерения товара: ')
        my_dict = {'название':title,
                   'цена': price,
                   'количество': count,
                   'ед': unit}
        my_goods.append((i, my_dict))
        i += 1
    elif answer == 2:
        product_analytics = {
            'название': [product[1].get('название') for product in my_goods],
            'цена': [product[1].get('цена') for product in my_goods],
            'количество': [product[1].get('количество') for product in my_goods],
            'ед': list(set([product[1].get('eд') for product in my_goods]))
        }
        print(product_analytics)
    elif answer == 3:
        break
