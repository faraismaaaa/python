q=1
a=input("Введите строку " )
b=input("Какое слово выберишь? ")
if q!=0:
    nao=b[: :-1]
    dlina=len(b)
    x=a.replace(b,nao)

print(dlina)
print(nao)
print(a*dlina)
print(x)
