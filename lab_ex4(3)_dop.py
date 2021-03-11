import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.linspace(0,10,1000);


def func(crt, t):
    global result
    vx,vy,x,y = crt;
    if(y/l>=1):
        if(t<result): result = t;
    dvx_dt = (y/l)*g
    dvy_dt = (y/l) * g
    dx_dt = vx
    dy_dt = vy
    
    return dvx_dt,dvy_dt,dx_dt,dy_dt;



result = 1e308
g = 9.81
l = 2.50
y0 = 0.1
x0 = 2.5
crt = 0, 0, x0, y0


sol = odeint(func,crt,t);
plt.plot(t, sol[:,3])
plt.ylim(0,2.5)
print(result)
