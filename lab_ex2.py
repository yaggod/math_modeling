from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt






t = np.arange(0,10,0.001);

def repSpeed(money, t):
    return -k * money * t

k = 0.08

money0 = 1000 #int(input("Начальное количество: "))
solve_Bi = odeint(repSpeed, money0, t)

plt.plot(t, solve_Bi[:,0], label='Размножение бактерий')
plt.show()
#print(solve_Bi)



#k * money(t) = dmoney / dt


