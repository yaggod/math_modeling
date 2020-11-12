import numpy as np
from math import sin
n=int(input("Введите высоту массива "))
m=int(input("Введите длину массива "))
a=np.zeros(shape=(n,m))

for (i,j),x in np.ndenumerate(a):
    a[i,j]=sin(n*(i+1)+m*(j+1))
    if a[i,j]<0:
        a[i,j]=0
print(a,"\n"*5)
n1=int(input("Какую строку вы хотите взять "))
n2=int(input("С какой заменить "))
b=np.zeros(shape=(2,n))
n1 -=1
n2 -=1
a=a.T
b[0]=a[n1-1]
b[1]=a[n2-1]
a[n1-1]=b[1]
a[n2-1]=b[0]
print(a.T)
