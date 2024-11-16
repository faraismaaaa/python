print  ("""
        меню
1.сложение
2.Вывести строку
3.выход
""")
while True:
    x = int(input())
    if x == 3: print('пока'); break
    elif x == 1: print ()
    elif x == 2: print (input ('Введите слово '))
    else: print('Некорректный ввод')
    
    y = int(input("""Вы хотите продолжить?
1- да
0- нет
"""))
    if y == 0 :print ('пока');break
    if y == 1 : continue
    else: print  ("""
        меню
1.сложение
2.Вывести строку
3.выход
""")

