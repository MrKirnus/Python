# -*- coding: utf-8 -*-
"""ДЗ. Функции и работа с данными.ipynb

### Задание 1
Напишите функцию, которая классифицирует фильмы из материалов занятия по следующим правилам:
- оценка 2 и меньше - низкий рейтинг
- оценка 4 и меньше - средний рейтинг
- оценка 4.5 и 5 - высокий рейтинг

Результат классификации запишите в столбец class
"""

import pandas as pd

rating = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

df_merge = rating.merge(movies, left_on='movieId', right_on='movieId', how='inner' )

def class_movie(row):
    
    if row['rating'] <= 2:
        return('Низкий рейтинг')
    
    elif (row['rating'] > 2) & (row['rating'] <= 4):
        return('Средний рейтинг')
    
    return('Высокий рейтинг')

df_merge['class'] = df_merge.apply(class_movie, axis=1)
df_merge.head()

"""### Задание 2
Используем файл keywords.csv.

Необходимо написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность определенному региону. Т. е. если поисковый запрос содержит название города региона, то в столбце ‘region’ пишется название этого региона. Если поисковый запрос не содержит названия города, то ставим ‘undefined’.

Правила распределения по регионам Центр, Северо-Запад и Дальний Восток:
"""

keywords = pd.read_csv('keywords.csv')

def region(row):

    geo_data = {

    'Центр': ['москва', 'тула', 'ярославль'],

    'Северо-Запад': ['петербург', 'псков', 'мурманск'],

    'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
    
    }
    
    decoding = {}
    for k,v in geo_data.items():
        for i in v:
            decoding[i] = k
    
    for i in row['keyword'].lower().split(' '):
        if i in decoding.keys():
            return decoding[i]
    return('undefined')

keywords['region'] = keywords.apply(region, axis=1)
# keywords.head()
keywords[(keywords['region']!='undefined')]