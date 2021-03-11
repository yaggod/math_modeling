import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.linspace(0,10,1000)

def func(crt, t):
    A, B, C = crt
    db_dt = A * k1 - B * k2
    dc_dt = B * k2 - k3 * C
    da_dt = -db_dt
    return da_dt, db_dt, dc_dt;
    
    
    
    
A0 = 1000;
B0 = 0;
C0 = 0;


k1 = 0.28;
k2 = 0.06
k3 = 0.3


crt = A0, B0, C0;
sol = odeint(func, crt, t);
plt.plot(t, sol);
plt.show();