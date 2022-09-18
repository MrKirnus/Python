# -*- coding: utf-8 -*-
<<<<<<< HEAD:HW_2 Списки и Циклы.py
"""ДЗ_Управляющие_конструкции_и_коллекции._Часть_1ipynb
=======
>>>>>>> 467f92917f93770f6e565763fa872d2de047fa7e:HW_2.py

## Задание 1

Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:

среднюю букву, если число букв в слове нечетное;
две средних буквы, если число букв четное.
Примеры работы программы:

word = 'test'
Результат:
es

word = 'testing'
Результат:
t
"""

word = str(input('введите слово '))
if len(word) % 2 != 0:
    print(word[int(len(word) / 2)])
else:
    print(word[int(len(word) / 2 - 1) : int(len(word) / 2) + 1])
print('Конец программы')

word = str(input('введите слово '))
if len(word) % 2 != 0:
    print(word[int(len(word) / 2)])
else:
    print(word[int(len(word) / 2 - 1) : int(len(word) / 2) + 1])
print('Конец программы')

"""## Задание 2

Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз) и после первого нуля выводит сумму всех ранее введенных чисел.

Примеры работы программы:

Введите число:  
1

Введите число:  
4

Введите число:  
6

Введите число:  
0
Результат:
11

Введите число:  
0
Результат:
0
"""

number = int(input('Введите число: '))
start_number = 0
while number != 0:
    start_number = number + start_number
    number = int(input('Введите число: '))
print(f'Результат: {start_number}')

start_number = 0
while True:
    number = int(input('Введите число: '))
    if number == 0:
        break
    start_number = number + start_number
print(f'Результат: {start_number}')

"""## Задание 3

Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки! Но мы не будем никого знакомить, если кто-то может остаться без пары:

Примеры работы программы:

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
Результат:

Идеальные пары:  
Alex и Emma  
Arthur и Kate  
John и Kira  
Peter и Liza  
Richard и Trisha
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
Результат:
Внимание, кто-то может остаться без пары!
"""

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) == len(girls):
    print('Идеальные пары:')
    match = zip(sorted(boys), sorted(girls))
    for element in match:
        print(f'{element[0]} и {element[1]}')
else:
    print('Внимание, кто-то может остаться без пары!')

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) == len(girls):
    print('Идеальные пары:')
    match = zip(sorted(boys), sorted(girls))
    for element in match:
        print(f'{element[0]} и {element[1]}')
else:
    print('Внимание, кто-то может остаться без пары!')

"""##Задание 4

У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период по странам (структура данных в примере). Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!) для каждой страны.

Пример работы программы:

countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
Результат:

Средняя температура в странах:
Thailand  -  23.9 С
Germany  -  13.8 С
Russia  -  3.7 С
Poland  -  12.0 С
"""

countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
for element in countries_temperature:
    print(f'{element[0]} - {round((sum(element[1]) / len(element[1]) - 32.0) / 1.8, 1)} C')

"""## Задание 5 (необязательное)
Дан поток логов по количеству просмотренных страниц для каждого пользователя. Вам необходимо написать алгоритм, который считает среднее значение просмотров на пользователя. Т. е. надо посчитать отношение суммы всех просмотров к количеству уникальных пользователей.

Примеры работы программы:

stream = [
‘2018-01-01,user1,3’,
‘2018-01-07,user1,4’,
‘2018-03-29,user1,1’,
‘2018-04-04,user1,13’,
‘2018-01-05,user2,7’,
‘2018-06-14,user3,4’,
‘2018-07-02,user3,10’,
‘2018-03-21,user4,19’,
‘2018-03-22,user4,4’,
‘2018-04-22,user4,8’,
‘2018-05-03,user4,9’,
‘2018-05-11,user4,11’,
]
Результат:
Среднее количество просмотров на уникального пользователя: 23.25

stream = [
‘2018-01-01,user100,150’,
‘2018-01-07,user99,205’,
‘2018-03-29,user1001,81’
]
Результат:
Среднее количество просмотров на уникального пользователя: 145.33
"""

stream = [
'2018-01-01,user1,3',
'2018-01-07,user1,4',
'2018-03-29,user1,1',
'2018-04-04,user1,13',
'2018-01-05,user2,7',
'2018-06-14,user3,4',
'2018-07-02,user3,10',
'2018-03-21,user4,19',
'2018-03-22,user4,4',
'2018-04-22,user4,8',
'2018-05-03,user4,9',
'2018-05-11,user4,11',
]

result = 0
nos = 0
user_name = 0
for element in stream:
    stream_list = element.split(',')
    result += int(stream_list[2])
    while stream_list[1] != user_name:
        user_name = stream_list[1]
        nos += 1
print(round(result/nos, 2))

stream = [
'2018-01-01,user100,150',
'2018-01-07,user99,205',
'2018-03-29,user1001,81'
]

result = 0
nos = 0
user_name = 0
for element in stream:
    stream_list = element.split(',')
    result += int(stream_list[2])
    while stream_list[1] != user_name:
        user_name = stream_list[1]
        nos += 1
print(round(result/nos, 2))
