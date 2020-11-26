import matplotlib.pyplot as plt
import numpy as np

x = np.zeros(shape = 5)
y = np.zeros(shape = 5)
print("¬ведите первую координату:", sep='')
x[0] = input("ќсь X ")
y[0] = input("ќсь Y ")
a = float(input("¬ведите размер стороны: ",))
x = [x[0],x[0]+a,x[0]+a,x[0],x[0]]
y = [y[0],y[0],y[0]+a,y[0]+a,x[0]]

plt.plot(x,y)
plt.show