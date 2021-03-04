import numpy
x=int(input("Введите длину массива: "))
m=numpy.zeros(shape=(x))
print(m)
for i in range(x-1):
    m[i]=input(f"Введи значение {i+1}-го элемента: ")
print(m)
a=int(input(f"Введи номер элемента: "))
b=int(input(f"Введи значение этогого элемента: "))
m=numpy.insert(m,a,b)
m=numpy.resize(m,x)
print(m)