import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import sqrt


x = np.arange(1e-20,5,0.000001)

def func(a,x):
    y, w = a;
    dy_dx = w
    dw_dx = (w*w)/y - (3*y)/sqrt(x)
    return dy_dx, dw_dx 

y0 = 1e-20;
w0 = 1;

crt = y0, w0;

solution = odeint(func, crt, x);


plt.plot(x, solution[:,0])

plt.show()
