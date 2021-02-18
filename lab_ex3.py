import numpy as np
from numpy import sin, cos
from scipy.integrate import odeint
import matplotlib.pyplot as plt



t = np.arange(-5,5,0.01)
def func(a, t):
    null, y = a
    dy_dt = null
    dw_dt = cos(t) + sin(t)
    return  dw_dt,dy_dt
    
    

cort = 0,3 

solution = odeint(func, cort, t)
plt.plot(t,solution)
plt.show()



