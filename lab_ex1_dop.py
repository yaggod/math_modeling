import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(-0.5,0.5,0.02)

def func(a,t):
    x, y, z = a
    dx_dt = 3*x - y + z
    dy_dt = x + y + z
    dz_dt = 4*x - y + 4*z
    return dx_dt, dy_dt, dz_dt;



x0 = -71
y0 = 1
z0 = -3

crt = x0, y0, z0

solution = odeint(func, crt, t);


plt.plot(t, solution)
plt.show()
