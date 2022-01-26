# ---------------------------------№1-------------------------------#
#
# def divide_number(num1, num2):
#     """The function returns the result of dividing two numbers
#
#     (number, number) -> (number)
#     >>> divide(100, 20)
#     5.0
#     """
#     try:
#         num1, num2 = float(num1), float(num2)
#         return round(num1 / num2, 4)
#     except ValueError:
#         return "Value Error"
#     except ZeroDivisionError:
#         return "Division by zero forbidden!!!"
#
#
#
# print(divide_number(input("Enter first number: "), input("Enter second number: ")))

# ---------------------------------№2-------------------------------#
# def get_user_date(user_name, year_of_birth, city_of_residence, email, phone_number):
#     """The function return the user data"""
#     return f"user_name: {user_name}, year_of_birth: {year_of_birth}, city_of_residence: {city_of_residence}, " \
#            f"email: {email}, phone_number: {phone_number}"
#
# print(get_user_date(user_name="Jack", year_of_birth="2018", city_of_residence="Moscow",
#     email="@gmail.com", phone_number="654564564564"))
# ---------------------------------№3-------------------------------#
# def my_func(arg1, arg2, arg3):
#     my_list = [arg1, arg2, arg3]
#     try:
#         my_list.remove(min(my_list))
#         return sum(my_list)
#     except TypeError:
#         return "Enter only a number!"
# print(my_func(20, 50, 10))
#
#
# def my_func2(arg1, arg2, arg3):
#     return sum(sorted([arg1, arg2, arg3])[1:])
#
#
# print(my_func(1975, 50, 1))

# my_func = lambda arg1, arg2, arg3: (arg1 + arg2 + arg3) - min(arg1, arg2, arg3)
# print(my_func(8, 7, 9))
# ---------------------------------№4-------------------------------#
# num1 = input("Введите действительное положительное число: ")
# num2 = input("Введите целое отрицательное число: ")


# def my_func1(x, y):
#     try:
#         x, y = float(x), int(y)
#         return x ** y
#     except TypeError:
#         return "Enter a float number and a negative power"
# print(my_func1(num1, num2))


# def my_func2(x, y):
#     try:
#         x, y = float(x), int(y)
#         if x <= 0 or y >= 0:
#             return "Не выполнено условие ввода данных:\nx должен быть больше 0\ny должен быть меньше 0"
#         else:
#             result = 1
#         for _ in range(abs(y)):
#             result /= x
#         return f"Результат возведения x в степень y: {round(result, 6)}"
#     except ValueError:
#         return "Программа работает только с числами."
#
# print(my_func2(num1, num2))


# ---------------------------------№5-------------------------------#
# def sum_num():
#     s = 0
#     while True:
#         in_list = input("Enter a number, input 'q' to exit: ").split()
#         for num in in_list:
#             if num == 'q':
#                 return s
#             else:
#                 try:
#                     s += float(num)
#                 except ValueError:
#                     print("To exit the program, enter - 'q'.")
#         print(f"Sum of numbers = {s}")
#
# print(sum_num())

# ------------------------Вариант-----------------------------------#

# num = 0
# try:
#     while num != '#':
#         for i in map(float, input("To exit enter: '#'\nEnter a numbers, using space.\n").split()):
#             num += i
#         print(num)
# except ValueError:
#     print(num)

# ---------------------------------№6-------------------------------#
# def int_func():
#     new_str = ""
#     for word in input("Enter a string of words separated by a space: ").split():
#         new_str += f"{word.title()} "
#     return new_str[:-1]
#
#
# print(int_func())
# ------------------------Вариант-----------------------------------#
# int_func = lambda word: word.title() if word and ascii(word)[1:-1].isalpha() else ''
# print(' _'.join(map(int_func, input("Enter phrase: ").split())))