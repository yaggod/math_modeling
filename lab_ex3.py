import numpy as np
from lab_ex1 import g
a=np.linspace(0,5,6)
x0=float(input("Начальная координата по оси X "))
y0=float(input("Начальная координата по оси Y "))
v0=float(input("Начальная скорость стела "))
b=np.zeros(shape=(6,3))
print(b)


for (i),j in np.ndenumerate(a):   # J номер I значение
    b[i,0]=j
    b[i,1]=x0+v0*j
    b[i,2]=y0+v0*j-(g*j*j)/2
print(b)