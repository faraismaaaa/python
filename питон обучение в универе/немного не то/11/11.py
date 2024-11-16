# from math import sqrt
# def height(a):
#     return a*sqrt(3)/2
# print('{:.3f}'.format(height(int(input('Введите длинну стороны a: ')))))


# from math import log, sin, cos, tan
#
# def from5to8(x):
#     if 3*(x**4)-((x+x**4)**1/5)!=0:
#         return log(3*(x**4)-((x+x**4)**1/5))*9**(x+5)
#     else:
#         return 'Mistake!'
# def from8to17(x):
#     if -1<=tan(x**3+4-(1/x**3))<=1:
#         return sin(tan(x**3+4-(1/x**3)))
#     else:
#         return 'Mistake!'
# def from17to19(x):
#     if -1<=x**2+1<=1:
#         if -1<=x**2-3<=1:
#             return cos(x**2+1)/(abs(sin(x**2-3)))**(1/3)
#         else:
#             return 'Mistake!'
#     else:
#         return 'Mistake!'
# def main(x):
#     if -5<=x<8:
#         return from5to8(x)
#     if 8<=x<17:
#         return from8to17(x)
#     if 17<=x<=19:
#         return from17to19(x)
# print(main(float(input('Введите x: '))))


from math import sin
def f(a,b,c):
    return (2*a-b-sin(c)+a*b)/(1+abs(c+a))
s, t = map(float, input('Введите числа s и t: ').split())
print(f(t,-2*s,1.17)+f(2.2,t,s-t))