import tkinter as tk
from PIL import ImageTk, Image
from itertools import cycle
# --------------------------------------1---------------------------------#


class TrafficLight:
    def __init__(self, working_algorithm):
        self.sec_count = 0
        self.working_algorithm = working_algorithm
        self.img_dict = {'red': Image.open('pic/red.jpg').resize((450, 600)),
                         'yellow': Image.open('pic/yellow.jpg').resize((450, 600)),
                         'green': Image.open('pic/green.jpg').resize((450, 600)),
                         'red + yellow': Image.open('pic/red + yellow.jpg').resize((450, 600)),
                         'off': Image.open('pic/tl_off.jpg').resize((450, 600))}
        self.iterator = cycle(self.working_algorithm)
        self.cur_state = next(self.iterator)

        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.geometry("400x600")
        image = ImageTk.PhotoImage(self.img_dict[self.cur_state[0]])
        self.label = tk.Label(image=image)
        self.label.pack(side="top", fill="both", expand="yes")
        self.running()
        self.root.mainloop()

    def running(self):
        self.sec_count += 1
        if self.sec_count == self.cur_state[1]:
            self.cur_state = next(self.iterator)
            self.sec_count = 0
            cur_img = ImageTk.PhotoImage(self.img_dict[self.cur_state[0]])
            self.label.configure(image=cur_img)
            self.label.photo_ref = cur_img
            self.label.pack()
        self.root.after(100, self.running)


mode = input("Enter traffic-light mode (0-simple, 1-advanced): ")
if mode == "0":
    app = TrafficLight([('red', 70), ('yellow', 20), ('green', 50)])
elif mode == "1":
    app = TrafficLight([('red', 70),
                        ('red + yellow', 20),
                        ('green', 50),
                        ('off', 5),
                        ('green', 5),
                        ('off', 5),
                        ('green', 5),
                        ('off', 5),
                        ('green', 5),
                        ('yellow', 20)])
else:
    print("Wrong choice!")

# --------------------------------------2---------------------------------#


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass_calculation(self):
        return f"{self._length} м * {self._width} м * 25 кг * 5см = {self._length * self._width * 25 * 5 * 0.001} т"


r = Road(5000, 20)
print(r.asphalt_mass_calculation())

# --------------------------------------3---------------------------------#


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self._income.values())}"


manager = Position("Igor", "Ivanov", "CEO", 25000, 1500)
print(manager.get_full_name())
print(manager.position)
print(manager.get_total_income())

# --------------------------------------4---------------------------------#

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} moved forward")

    def stop(self):
        print("Car stopped")

    def turn(self, direction):
        print(f"The car turned to {direction}")

    def show_speed(self):
        print(f"Current speed {self.speed}")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Warning!!! Speeding on {self.speed - 60}")
        else:
            print(f"Current speed {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Speeding on {self.speed - 40}")
        else:
            print(f"Current speed {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


t = TownCar(80, "red", "toyota", False)
t.go()
t.show_speed()

# --------------------------------------5---------------------------------#


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start rendering")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title} rendering")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} rendering")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} rendering")

pen = Pencil("pen")
pen.draw()