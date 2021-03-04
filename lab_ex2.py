import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.linspace(0,50,200)
def func(cort, t):
    A, x, y = cort
    dx_dt = A * k1
    dy_dt = A * k2
    da_dt = -(dy_dt + dx_dt)
    return da_dt, dx_dt, dy_dt


A0 = 1000
k1 = 0.1
k2 = 0.01
x0 = 0
y0 = 0

crt = A0, x0, y0

sol = odeint(func, crt, t);
plt.plot(t,sol); plt.show();