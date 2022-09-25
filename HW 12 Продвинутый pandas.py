# -*- coding: utf-8 -*-
"""ДЗ. Продвинутый pandas.ipynb

### Задание 1

Для датафрейма log из материалов занятия создайте столбец source_type по следующим правилам:

если источник traffic_source равен yandex или google, то в source_type ставится organic
для источников paid и email из России - ставим ad
для источников paid и email не из России - ставим other
все остальные варианты берем из traffic_source без изменений
"""

import pandas as pd

log = pd.read_csv('visit_log.csv', sep = ';')
log.head()

log.loc[(log.traffic_source == 'yandex') | (log.traffic_source == 'google'), 'source_type'] = 'organic'
log.loc[((log.traffic_source == 'paid') | (log.traffic_source == 'email')) & (log.region=='Russia'), 'source_type'] = 'ad'
log.loc[((log.traffic_source == 'paid') | (log.traffic_source == 'email')) & (log.region!='Russia'), 'source_type'] = 'other'
log.loc[log.source_type.isnull(), 'source_type']=log['traffic_source']
log.head(15)

"""### Задание 2

В файле URLs.txt содержатся url страниц новостного сайта. Вам необходимо отфильтровать его по адресам страниц с текстами новостей. Известно, что шаблон страницы новостей имеет внутри url следующую конструкцию: /, затем 8 цифр, затем дефис. Выполните следующие действия:

Прочитайте содержимое файла с датафрейм
Отфильтруйте страницы с текстом новостей, используя метод str.contains и регулярное выражение в соответствии с заданным шаблоном
"""

import re

urls = pd.read_csv('URLs.txt')
urls.head()

urls[urls.url.str.contains('/[0-9]{8}-', regex=True)].head()

"""### Задание 3

Используйте файл с оценками фильмов ml-latest-small/ratings.csv. Посчитайте среднее время жизни пользователей, которые выставили более 100 оценок. Под временем жизни понимается разница между максимальным и минимальным значением столбца timestamp для данного значения userId.
"""

ratings = pd.read_csv('ratings.csv')
ratings.head()

ratings_count = ratings[['userId','rating']].groupby('userId').count().reset_index()
ratings_count = ratings_count[ratings_count['rating'] > 100]
ratings_count.head()

rating_max = (ratings
            .rename(columns = {'timestamp': 'timestamp_max'})[['userId','timestamp_max']]
            .groupby('userId')
            .max()
            .reset_index())


rating_min = (ratings
              .rename(columns = {'timestamp': 'timestamp_min'})[['userId','timestamp_min']]
              .groupby('userId')
              .min()
              .reset_index())

lifetime = ratings_count.merge(rating_max, how = 'inner').merge(rating_min, how = 'inner')

lifetime['avg'] = lifetime['timestamp_max'] - lifetime['timestamp_min']
lifetime.head()

"""### Задание 4

Дана статистика услуг перевозок клиентов компании по типам (см. файл “Python_13_join.ipynb” в разделе Материалы для лекции «Продвинутый pandas» ---- Ноутбуки к лекции «Продвинутый pandas»).

Необходимо сформировать две таблицы:
- таблицу с тремя типами выручки для каждого client_id без указания адреса клиента
- аналогичную таблицу по типам выручки с указанием адреса клиента

Обратите внимание, что в процессе объединения таблиц данные не должны теряться.
"""

rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)
rzd

auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)
auto

air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)
air

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1', 
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)
client_base

"""#### Таблица с тремя типами выручки для каждого client_id без указания адреса клиента"""

revenue = rzd.merge(auto, how = 'outer', on = 'client_id')
revenue = revenue.merge(air, how = 'outer', on = 'client_id')
revenue.fillna(0)

"""#### Аналогичная таблица по типам выручки с указанием адреса клиента"""

client_revenue = revenue.merge(client_base, how='outer', on='client_id')
client_revenue.fillna(0)