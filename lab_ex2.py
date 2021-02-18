import numpy as np
from numpy import exp
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1,1,0.01);

def func(a, t):
    x, y = a;
    dx_dt = 3*x - 2*y + (exp(3*t))/(exp(t) + 1);
    dy_dt = x - exp(3*t)/(exp(t)+1);
    return dx_dt, dy_dt;

crt = 5, -7;
solution = odeint(func, crt, t);

plt.plot(t, solution);