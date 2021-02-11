from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt






t = np.arange(1,5,1);

def repSpeed(m, t):
    return k * m

k = 1.1

m0 = 5   #int(input("Начальное количество: "))
solve_Bi = odeint(repSpeed, m0, t)

plt.plot(t, solve_Bi[:,0], label='Размножение бактерий')
plt.show()
#print(solve_Bi)
