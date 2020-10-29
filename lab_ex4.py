import numpy as np
def Fnc(mn=0,mx=5,col=6):
    a=np.linspace(mn,mx,col)
    b=np.zeros(shape=(col))
    for i in range(0,col,1):
       b[i]=(a[i])**2
    print(a,'- ось Х\n',b,'- ось Y',sep='')
a=int(input("Минимальное значение "))
b=int(input("Максимальное значение "))
c=int(input("Количество значений "))
Fnc(a,b,c)
