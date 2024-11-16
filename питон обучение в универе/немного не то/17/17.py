import csv
from os import listdir

def start():
    print('=======================')
    print(f'Открыть файл или создать новый?\n'
          '=======================\n'
          f'1. Открыть\n'
          f'2. Создать')
    print('=======================')
    select = 'null'
    while select.isdigit() == False or int(select) > 2:
        select = input('Выбор пункта меню: ')
    if select == '1':
        select_file()
    elif select == '2':
        main()
def select_file():
    print('=======================\n'
          'Какой файл хотите открыть?\n'
          '=======================')
    file_id = 0
    for x in listdir():
        file_id += 1
        print(f'{file_id}) {x}')
    print('=======================')
    select = int(input('Выбор пункта меню: '))
    open_file(listdir()[select-1])
def open_file(filename):
    with open(filename, "r", encoding="utf8", newline="") as file:
        for line in list(csv.reader(file,delimiter=';')):
            glossary[line[0]] = line[1]
    main()
def print_glossary():
    for element in glossary.items():
        print(*element, sep=" - ")
def add_data():
    termin = input("Введите термин: ")
    oprdel_termin = input("Введите определение: ")
    glossary[termin] = oprdel_termin
    return "Запись добавлена!"
def remove_data():
    termin = input('Какой термин будем удалять?: ')
    glossary.pop(termin)
    return f'Термин {termin} успешно удален!'
def edit_data():
    termin = input('Какой термин будем менять?: ')
    data = input('Введите новое определение: ')
    glossary[termin]=data
    return f'Данные для термина {termin} успешно изменены!'
def find_data():
    termin = input('Какой термин будем искать?: ')
    if termin in glossary:
        return f'{termin} — {glossary[termin]}'
    else:
        return f'Термин {termin} не найден!'
def save_to_file():
    filename=input('Имя файла: ')
    with open(filename+'.csv', "w", encoding="utf8", newline="") as file:
        write = csv.writer(file, delimiter=";")
        for item in glossary.items():
            write.writerow(item)
    return f'Глоссарий сохранен под названием {filename}.csv'
def main():
    while True:
        text = "Выбор пункта меню: "
        print('\n=======================')
        print('0. Сохранить глоссарий\n'
              '1. Вывести глоссарий\n'
              '2. Дополнить глоссарий\n'
              '3. Поиск в глоссарии\n'
              '4. Редактировать глоссарий\n'
              '5. Удалить термин из глоссария\n'
              '6. Выход')
        print('=======================')
        menu = 'null'
        while menu.isdigit() == False or int(menu) > 6 and int(menu)<=0:
            menu = input(text)
        if menu == '0':
            print(save_to_file())
        elif menu == '1':
            print_glossary()
        elif menu == '2':
            print(add_data())
        elif menu == '3':
            print(find_data())
        elif menu == '4':
            print(edit_data())
        elif menu == '5':
            print(remove_data())
        elif menu == '6':
            while True:
                print('Сохранить изменения? (y/n)')
                answer = input()
                if answer == 'y':
                    print(save_to_file())
                    break
                elif answer == 'n':
                    break
                else:
                    continue
            print('exit')
            break
if __name__ == '__main__':
    glossary = {}
    start()