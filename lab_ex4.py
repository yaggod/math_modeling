import numpy as np
from numpy import sin, cos
from scipy.integrate import odeint
import matplotlib.pyplot as plt



t = np.arange(-5,5,0.01)
def func(a, t):
    w, y = a
    dy_dt = w
    dw_dt = -4*w - 5*y
    return  dw_dt,dy_dt
    
    
y0 = 4
w0 = -1
cort =  w0,y0

solution = odeint(func, cort, t)
plt.plot(t,solution)
plt.show()



