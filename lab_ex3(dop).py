from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt



dth = np.linspace(0, 2*np.pi,720)

L = 3.827E26
R = 6400e3
Vq = 30.4e3
q = 147e9



def dw_dth(w, th):
    return (L*R*R)/( 4 * q * Vq )


W = 0;
solve_Bi = odeint(dw_dth, W, dth)

plt.plot(dth, solve_Bi[:,0], label='Размножение бактерий')
plt.show()


    plt.plot([0,6],[0,5e24])
plt.show()

#print(solve_Bi)




#v dt = r dtheta

#dtheta = (v dt) / r

#dt = (r dtheta) / v

