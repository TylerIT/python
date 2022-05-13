import random
import json
# Задание №5.1
# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка
print(f'Задание №5.1 {"*" * 100}')

with open(r'task5_1.txt', 'w', encoding='utf-8') as f:
    while True:
        user_str = input('Введите строку: ')
        print(user_str)
        f.write(f'{user_str}\n')
        if user_str == '':
            break

with open(r'task5_1.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Способ на одну строку короче
with open(r'task5_1.txt', 'w', encoding='utf-8') as f:
    user_str = ' '
    while user_str != '':
        user_str = input('Введите строку: ')
        print(user_str)
        f.write(f'{user_str}\n')


with open(r'task5_1.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Задание №5.2
# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке
print()
print(f'Задание №5.2 {"*" * 100}')
print('*** Способ1 ***')

# Способ 1
with open(r'task5_2.txt', 'r', encoding='utf-8') as f:
    str_content = f.read()

ls_content = str_content.split('\n')
for i, el in enumerate(ls_content, 1):
    print(f'В строке №{i} - {el.count(" ") + 1} слов(а), содержимое строки: ({el})')

print('*** Способ2 ***')
# Способ2 - более логичный, за счёт обработки поочередно каждой строки (readlines) и посчета слов с помощью len строки
with open(r'task5_2.txt', 'r', encoding='utf-8') as f:
    str_content = f.readlines()
    for i, line in enumerate(str_content, 1):
        line = line.replace('\n', '')
        print(f'В строке №{i} - {len(line.split())} слов(а), содержимое строки: {line}')

# Задание 5.3
# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
print()
print(f'Задание №5.3 {"*" * 100}')

lastname = ['Иванов', 'Петров', 'Сидоров', 'Фёдоров', 'Игнатьев', 'Кириллов', 'Елисеев', 'Антонов', 'Захаров', 'Абрамов']
print('Сотрудники, у которых заработная плата меньше 20000:')

with open(r'task5_3.txt', 'w+', encoding='utf-8') as f:
    for el in lastname:
        f.write(f'{el} {random.randint(10000, 35000)}\n')
    f.seek(0)
    summ = 0
    quan = 0
    for line in f:
        summ += int(line.split()[1])
        quan += 1
        if int(line.split()[1]) < 20000:
            print(f'{line.split()[0]} : {line.split()[1]}')

print(f'Средняя заработная плата составляет: {summ/quan}')

# Задание №5.4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.
print()
print(f'Задание №5.4 {"*" * 100}')


translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

# Способ 1
ls_ru = []

with open(r'task5_4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split(' ', 1)
        ls_ru.append(translate[line[0]] + ' ' + line[1])

print(f'В файл task5_4.txt будет записано следующее содержимое: {ls_ru}')

with open(r'task5_4_new.txt', 'w', encoding='utf-8') as f:
    f.writelines(ls_ru)

# Способ 2 более локаничный
with open(r'task5_4.txt', 'r', encoding='utf-8') as f_read:
    with open(r'task5_4_new.txt', 'w', encoding='utf-8') as f_write:
        for line in f_read:
            f_write.writelines(line.replace(line.split()[0], translate[line.split()[0]]))

# Задание №5.5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
print()
print(f'Задание №5.5 {"*" * 100}')

# Способ 1
print('*** Способ1 ***')
with open(r'task5_5.txt', 'w+', encoding='utf-8') as f:
    for _ in range(1, 11):
        f.writelines(str(random.randint(1, 100)) + ' ')
    f.seek(0)
    numbers = f.read().split(' ')
    numbers.pop()
    print(sum(list(map(int, numbers))))

# Способ 2 более короткий, но без чтения файла после записи
print('*** Способ2 ***')
with open(r'task5_5.txt', 'w+', encoding='utf-8') as f:
    ls = [random.randint(1, 100) for _ in range(1, 11)]
    f.write(' '.join(map(str, ls)))
print(sum(ls))

# Задание №5.6
# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
# были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
print()
print(f'Задание №5.6 {"*" * 100}')

with open(r'task5_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        str = ''
        for el in line: str = ''.join([str, (el if el in '0123456789' else ' ')])
        res = list(map(int, str.split()))
        print(f'{line.split()[0]} {sum(res)}')

# Задача №5.7
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
print()
print(f'Задание №5.7 {"*" * 100}')
with open('task5_7.json', 'w', encoding='utf-8') as f_write:
    with open('task5_7.txt', 'r', encoding='utf-8') as f_read:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_read}
        res = [profit, {'average_profit': sum([int(i) for i in profit.values() if int(i) > 0]) /
                        len([int(i) for i in profit.values() if int(i) > 0])}]
    json.dump(res, f_write)
