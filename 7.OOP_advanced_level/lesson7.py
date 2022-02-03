#---------------------------- Перегрузка операторов ------------------------#
"""
● __init__() — соответствует конструктору объектов класса, срабатывает при создании
объектов,
● __del__() — соответствует деструктору объектов класса, срабатывает при удалении объектов,
● __str__() — срабатывает при передаче объекта функциям str() и print(), преобразует объект к
строке,
● __add__() — срабатывает при участии объекта в операции сложения в качестве операнда с
левой стороны, обеспечивает перегрузку оператора сложения,
● __setattr__() — срабатывает при выполнении операции присваивания значения атрибуту
объекта,
● __getitem__() — срабатывает при извлечении элемента по индексу,
● __call__() — срабатывает при обращении к экземпляру класса как к функции,
● __gt__() — соответствует оператору > ,
● __lt__() — соответствует оператору < ,
● __ge__() — соответствует оператору ≥ ,
● __le__() — соответствует оператору ≤ ,
● __eq__() — соответствует оператору == ,
● __iadd__() — соответствует операции «Сложение и присваивание» += ,
● __isub__() — соответствует операции «Вычитание и присваивание» -= """

# 1. __init__


class MyClass:
    def __init__(self, param):
        self.param = param


mc = MyClass("text")
print(mc.param)

# 2. __del__


class MyClass:
    def __init__(self, param):
        self.param = param

    def __del__(self):
        print(f"Удаляем объект {self.param} класса MyClass")


mc = MyClass("text")
del mc

# 3. __str__


class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def __str__(self):
        return f"Объект с параметрами ({self.param_1}, {self.param_2})"


mc = MyClass("text_1", "text_2")
print(mc)

# 4. __add__


class MyClass:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        return MyClass(self.width + other.width, self.height + other.height)

    def __str__(self):
        return f"Объект с параметрами ({self.width}, {self.height})"


mc_1 = MyClass(10, 20)
mc_2 = MyClass(30, 40)
print(mc_1 + mc_2)

# 5. __setattr__


class MyClass:
    def __setattr__(self, attr, value):
        if attr == "width":
            self.__dict__[attr] = value
        else:
            print(f"Атрибут {attr} недопустим")


mc = MyClass()
mc.height = 40

# 5. __getitem__
# 1)


class MyClass1:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return str(self.param)


class Class2:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(MyClass1(el))


my_obj = Class2(10, True, "text")
print(my_obj.my_list[1])

# 2)


class Class1:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return str(self.param)


class Class2:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(Class1(el))

    def __getitem__(self, index):
        return self.my_list[index]


my_obj = Class2(10, True, "text")
print(my_obj.my_list[0])
print(my_obj[1])
print(my_obj[2])

# 6. __call__


class MyClass:
    def __init__(self, param):
        self.param = param

    def __call__(self, new_param):
        self.param = new_param

    def __str__(self):
        return f"Значение пареметра - {self.param};"


obj_1 = MyClass("width")
obj_2 = MyClass("height")

obj_1("length")
obj_2("square")

print(obj_1, obj_2)

# 7. __eg__


class MyClass:
    def __init__(self):
        self.x = 40

    def __eq__(self, y):
        return self.x == y


mc = MyClass()
print("Равно" if mc == 40 else "Не равно")
print("Равно" if mc == 41 else "Не равно")

# 8. __lt__


class Salary:
    val = 50000

    def __lt__(self, other):
        print("Оклад меньше премии?")
        return self.val < other.val


class Prize:
    val = 5000

    def __lt__(self, other):
        print("Премия меньше оклада?")
        return self.val < other.val


s = Salary()
p = Prize()

check = (p < s)
print(check)

# 9. __iadd__


class MyClass:
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):
        self.val += other
        return self

mc = MyClass(100)
print(mc.val)
mc += 200
print(mc.val)

#---------------------------- Переопределение методов ------------------------#


class ParentClass:
    def __init__(self):
        print("Конструктор класса-родителя")

    def my_method(self):
        print("Метод my_method() класса ParentClass")


class ChildClass(ParentClass):
    def __init__(self):
        print("Конструктор дочернего класса")
        ParentClass.__init__(self)

    def my_method(self):
        print("Метод my_method() класса ChildClass")
        ParentClass.my_method(self)


c = ChildClass()
c.my_method()

# super


class ParentClass:
    def __init__(self):
        print("Конструктор класса-родителя")

    def my_method(self):
        print("Метод my_method() класса ParentClass")


class ChildClass(ParentClass):
    def __init__(self):
        print("Конструктор дочернего класса")
        super().__init__()

    def my_method(self):
        print("Метод my_method() класса ChildClass")
        super().my_method()


c = ChildClass()
c.my_method()

#---------------------------- Интерфейсы ------------------------#
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_method_1(self):
        pass

    @abstractmethod
    def my_method_2(self):
        pass


class MyClass(MyAbstractClass):
    def my_method_1(self):
        print("Метод my_method_1()")

    def my_method_2(self):
        print("Метод my_method_2()")


mc = MyClass()

#---------------------------- Интерфейс итерации ------------------------#

my_list = [30, 105.6, "text", True]
for el in my_list:
    print(el)


class Iterator:
    """Объект - итератор"""
    def __init__(self, start=0):
        self.i = start
    # У итератора есть метод __next()__

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


class IterObj:
    """Объект, поддерживающий интерфейс итерации (итерируемый объект)"""

    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        # Метод __iter__ должен возвращать объект-итератор
        return Iterator(self.start)


obj = IterObj(start=2)
for el in obj:
    print(el)

print("Еще раз ...")
for el in obj:
    print(el)

# 1)


class Iter:
    def __init__(self, start=0):
        self.i = start - 1

    # Метод __iter()__ должен возвращать объект-итератор
    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


obj = Iter(start=2)
for el in obj:
    print(el)

#---------------------------- Декоратор @property ------------------------#


class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    @property
    def my_method(self):
        return f"Парметры, переданные в класс:"\
                f"{self.param_1}, {self.param_2}"


mc = MyClass("text_1", "text_2")
print(mc.param_1)
print(mc.param_2)

print(mc.my_method)

# 1.
# класс Auto


class Auto:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year

    def get_auto_year(self):
        return f"Автомобиль выпущен в {str(self.year)} году"


a = Auto(2090)
print(a.get_auto_year())

#---------------------------- Композиция ------------------------#


class WindowDoor:
    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height


class Room:
    def __init__(self, len_1, len_2, height):
        self.square = 2 * height * (len_1 + len_2)
        self.wd = []

    def add_win_door(self, wd_len, wd_height):
        self.wd.append(WindowDoor(wd_len, wd_height))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square


r = Room(7, 4, 3.7)
print(r.square)
r.add_win_door(2, 2)
r.add_win_door(2, 2)
r.add_win_door(2, 2)
print(r.common_square())
