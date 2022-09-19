# -*- coding: utf-8 -*-
"""ДЗ. Библиотека numpy. Вычислительные задачи.ipynb

### Задание 1
Создайте numpy array с элементами от числа N до 0 (например, для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])).
"""

import numpy as np

from random import randint

np.arange(randint(1, 10), -1, -1)

"""### Задание 2
Создайте диагональную матрицу с элементами от N до 0. Посчитайте сумму ее значений на диагонали.
"""

arr = np.diag(np.arange(randint(1, 10), -1, -1))
print(arr)

res = 0
index = 0
for i in arr:
    res = res+i[index]
    index +=1
print()
print(f'Cумма значений по диагонали: {res}')

"""### Задание 3
Решите систему уравнений:

\begin{equation*}
\LARGE
4x + 2y + z = 4 \\
\LARGE
x + 3y = 12 \\
\LARGE
5y + 4z = -3
\end{equation*}
"""

a = np.array([[4, 2 ,1], [1, 3, 0], [0, 5, 4]])

b = np.array([4, 12, -3])

from numpy import linalg

linalg.solve(a, b)

"""### Задание 4"""

# Матрица в виде numpy array

users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ], 
    np.int32
)

# На сайт заходит очередной посетитель, о покупках которого известно следующее:

next_user_stats = np.array([0, 1, 2, 0, 0, 0])

"""Найдите самого похожего пользователя. Т. е. посчитайте косинусное сходство между этим пользователем и всеми пользователями из массива user_stats"""

def cosine( a, b ):
    """
    Подсчет косинуса угла между векторами a, b по их координатам
    """
    
    # длины векторов
    aLength = np.linalg.norm( a )
    bLength = np.linalg.norm( b )
    
    return np.dot( a, b ) / ( aLength * bLength )

user_cosiner = 0

for i in users_stats:
    if cosine(i, next_user_stats) > user_cosiner:
        user_cosiner = cosine(i, next_user_stats)
        
print(f'ID самого похожего пользователя: {[e+1 for e, i in enumerate(users_stats) if cosine(i, next_user_stats) == user_cosiner]}. Их косинусное сходство = {user_cosiner}')

# Или такой вариант

users_cosine = []

for i in users_stats:
    users_cosine.append(cosine(i, next_user_stats))
    
    
for e, i in enumerate(users_stats):
    if np.max(users_cosine) == cosine(i, next_user_stats):
        print(f'ID самого похожего пользователя: {e+1}, их косинусное сходство = {np.max(users_cosine)}')