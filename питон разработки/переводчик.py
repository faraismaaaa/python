c=[]
a="Я люблю чай"
b={"Я":"I" ,
   "люблю": "love" ,
   "чай": "tea"}
a=a.split()
print(a)

for i in a :
    c.append(b[i])
print(" ".join(c))
