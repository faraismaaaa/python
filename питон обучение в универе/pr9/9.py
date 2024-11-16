# x = int(input())
#
# def func(x):
#     if 3 < x <=6:
#         return (x/(3*x-4))
#     elif x>6:
#         return ((4**(-3*x))+4)
#     else:
#         if (2-x)!=0:
#             return (x**3) - ((2-x)**(1/5))
# print(round(func(x),12))


def find(zn):
    result = 0.0
    for i in range(1,zn+1):
        result += (1.0/i)
    return result
x = float(input())
zn = 1
while (find(zn)<=x):
    zn+=1
print(zn)

from math import sin
b = float(input())
c=0
x=-3
while x<=1.0:
    y = (sin(b*x)*(2**(-(x+3))))/(5-(x+4)**0.5)
    if y>0:
        c+=1
    x+=0.5
print(c)

x = int(input())

def func(x):
    if 3 < x <= 6:
        return (x/(3*x-4))
    elif x>6:
        return ((4**(-3*x))+4)
    else:
        if (2-x)!=0:
            return ((x**3) - ((2-x)**(1/5)))
print(round(func(x),12))