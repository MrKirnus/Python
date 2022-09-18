# -*- coding: utf-8 -*-
"""ДЗ Работа с файловой системой и модули.ipynb

## 1. Переведите содержимое файла purchase_log.txt в словарь purchases вида:
`
{‘1840e0b9d4’: ‘Продукты’, …}
`
"""

import json

purchase_dict={}

with open('purchase_log.txt', encoding = 'utf-8') as p_l:
    next(p_l) #пропускаем заголовок столбцов
    for i in p_l:
        i = i.strip() # удаляем лишние символы
        dict_ = json.loads(i) #переводим в json
        key=dict_['user_id']
        value=dict_['category']
        purchase_dict.setdefault(key,value)

i = 0
for k,v in purchase_dict.items():
    print(k,v)
    i +=1
    if i >10:
        break

"""##2. Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки (если покупка была, сам файл visit_log.csv изменять не надо). Запишите в файл funnel.csv визиты из файла visit_log.csv, в которых были покупки с указанием категории.
Учтите условия на данные:
содержимое purchase_log.txt помещается в оперативную память компьютера
содержимое visit_log.csv - нет; используйте только построчную обработку этого файла
"""

with open('visit_log.csv', 'r', encoding='utf-8') as v_l:
    with open('funnel.csv', 'w', encoding='utf-8') as funnel:

        for i in v_l:
            i_list = i.strip().split(',')
            p_d = purchase_dict.get(i_list[0])
            if p_d is not None:
                i_list.append(p_d)
                f = ','.join(i_list)
                funnel.write(f + '\n')