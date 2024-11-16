import csv
def main():
    while True:
        text = "Выбор пункта меню: "
        print('\n=======================')
        print('1. Новая запись\n'
              '2. Вывод\n'
              '3. Поиск по зарплате\n'
              '4. Выход'
              )
        print('=======================')
        menu = 'null'
        while menu.isdigit() == False or int(menu) > 4:
            menu = input(text)
        if menu == '1':
            print(write())
        elif menu == '2':
            for x in read():
                print(*x)
        elif menu == '3':
            find()
        elif menu == '4':
            break
    print('exit')
def read():
    with open('file.csv',encoding='utf-8') as file:
        return list(csv.reader(file,delimiter=';'))
def write():
    text = ['Фамилия', 'Инициалы', 'Занимаемая должность', 'Зарплата', 'Год поступления']
    data = []
    for x in text:
        tmp_data = input(x+': ')
        data.append(tmp_data)
    with open('file.csv',"a",encoding='utf-8',newline='') as file:
        csv_writer = csv.writer(file,delimiter=';')
        csv_writer.writerow(data)
    return 'Запись сохранена!'

def find():
    result = []
    value = input('Размер з/п: ')
    if not value.isdigit():
        print('Неверное значение!')
        find()
    with open('file.csv', encoding='utf8') as file:
        data = list(csv.reader(file,delimiter=';'))
        for x in data:
            if int(x[3]) >= int(value):
                result.append(x)
    if len(result) != 0:
        for x in result:
            print(x[0],x[1],x[3]+'у.е')
        print('Итого: {} записей.'.format(len(result)))
    else:
        print('Ничего не найдено!')


if __name__ == '__main__':
    main()