from os import system
from random import randint as rnd


def cls():
    system('cls')
def create_mas(n):
    global ls
    ls = [rnd(-100, 100) for i in range(n)]
def main():
    cls()
    text = "Выбор пункта меню: "
    print('\n=======================')
    print('0. Заполнить массив новыми, случайными значениями\n'
          '1. Вывести массив на экран\n'
          '2. Редактировать i-ый элемент массива\n'
          '3. Произведение ненулевых элементов массива, кратных 5\n'
          '4. Вывести отрицательные элементы на экран в обратном порядке\n'
          '5. Отсортировать массив методом выбора элементов и вывести отсортированный массив на экран\n'
          '6. Определить, есть ли в массиве два элемента сумма которых является четным числом\n'
          '7. Выход'
          )
    print('=======================')
    while True:
        menu = int(input(text))
        if menu==0:
            new_mas()
        elif menu==1:
            printmas()
        elif menu==2:
            replace()
        elif menu==3:
            multipe5()
        elif menu==4:
            reverseminus()
        elif menu==5:
            sortmas()
        elif menu==6:
            evenbytwo()
        elif menu==7:
            break
        print("exit")
def printmas(): # Выввод массива
    print(*ls)
    main()
def replace(): #Замена i-того элемента массива на x
    i = int(input('Элемент с каким индексом поменять?: '))
    x = int(input('На что меняем?: '))
    ls[i]=x
    print('Успешно!')
    main()
def multipe5(): #Произведение ненулевых элементов массива, кратных 5
    result = 1
    for i in range(len(ls)):
        if ls[i]%5==0 and ls[i]!=0:
            result*=ls[i]
    if result != 1:
        print(result)
    else:
        print('Таковых элементов в массиве нет!')
    main()
def reverseminus(): #Отрицательные элементы на экран в обратном порядке
    tmp = list(filter(lambda x: x < 0, ls))
    if tmp:
        print(tmp[::-1])
    else:
        print('В массиве отсутствуют отрицательные элементы!')
    main()
def sortmas(): #Методом выбора элементов и вывод
    tmp_sort = ls.copy()
    for i in range(len(tmp_sort) - 1):
        nMin = i
        for j in range(i + 1, len(tmp_sort)):
            if tmp_sort[j] < tmp_sort[nMin]:
                nMin = j
                if i != nMin:
                    tmp_sort[i], tmp_sort[nMin] = tmp_sort[nMin], tmp_sort[i]
    print(*tmp_sort)
    main()
def evenbytwo(): #Числа кратные двум
    flag = False
    for i in range(0, len(ls)):
        for j in range(i + 1, len(ls)):
            if (ls[i] + ls[j]) % 2 == 0 and (ls[i] + ls[j] != ls[i]) and (ls[i] + ls[j] != ls[j]):
               flag = True
    if flag:
        print('Да, имеются!')
    else:
        print('Таких чисел нет!')
    main()
def new_mas():
    create_mas(int(input('Введите размерность массива: ')))
    main()
while True:
    if __name__ == '__main__':
        new_mas()
        main()