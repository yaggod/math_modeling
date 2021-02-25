import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import sqrt



t = np.arange(0,3,1e-5)

def func(a,t):
    y,w = a
    dy_dt = w 
#    dw_dt = (1 - w**2)**1/2 
    dw_dt = sqrt(1 - w**2)
    return dy_dt, dw_dt


w0 = 0
y0 = 3

crt = y0, w0

solution = odeint(func, crt, t);


plt.plot(t, solution)
plt.show()
    

print(solution);

