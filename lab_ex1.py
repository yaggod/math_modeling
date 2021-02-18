import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.001);
print(x)
def func(a, x):
    y, z = a
    dy_dx = y*y*z
    dz_dx = z/x - y*z*z
    return dy_dx, dz_dx


crt = 1, -3
solution = odeint(func, crt, x);


plt.plot(x, solution[:,1])
plt.show();


