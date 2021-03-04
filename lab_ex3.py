import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.linspace(0,100,200)
def func(cort, t):
    v, y = cort
    dy_dt = v
    dv_dt = ( k* -y)/m
    if type == 1:
        dv_dt -= 0.8 * v
    elif type == 2:
        dv_dt += 5 * np.cos(w*t)
    elif type == 3:
        dv_dt -= 0.8 * v
        dv_dt += 5 * np.cos(w*t)
    return dv_dt, dy_dt

g = 9.81
y0 = 0
v0 = 0.5 
dl = 0.08
k = 0.125
y0 = - dl
m = 0.5

crt = v0, y0


type = 42;
while(type<0 or type>3):
    type = int(input("Вариант задачи:\n0)Без сил сопротивления\n1)F = -0.8mv\n2)F = 5cos(w*t)\n3)1 и 2\n"))

    
if (type == 2 or type == 3): w = int(input("Коэффициент w: "))
#plt.ylim(-0.02,0.02)
sol = odeint(func, crt, t);
plt.plot(t,sol[:,1]); plt.show();

