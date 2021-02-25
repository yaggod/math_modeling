import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt



x = np.arange(-1,1,1e-5)

def func(a,x): 
    y,w = a
    dy_dx = w
    dw_dx = (-x*w + (4*x*x + 1/2)*y)/(x*x)
    return dy_dx, dw_dx


w0 = 0
y0 = 3

crt = y0, w0

solution = odeint(func, crt, x);
plt.ylim(-5, 100)

plt.plot(x, solution)
plt.show()
    
print(type(solution[0,1 ]))
