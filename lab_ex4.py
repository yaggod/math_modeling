import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.linspace(0,100,2000)
def func(cort, t):
    m, y, v = cort
    dm_dt = -h
    dy_dt = v
    dv_dt = (d*h)/m - g
    return dm_dt, dy_dt, dv_dt





m0 = 25e4
d = 3e3 # км/3
h = 1e3 # т/с
g = 9.81
y0 = 0
v0 = 0

crt = m0, y0, v0



#plt.ylim(0,200)
sol = odeint(func, crt, t);
plt.plot(t,sol[:,1]); plt.show();
