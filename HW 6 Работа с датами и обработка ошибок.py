# -*- coding: utf-8 -*-
"""

## Задание 1
Печатные газеты использовали свой формат дат для каждого выпуска. Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime:
The Moscow Times - Wednesday, October 2, 2002
The Guardian - Friday, 11.10.13
Daily News - Thursday, 18 August **1977**
"""

from datetime import datetime

# The Moscow Times
datetime.strptime('October 2, 2002', '%B %d, %Y')

# The Guardian
datetime.strptime('Friday, 11.10.13', '%A, %d.%m.%y')

# Daily News
datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')

"""## Задание 2
Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]

Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой даты возвращает True (дата корректна) или False (некорректная дата).
"""

stream = ['2018-04-02', '2018-02-29', '2018-19-02']

for i in stream:
    try:
        datetime.strptime(i, '%Y-%m-%d')
        print(i, 'True')
    except:
        print(i, 'False')

"""## Задание 3
Напишите функцию date_range, которая возвращает список дат за период от start_date до end_date. 
Даты должны вводиться в формате YYYY-MM-DD. 
В случае неверного формата или при start_date > end_date должен возвращаться пустой список.
"""

from datetime import timedelta

def date_range():
    start_date = input('start_date ')
    end_date = input('end_date ')
    datediff = []

    try:
        start_date_dt = datetime.strptime(start_date,'%Y-%m-%d') + timedelta(days=-1)
        end_date_dt = datetime.strptime(end_date,'%Y-%m-%d')

        while start_date_dt < end_date_dt:
            start_date_dt += timedelta(days = 1)
            datediff.append(datetime.strftime(start_date_dt,'%Y-%m-%d'))
        print(datediff)
    except:
        print(datediff)

date_range()