#функция int() возвращает целое число в десятичной системе счисления (класс int).тип переменой
a = int(input('Введите число '))
while b<0:
        if a == 0:
                print('Не понял')
        elif  a % 2 == 0:
                print('Число четно')
        elif a % 2>0:
                print('Число не четное')
        else:
                print("не понял")
b=int(input('продолжим? '))
if b>=1 :print ('пока'); break 
