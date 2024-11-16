from random import randint as rnd

def create_mas(n,m):
    ls = []
    for i in range(n):
        ls.append( [0]*m)
    for i in range(n):
        for j in range(m):
            ls[i][j]= rnd(-50,50)
    return ls


def main():
    n, m = map(int, input('Размерность массива NxM: ').split())
    arr = create_mas(n, m)
    while True:
        text = "Выбор пункта меню: "
        print('\n=======================')
        print('0. Заполнить массив новыми, случайными значениями\n'
              '1. Вывести массив на экран\n'
              '2. Редактировать элемент двумерного массива\n'
              '3. Найти максимальный элемент двухмерного массива среди элементов кратных 7\n'
              '4. Поиск в массиве\n'
              '5. Определить, есть ли в двумерном массиве строка (столбец), состоящих из элементов больших определенного числа\n'
              '6. Выход'
              )
        print('=======================')
        menu = 'null'
        while menu.isdigit() == False or int(menu)>6:
            menu = input(text)
        int(menu)
        if int(menu) == 0:
            arr = create_mas(n, m)
        elif int(menu) == 1:
            printmas(arr)
        elif int(menu) == 2:
            edit_mas(arr,n,m)
        elif int(menu) == 3:
            maxevenby7(arr)
        elif int(menu) == 4:
            find(arr,n,m)
        elif int(menu) == 5:
            maxbyinput(arr,m)
        elif int(menu) == 6:
            break
    print("exit")

def printmas(ls):
    for x in ls:
        print(*list(map('{{:>4d}}'.format().format, x)))

def edit_mas(ls,n,m):
    i = j = n+1
    while i>n and j>m:
        i, j = map(int, input('Индексы элемента:').split())
    x = int(input('На что меняем? '))
    ls[i-1][j-1]=x

def maxevenby7(ls):
    tmp = []
    for row in ls:
        for col in row:
            if col%7==0:
                tmp.append(col)
    print(max(tmp))

def find(ls,n,m):
    count_x=-1
    count_y=-1
    tmp = []
    for row in range(0,n,2):
        for col in range(1,m,2):
            if ls[col][row]%2!=0 and ls[col][row]>0:
                tmp.append(ls[col][row])
    x = max(tmp)
    for x1 in ls:
        count_x+=1
        for x2 in x1:
            count_y+=1
            if x2>x:
                print('{}[{},{}]'.format(x2,count_x,count_y))
def maxbyinput(ls,m):
    x = int(input('Элементы больше какого числа выводить?: '))
    total_row = 0
    total_col = 0
    for x1 in ls:
        tmp_count_row = 0
        for x2 in x1:
            if x2 > x:
                tmp_count_row +=1
        if tmp_count_row == m:
            total_row+=1
    if total_row != 0:
        print(total_row)
    else:
        print('Таковых строк нет!')

    for x1 in range (0,len(ls)):
        tmp_count_col = 0
        for x2 in range(0,m):
            if ls[x2][x1] > x:
                tmp_count_col +=1
        if tmp_count_col == len(ls):
            total_col+=1
    if total_col != 0:
        print(total_col)
    else:
        print('Таковых столбцов нет!')

if __name__ == '__main__':
    main()