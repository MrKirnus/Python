# -*- coding: utf-8 -*-
"""

## Задание 1
Напишите функцию, которая принимает на вход строку и проверяет является ли она валидным транспортным номером (1 буква, 3 цифры, 2 буквы, 2-3 цифры). Обратите внимание, что не все буквы кириллического алфавита используются в транспортных номерах.

Если номер валиден, то функция должна возвращать отдельно номер и регион.

Примеры работы программы:

car_id = 'A222BC96’
Результат: Номер A222BС валиден. Регион: 96

car_id = 'АБ22ВВ193’
Результат: Номер не валиден
"""

import re

def valid_number():
    car_id = input()
    if len(re.findall(r'[А-ЯA-Z]\d{3}[А-ЯA-Z]{2}\d{2,3}', car_id)) > 0:
        print(f"Результат: Номер {car_id[0:6]} валиден. Регион {car_id[6:8]}")
    else:
        print('Результат: Номер не валиден')
        
valid_number()

def valid_number():
    car_id = input()
    if len(re.findall(r'[А-ЯA-Z]\d{3}[А-ЯA-Z]{2}\d{2,3}', car_id)) > 0:
        print(f"Результат: Номер {car_id[0:6]} валиден. Регион {car_id[6:8]}")
    else:
        print('Результат: Номер не валиден')
        
valid_number()

"""## Задание 2
Напишите функцию, которая будет удалять все последовательные повторы слов из заданной строки при помощи регулярных выражений.

Пример работы программы:

some_string = ‘Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений.’

Результат:
Напишите функцию, которая будет удалять все последовательные повторы слов из заданной строки при помощи регулярных выражений.
"""

def delete_copy():
    some_string = input()
    print()
    print('Результат:')
    return(re.sub(r'\b([^\W\d]+)(\s+\1)+\b', r'\1', some_string))
    
delete_copy()

"""## Задание 3
Напишите функцию, которая будет возвращать акроним по переданной в нее строке со словами.

Примеры работы программы:

some_words = 'Информационные технологии’
Результат: ИТ

some_words = 'Near Field Communication’
Результат: NFC
"""

def acronym():
    some_words = input()
    result = ''.join(re.findall(r'(\b\w)', some_words)).upper()
    return(f"Результат: {result}")

acronym()

def acronym():
    some_words = input()
    result = ''.join(re.findall(r'(\b\w)', some_words)).upper()
    return(f"Результат: {result}")

acronym()

"""## Задание 4
Напишите функцию, которая будет принимать на вход список email-адресов и выводить их распределение по доменным зонам.

Пример работы программы:

emails = [‘test@gmail.com’, ‘xyz@test.in’, ‘test@ya.ru’, ‘xyz@mail.ru’, ‘xyz@ya.ru’, ‘xyz@gmail.com’]

Результат:

gmail.com: 2
test.in: 1
ya.ru: 2
mail.ru: 1
"""

def number_domains(*args):
    """
    Выводит распределение списка email-адресов по доменным зонам
    """
    emails_dictionary = {}
    
    for i in re.findall(r"(?<=@).+?(?=')", str(args)):
        emails_dictionary[i] = emails_dictionary.setdefault(i, 0) + 1
    #     print(emails_dictionary.items())

    print('Результат:')
    for k, v in emails_dictionary.items():
        print(k, v)
        
number_domains('test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com')

?number_domains