import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from time import sleep

plt.autumn()
#i = 0;
ms = []
x = np.arange(-0.9999999999,1.5,1e-5)

def func(a,x):
#    global i;
#    print(i)
    y, w = a
    dy_dx = w
    dw_dx = (3*x*w - i*(i+2)*y)/(1-x*x)
    return dy_dx, dw_dx



y0 = 3
w0 = 0
for i in range(0,6):
#    sleep(1);
#    i = k
    crt = y0, w0
    ms.append(odeint(func, crt, x))
    
for sol in ms:
    plt.plot(x,  sol[:,0])
#   
plt.ylim(-2, 2)
#plt.xlim(-7,5)

plt.show()
