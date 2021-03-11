import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.linspace(0,10,1000000)

def func(crt, t):
    
    vx, vy, x, y = crt;
    dvx_dt = -meow*vx*np.abs(vx) / m 
    dvy_dt = -(g + meow*vx*np.abs(vy) / m)
    dx_dt = vx
    dy_dt = vy
    return dvx_dt, dvy_dt, dx_dt, dy_dt;
    
    
    
    

m = 50;

angle = np.pi / 4;
v0 = 50;
vy0 = np.sin(angle) * v0;
vx0 = np.cos(angle) * v0;

g = 9.81;

meow = 1.023456789

x0 = y0 = 0

crt = vx0, vy0, x0, y0

sol = odeint(func, crt, t);
plt.plot(sol[:,2],sol[:,3]);
plt.ylim(0)
plt.show();