from abc import ABC, abstractmethod
print('Задание №8.1')
class Data:

    @staticmethod
    def valid(obj):
        dd, mm, yy = Data().convert(obj)
        if dd < 1 or dd > 31:
            return ('Неверное число')
        elif mm <= 0 or mm  > 12:
            return ('Неверно задан месяц')
        elif yy > 2022 or yy < 2000:
            return ('Неверно задан год')
        else:
            return f'{dd}.{mm}.{yy}'

    @classmethod
    def convert(cls, str):
        dd, mm, yy = str.split('-')
        return int(dd), int(mm), int(yy)


print(f'{Data.valid("31-05-2022")}\n')

print("Задание №8.2")
class ZeroDivision(Exception): # Содание собственного исключения возможно при создании дочернего класса от встроенного родительского класса Exception
    def __init__(self, text):
        self.text = text

# Использую исключение в программе
try:
    divisible = int(input('Введите делимое: '))
    divisor = int(input('Введите делитель: '))
    if divisor == 0:
        raise ZeroDivision('') # 1. raise принудительно вызывает исключение ZeroDivision
except ZeroDivision: # 2. Тут обрабатывается вызванное конструкцией raise исключение ZeroDivision.
    print(ZeroDivision('На ноль делить нельзя')) # 3. Перегрузка метода __str__ уже имеется в классе Exception, поэтому print выведет переданный в качестве аргумента текст
else:
    print(divisible / divisor)
finally:
    print('end\n')


print('Задание №8.3')
class ls_control(Exception):
    def __init__(self, text):
        self.text = text


ls = []

while True:
    try:
        ls_i = input('Enter integer positive number (Enter "q" to exit): ')
        if ls_i.lower() == "q":
            print("You're out")
            break
        elif ls_i.isdigit() is False:
            raise ls_control('Enter only integer positive numbers!')
        else:
            ls.append(ls_i)
    except ls_control as err:
        print(err)
    finally:
        print(ls)
print()

print('Задание №8.4; №8.5; №8.6')

class num_control(Exception):
    def __init__(self, text):
        self.text = text

class Storage:
    def __init__(self):
        self.nomenclature = {}

    def store(self, unit, num, price):
        self.nomenclature[unit] = [num, price]

    def show(self):
        return self.nomenclature

    def get_number(self, obj):
        # получаем имя экземпляра класса, находим в номенклатуре по полному наименованию (строка из всех характеристик), возвращаем наименование объекта и количество на складе
        return f'{ObjName.GetName(obj)} - {self.nomenclature[obj.get_unit()][0]} шт.'

    def get_price(self, obj):
        return f'{ObjName.GetName(obj)} - {self.nomenclature[obj.get_unit()][1]} р.'


class Equipment(ABC):
    @abstractmethod
    def __init__(self, name, model):
        self.name = name
        self.model = model

    @abstractmethod
    def get_unit(self):
        pass


class Printer(Equipment):
    def __init__(self, name, model, color):
        super().__init__(name, model)
        self.color = color

    def get_unit(self):
        return f'Type: {Printer.__name__}, Name: {self.name}, Model: {self.model}, Color: {self.color}'



class Scanner(Equipment):
    def __init__(self, name, model, sheet_format):
        super().__init__(name, model)
        self.sheet_format = sheet_format

    def get_unit(self):
        return (f'Type: {Scanner.__name__}, Name: {self.name}, Model: {self.model}, Sheet_format: {self.sheet_format}')


class MFU(Equipment):
    def __init__(self, name, model, color, sheet_format):
        super().__init__(name, model)
        self.color = color
        self.sheet_format = sheet_format

    def get_unit(self):
        return (
            f'Type: {MFU.__name__}, Name: {self.name}, Model: {self.model}, Color: {self.color}, Sheet_format: {self.sheet_format}')

class ObjName:
  def GetName(self):
    for i, j in globals().items():
      if j is self:
        return i

Canon_LBP6030B = Printer("Canon", "LBP6030B", "черно-белая")
Fujitsu_SP_1425 = Scanner("Fujitsu", "SP-1425", "A4")
LaserJet_Pro_400 = MFU("HP", "LaserJet Pro 400", "черно-белая", "A4")
storage = Storage()
storage.store(Canon_LBP6030B.get_unit(), "5", "33999")
storage.store(Fujitsu_SP_1425.get_unit(), "3", "30999")
storage.store(LaserJet_Pro_400.get_unit(), "7", "57899")
print(f'{"*" * 20} вся номенклатура на складе оргтехники: {"*" * 20}')
print(storage.show())
print(f'{"*" * 20} посмотрим количество отдельных объектов оргтехники: {"*" * 20}')
print(storage.get_number(Canon_LBP6030B))
print(storage.get_number(Fujitsu_SP_1425))
print(storage.get_number(LaserJet_Pro_400))
print(f'{"*" * 20} зададим новое количество Fujitsu_SP_1425 на складе: {"*" * 20}')
storage.store(Fujitsu_SP_1425.get_unit(), '5', '33999')
print(storage.get_number(Fujitsu_SP_1425))
print(f'{"*" * 20} посмотрим стоимость сканеров Fujitsu_SP_1425: {"*" * 20}')
print(storage.get_price(Fujitsu_SP_1425))
print(f'{"*" * 20} посмотрим характеристики сканера Fujitsu_SP_1425: {"*" * 20}')
print(Fujitsu_SP_1425.get_unit())
print(f'{"*" * 20} передаем два сканера Fujitsu_SP_1425 бухгелтерии: {"*" * 20}')
accounts_dep = Storage()
accounts_dep.store(Fujitsu_SP_1425.get_unit(), '2', '0')
storage.store(Fujitsu_SP_1425.get_unit(), '3', '57899')
print(f'{"*" * 20} количество сканеров Fujitsu_SP_1425 на балансе бухгалтерии: {"*" * 20}')
print(accounts_dep.get_number(Fujitsu_SP_1425))
print(f'{"*" * 20} остаток сканеров Fujitsu_SP_1425 на складе оргтехники: {"*" * 20}')
print(storage.get_number(Fujitsu_SP_1425))
print()
print(f'{"*" * 20} Ручной ввод количества и стоимости {"*" * 20}\n')
while True:
    try:
        obj = input('Введите номер устройста, где 1 - Fujitsu_SP_1425, 2 - Canon_LBP6030B, 3 - LaserJet Pro 400 >>> ')
        if obj == '1':
            obj = Fujitsu_SP_1425.get_unit()
        elif obj == '2':
            obj = Canon_LBP6030B.get_unit()
        elif obj == '3':
            obj = LaserJet_Pro_400.get_unit()
        else:
            raise num_control("необходимо выбрать из списка")
        number = input('введите количество: ')
        price = input('введите стоимость: ')
        if number.isdigit() is False:
            raise num_control('Количество должно быть задано целым числом')
        elif price.isdigit() is False:
            raise num_control('Стоимость должна быть задана целым числом')
        else:
            storage.store(obj, number, price)
            break
    except num_control as err:
        print(err)
print(f'Новые данные:')
print(f'{storage.get_number(Fujitsu_SP_1425)}\n{storage.get_price(Fujitsu_SP_1425)}\n')

print("Задание №8.7")
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)