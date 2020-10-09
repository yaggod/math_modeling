num=int(input("Введите значение "))
sp=[2,3]
res=[]
true=bool(True)
for n in range(5,num+1,1):
    for i in sp:
        if n%i==0:
            true=False
            break
    if true==True:
        sp.append(n)
    true=True
for i in sp:
    if num%i==0:
        res.append(i)
print("Список всех простых чисел до",num,"-",sp,"из которых",num,"делится на",res)