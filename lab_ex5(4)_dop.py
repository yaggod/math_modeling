import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.linspace(0,300,1000);


def func(crt, t):
    T1, T2 = crt;
    dt1_dt = a2*(Te - T1) + a1*(Tg-T1) + a3*(T2-T1);
    print(dt1_dt)
    if (dt1_dt < 0): dt1_dt +=v
    dt2_dt = a2*(Te-T1) + a3*(T1-T2);
    return dt1_dt, dt2_dt;



v = 5
a1 = 0.1
a2 = 0.02
a3 = 0.6
T1_0 = 273+20
T2_0 = 273-2
Tg = 273+20
Te = 273-10

crt = T1_0, T2_0
sol = odeint(func,crt,t);
plt.plot(t,sol-273)
