from math import log
x = int(input('Введите число X: '))
def f(x):
    if x<=0:
        if x != -2:
            return x/x+2
    elif 0<x<=8:
        if x != 1:
            return (4**(-2*x)+3)/log(x)
    else:
        return x**2-(16-x)**1/3
print(f(x))