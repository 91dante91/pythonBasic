from abc import ABC, abstractmethod
# --------------------------------------1---------------------------------#


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip(*i)) for i in zip(self.matrix, other.matrix)])


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_1 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(m)
print(m_1)
print(m + m_1)

# -------------------------------------- 2 ---------------------------------#


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return self.fabric_consumption + other.fabric_consumption


class Coat(Clothes):
    @property
    def fabric_consumption(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def fabric_consumption(self):
        return 2 * self.param + 0.3 / 100


coat = Coat(55)
costume = Costume(170)
print(coat + costume)

# -------------------------------------- 3 ---------------------------------#


class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        return self.count - other.count if self.count - other.count > 0 \
            else "Ячеек в первой клетке меньше чем во второй, вычитание не возможно!"

    def __mul__(self, other):
        return self.count * other.count

    def __floordiv__(self, other):
        if other.count != 0:
            return self.count // other.count
        else:
            raise ZeroDivisionError

    def make_order(self, row):
        return '\n'.join(['*' * row for _ in range(self.count // row)]) + '\n' + '*' * (self.count % row)


c_1 = Cell(15)
c_2 = Cell(11)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 // c_2)
print(c_1.make_order(7))
c_2.make_order(5)
