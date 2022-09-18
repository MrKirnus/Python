# -*- coding: utf-8 -*-


documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

#Пункт 1. Пользователь по команде "p" может узнать владельца документа по его номеру
def p():
    a = input('Введите номер документа: ')
    for i in documents:
        if a == i['number']:
            print(f"Владелец документа: {i['name']}")
            break
    else:
        print('Документ не найден в базе')

#Пункт 2. Пользователь по команде "s" может по номеру документа узнать на какой полке он хранится
def s():
    b = input('Введите номер документа: ')

    for key, value in directories.items():
        if b in value:
            print(f'Документ хранится на полке: {key}')
            break
    else:
        print('Документ не найден в базе')

#Пункт 3. Пользователь по команде "l" может увидеть полную информацию по всем документам
def l():
    for i in documents:
        for k, v in directories.items():
            for p in v:
                if i['number'] == p:
                   i[4]= k
        print('№:', i['number'], 'тип:', i['type'], 'владелец:', i['name'], 'полка хранения:', i[4])

#Пункт 4. Пользователь по команде "ads" может добавить новую полку
def ads():
    n = input('Введите номер полки: ')

    for k, v in directories.items():
        if n == k:
            print(f'Такая полка уже существует. Текущий перечень полок: {[k for k,v in directories.items()]}')
            break
    else:
        directories[n] = []
        print(f'Полка добавлена. Текущий перечень полок: {[k for k,v in directories.items()]}')

#Пункт 5. Пользователь по команде "ds" может удалить существующую полку из данных (только если она пустая)
def ds():
    del_polka = input('Выберете номер полки: ')

    if del_polka in directories:
            if len(directories[del_polka]) > 0:
                print('На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: ' + ', '.join(directories.keys()))
            else:
                del directories[del_polka]
                print('Полка удалена. Текущий перечень полок: ' + ', '.join(directories.keys()))
    else:
            print('Такой полки не существует. Текущий перечень полок: ' + ', '.join(directories.keys()))
ds()

print('p - узнать владельца документа по его номеру')
print('s - по номеру документа узнать на какой полке он хранится')
print('l - увидеть полную информацию по всем документам')
print('ads - добавить новую полку')
print('ds - удалить существующую полку из данных (только если она пустая)')
print('q - выход')
def main():
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            p()
        elif command == 's':
            s()
        elif command == 'l':
            l()
        elif command == 'ads':
            ads()
        elif command == 'ds':
            ds()
        elif command == 'q':
            break

main()