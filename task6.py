import time

# Задание №6.1
# Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт

class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        print(self.__color[0])
        time.sleep(7)
        print(self.__color[1])
        time.sleep(2)
        print(self.__color[2])
        time.sleep(2)

tl = TrafficLight()
tl.running()

print("*" * 50)

# Задание №6.2
# Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width


class Highway(Road):
    def __init__(self, _length, _width, weight, thickness):
        Road.__init__(self, _length, _width)
        self.weight = weight
        self.thickness = thickness

    def mass(self):
        return f'{int((self._length * self._width * self.weight * self.thickness)/1000)} т.'


highway = Highway(5000, 20, 25, 5)
print(highway.mass())
print("*" * 50)

# Задание №6.3
# Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 150000, "bonus": 50000}

class Position(Worker):
    def __init__(self, name, surname, position):
        Worker.__init__(self, name, surname, position)


    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income.get("wage") + self._income.get("bonus")}'

worker = Position('Ivanov', 'Ivan', 'data analyst')
print(worker.get_full_name())
print(worker.get_total_income())
print("*" * 50)

# Задание №6.4
# Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return 'goes'

    def show_speed(self):
        return self.speed

    def stop(self):
        return 'stops'

    def turn(self, direction):
        return f'turned {direction}'

class TownCar(Car):
    def getinfo(self):
        return f'Класс: {TownCar.__name__}, Скорость: {self.speed}, Цвет: {self.color}, Марка: {self.name}, Полиция? - {self.is_police}'

    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости'

class WorkCar(Car):
    def getinfo(self):
        return f'Класс: {WorkCar.__name__}, Скорость: {self.speed}, Цвет: {self.color}, Марка: {self.name}, Полиция? - {self.is_police}'

    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости'

class PoliceCar(Car):
    def getinfo(self):
        return f'Класс: {PoliceCar.__name__}, Скорость: {self.speed}, Цвет: {self.color}, Марка: {self.name}, Полиция? - {self.is_police}'

towncar = TownCar(78, "beige", "BMW", False)
print(towncar.getinfo())
print(towncar.go())
print(towncar.show_speed())
print(towncar.turn('left'))
print(towncar.stop())
print("*" * 50)
workcar = WorkCar(60, "red", "MAN", False)
print(workcar.getinfo())
print(workcar.go())
print(workcar.show_speed())
print(workcar.turn('right'))
print(workcar.stop())
print("*" * 50)
towncar = PoliceCar(200, "blue", "Toyota", True)
print(towncar.getinfo())
print(towncar.go())
print(towncar.show_speed())
print(towncar.turn('left'))
print(towncar.stop())
print("*" * 50)

# Задание №6.5
# Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'drawing started'

class Pen(Stationery):
    def draw(self):
        return f'{self.title} drawing started'

class Pencil(Stationery):
    def draw(self):
        return f'{self.title} drawing started'

class Handle(Stationery):
    def draw(self):
        return f'{self.title} drawing started'

pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())