from translate import Translator
from googletrans import Translator
from random import randint
import json
import requests
# --------------------------------------1---------------------------------#
print("The program writes the entered data line by line to a text file. To complete the data entry in the line,"
      "press 'Enter,'. The program exits by entering an empty string.")
with open("exercise_1.txt", "a", encoding="utf-8") as f:
    while True:
        data = input("Enter the data to write to the file: ")
        if not data:
            break
        f.write(f"{data}\n")

# Вариант решения
print("The program writes the entered data line by line to a text file. To complete the data entry in the line,"
      "press 'Enter,'.\nThe program exits by entering an empty string.")
with open("exercise_1.txt", "a", encoding="utf-8") as f:
    while(data := input("Enter the data to write to the file: ")) != "":
        print(data, file=f)


# --------------------------------------2---------------------------------#
with open("exercise_2.txt", encoding="utf-8") as f:
    usefulness = [f'{count}.{" ".join(line.split())} - {len(line.split())} слов'
                  for count, line in enumerate(f, 1)]
    print(*usefulness, f'Всего строк - {len(usefulness)}', sep="\n")

# --------------------------------------3---------------------------------#
with open("exercise_3.txt", encoding="utf-8") as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f }
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Employees with salary less than 20000: {", ".join([key for key, value in employees_dict.items() if value < 20000])}.')

# --------------------------------------4---------------------------------#
rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
try:
    with open("new_exercise_4.txt", mode="a", encoding="utf-8") as new_f:
        with open("exercise_4.txt", encoding="utf-8") as f:
            new_f.writelines([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in f])
except IOError:
    print("An I/O error has occurred!")

# --------------------------------------5---------------------------------#

with open("exercise_5.txt", "a+") as f:
    my_list = [randint(1, 100) for _ in range(10)]
    f.write(" ".join(map(str, my_list)))

print(f"The sum of the numbers in the file: {sum(my_list)}")
# --------------------------------------6---------------------------------#

new_dict = {}
with open("exercise_6.txt", encoding="utf-8") as f:
    for row in f:
        name, stats = row.split(":")
        name_sum = sum(map(int, "".join([i for i in stats if i == " " or "9" >= i >= '0']).split()))
        new_dict[name] = name_sum
    print(new_dict)
# --------------------------------------7---------------------------------#

with open("exercise_7.json", "w", encoding="utf-8") as new_f:
    with open("exercise_7.txt", encoding="utf-8") as f:
        profit = {row.split()[0]: int(row.split()[2]) - int(row.split()[3]) for row in f}
        result = [profit, {"average_profit": round(sum([int(i) for i in profit.values() if int(i) > 0]) / len(
            [int(i) for i in profit.values() if int(i) > 0]))}]
        json.dump(result, new_f, ensure_ascii=False, indent=4)