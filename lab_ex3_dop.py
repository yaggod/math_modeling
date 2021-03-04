def Lens(typ,dist,foc):
    if (typ==1):
        return str("Уменьшенное, мнимое, прямым")
    elif (typ==2):
        if (dist==foc):
            return str("Нету изображения")
        elif(dist<foc):
            return str("Увеличинное, мнимое, прямое")
        elif(foc<dist<(2*foc)):
            return str("Уменьшенное, действительное, обратное")
        elif(dist==(2*foc)):
            return str("Равное, действительное, перевернутое")
        elif(dist>(2*foc)):
            return str("Уменьшенное, действительное, перевернутое")
        else:
            return str("Неправильное значение")
    else:
        return str("Неправильное значение")  
t=d=f=0
print("Какого вида ваша линза?")
while (t !=1) and (t != 2):
    t=int(input("1)Рассеивающая\n2)Собирающая\n"))
while (d <=0):
    d=float(input("Введите расстояние до предмета "))
print("")
if (t==1):
    while (f>=0):
        f=float(input("Введите фокусное расстояние линзы "))
else:
    while (f<=0):
        f=float(input("Введите фокусное расстояние линзы "))
print(Lens(t,d,f))