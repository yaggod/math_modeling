import numpy
n1=n2=3
n1=int(input('Введите "высоту": '))
n2=int(input('Введите "ширину": '))
m1=numpy.zeros(shape=(2,n1,n2))
for (x1,x2,x3),x4 in numpy.ndenumerate(m1):
    m1[x1,x2,x3]=input(f'Введите значение {x1+1}-го массива, {x2+1}-го по высоте и {x3+1}-го по ширине значения ')
print("Начальный массив:\n",m1)
m2=numpy.zeros(shape=(n1,n2))
for i in range(n1):
    for n in range(n2):
        if m1[0,i,n]>=m1[1,i,n]:
            m2[i,n]=m1[0,i,n]
        else:
            m2[i,n]=m1[1,i,n]
print("Результат:\n",m2)
