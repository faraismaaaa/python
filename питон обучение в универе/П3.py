a=int(input('Введите число a '))
b=int(input('Введите число b '))
x=int(input('Введите число x '))
c=int(input('Введите число c '))
if a<0 and x!=0:
    cas=a*x**2+b**2*x
    print(cas)
elif a>0 and x==0:
    cas=x-a/(x-c)
    print(cas)
else:
    if c==0:
        print("На ноль делить нельзя!!!")
        cas=1+x/c
        print(cas)
###выдает ошибку при 0 5 4 0
