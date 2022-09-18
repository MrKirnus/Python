# -*- coding: utf-8 -*-
"""ДЗ. Понятие класса.ipynb

### Задание 1
Напишите функцию, которая возвращает название валюты (поле ‘Name’) с максимальным значением курса с помощью сервиса https://www.cbr-xml-daily.ru/daily_json.js
"""

import requests

class Rate:
    def __init__(self, format_= 'value'):
        self.format = format_
    
    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:
        
        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']
    
    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
        
        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()
        
        if currency in response:
            if self.format == 'full':
                return response[currency]
            
            if self.format == 'value':
                return response[currency]['Value']
        
        return 'Error'
    
    def max_value(self):
        """Возвращает название код валюты с максимальным значением курса"""
        max_val = 0
        for k,v in r.exchange_rates().items():
            if max_val < v['Value']:
                max_val = v['Value']
                name = v['Name']
        return(v['Name'], v['CharCode'])

r = Rate(format == 'full')

r.max_value()

"""### Задание 2
Добавьте в класс Rate параметр diff (со значениями True или False), который в случае значения True в методах курсов валют (eur, usd итд) будет возвращать не курс валюты, а изменение по сравнению в прошлым значением. Считайте, self.diff будет принимать значение True только при возврате значения курса. При отображении всей информации о валюте он не используется.
"""

class Rate:
    def __init__(self, format_ = 'value', check = 'True'):
        self.format = format_
    
    def exchange_rates(self):
        
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']
    
    def make_format(self, currency):
       
        response = self.exchange_rates()
        
        if currency in response:
            if self.format == 'full':
                return response[currency]
            
            if self.format == 'value':
                return response[currency]['Value']
        
        return 'Error'
    
    def diff(self, check):
        self.check = check
        
        xxx = input('Введите код вылюты ')
#         xxx = 'JPY'
        if self.format == 'value':
            if self.check=='True':
                for i in r.exchange_rates().values():
                    if i['CharCode'] == xxx:
                        print(xxx, i['Previous'] - i['Value'])
    
    def max_value(self):

        max_val = 0
        for k,v in r.exchange_rates().items():
            if max_val < v['Value']:
                max_val = v['Value']
                name = v['Name']
        return(v['Name'], v['CharCode'])

r=Rate('value', 'True')

r.diff('True')

"""### Задание 3
Напишите класс Designer, который учитывает количество международных премий. Подсказки в коде занятия в разделе “Домашнее задание задача 3”.


Комментарий по классу Designer такой:
Напишите класс Designer, который учитывает количество международных премий для дизайнеров (из презентации: “Повышение на 1 грейд за каждые 7 баллов. Получение международной премии – это +2 балла”). Считайте, что при выходе на работу сотрудник уже имеет две премии и их количество не меняется со стажем (конечно если хотите это можно вручную менять).

Класс Designer пишется по аналогии с классом Developer из материалов занятия.
"""

class Employee:
    def __init__(self, name, seniority, awards):
        self.name = name
        self.seniority = seniority
        self.awards = awards
        
        self.grade = 1
    
    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1
    
    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)

class Designer(Employee):
    def __init__(self, name, seniority, awards):
        super().__init__(name, seniority, awards)
        
    def check_if_it_is_time_for_upgrade(self):
        if self.seniority==0: 
            self.seniority=1+self.awards*2
        else:
            self.seniority+=1
            if self.seniority % 7==0:
                    self.grade_up()
        
        return self.publish_grade()