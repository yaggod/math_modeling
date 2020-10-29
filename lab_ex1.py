import numpy as np
def srar(a):
    b=int()
    for i in a:
        b=b+i
    return b/len(a)
    
a=int(input("Длина массива "))
b=np.zeros(shape=a)
for (i),a in np.ndenumerate(b):
    n=i[0]
    b[i]=input(f'Введите значение {n+1} элемента массива ')
print("Среднее арифметическое значений в массиве:",srar(b))