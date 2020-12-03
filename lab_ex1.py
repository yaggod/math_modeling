import matplotlib.pyplot as plt
import numpy as np

x = np.zeros(shape = 5)
y = np.zeros(shape = 5)
print("Введите начальные координаты:", sep='')
x[0] = input("Ось X ")
y[0] = input("Ось Y ")
a = float(input("Введите размер стороны: ",))
x = [x[0],x[0]+a,x[0]+a,x[0],x[0]]
y = [y[0],y[0],y[0]+a,y[0]+a,x[0]]

plt.plot(x,y)
plt.show
