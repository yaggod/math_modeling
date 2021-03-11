import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.linspace(0,10,2147000);


def func(crt, t):
    global result
    vx,vy,x,y = crt;
    dvx_dt = (y/l)*g
    dvy_dt = (y/l) * g
    dx_dt = vx
    dy_dt = vy
    
    return dvx_dt,dvy_dt,dx_dt,dy_dt;




g = 9.81
l = 2.50
y0 = 0.1
x0 = 2.5
crt = 0, 0, x0, y0


sol = odeint(func,crt,t);
plt.plot(t, sol[:,3])
plt.ylim(0,2.5)
for i in range(len(sol)):
    if (sol[0:,3][i]>=2.5):
        res = t[i];
        break;
print(res);