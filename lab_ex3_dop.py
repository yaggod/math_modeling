res=[]
import numpy
larger=int()
xs=int(input("Введите высоту "))
ys=int(input("Введите ширину "))
m=numpy.zeros(shape=(xs,ys))
print("\n\n",m)
for (x,y),n in numpy.ndenumerate(m):
    m[x,y]=float(input(f'Введите значение {x+1}-го по высоте и {y+1}-го по ширине значения '))
print("\n",m)
m=m.T
for i in range(ys):
    for n in range(xs):
        if larger<m[i,n]:
            larger=m[i,n]
    res.append(larger)
    larger=int()
print(res)
