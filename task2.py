# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list = (1, "2", True, [3, 4], 0.5, (1, 2), {'nuber1': 1, 'number2': 2})

for el in list:
    print(type(el), el)

# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

# Решение через цикл for
user_list = input('Введите элементы списка через пробел: ').split(' ')
for i in range(0, len(user_list) - 1, 2):  # len(user_list)-1 --> для нечетного количества элементов, шаг 2, чтобы увеличивать i на 2
    print('i =', i)
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    print(user_list)

# Решение через цикл while
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
i = 0
while i < len(list2) - 1:
    list2[i], list2[i + 1] = list2[i + 1], list2[i]
    i += 2
print(list2)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

month = int(input('Введите номер месяца цифрой от 1 до 12: '))

d_month = {'winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'autumn': [9, 10, 11]}

for key in d_month:
    if month > 12:
        print(f'Месяца {month} не существует')
        break
    if month in d_month[key]:
        print(f' month {month} - is {key}')


l_month = [['winter', 12, 1, 2], ['Spring', 3, 4, 5], ['Summer', 6, 7, 8], ['autumn', 9, 10, 11]]

for el in l_month:
    if month > 12:
        print(f'Месяца {month} не существует')
        break
    if month in el:
        print(f' month {month} - is {el[0]}')

# Хитрый вариант решения
l_month = ['winter', 'Spring', 'Summer', 'autumn']
if month > 12:
    print(f'Месяца {month} не существует')
else:
    print(f' month {month} - is {l_month[month // 3]}')

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

l_str = input('Введите строку инескольких слов >>> ').split()
for i, el in enumerate(l_str, 1):
    print(f' {i}. {el[0:10]}')

# 5. Реализовать структуру «Рейтинг»,
# представляющую собой набор натуральных чисел,
# который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2]

rating = [7, 5, 3, 3, 2]
print(rating)
new_rat = int(input('Введите число от 0 до 10 >>> '))

# Простой вариант решения
rating.append(new_rat)
rating.sort(reverse=True)
print(f'Рейтинг обновлен: {rating}')

# Алгоритмический вариант решения
rating2 = [7, 5, 3, 3, 2]

i = 0
for el in rating2:
    if new_rat <= el:
        i += 1
rating2.insert(i, new_rat)
print(f'Рейтинг обновлен: {rating2}')

# 6. (Дополнительно) Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
#
# Пример готовой структуры:
#
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
#
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }