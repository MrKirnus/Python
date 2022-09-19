# -*- coding: utf-8 -*-
"""ДЗ. Библиотека Pandas.ipynb

### Задание 1
Скачайте с сайта grouplens.org...movielens/ датасет любого размера. Определите, какому фильму было выставлено больше всего оценок 5.0.
"""

import pandas as pd

rating = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

data_five = rating[(rating['rating'] == 5.0)]

df_merge = data_five.merge(movies, left_on = 'movieId', right_on = 'movieId', how = 'inner')

df_merge.groupby(['movieId' , 'title'])['movieId'].count().sort_values(ascending = False).head(1)

# скриншот из анаконды с итоговым результатом
from IPython.display import Image
Image("скриншот из анаконды.png")

"""### Задание 2
По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 года. Не учитывайте в расчетах отрицательные значения quantity.
"""

df = pd.read_csv('power.csv')
df.head()

baltic_states = df[(df['country'] == 'Latvia') | (df['country'] == 'Lithuania') | (df['country'] == 'Estonia') ]
# Можно ли как-то сразу указать список каких параметров оставить? Видел пример с методом .isin(), но до конца так и не понял как он работает
b_s_c = baltic_states[(baltic_states['category'] == 4) | (baltic_states['category'] == 12) | (baltic_states['category'] == 21)]
b_s_c_y = b_s_c[(b_s_c['year'] > 2005) & (b_s_c['year'] < 2010) & (b_s_c['quantity'] > 0)]

print(f'Суммарное потребление стран Прибалтики: {b_s_c_y["quantity"].sum()}')

"""### Задание 3
Выберите страницу любого сайта с табличными данными. Импортируйте таблицы в pandas dataframe.
Примеры страниц (необязательно брать именно эти):
https://fortrader.org/quotes
www.finanz.ru...om-vremeni
"""

page_url = 'https://tradingeconomics.com/commodity/crude-oil'

# Oil price
df = pd.read_html(page_url, attrs = {'class': 'table table-condensed'})
df[:5]