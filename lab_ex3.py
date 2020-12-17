import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
obj, = plt.plot([],[],'o',color='r',label='Ball')

x, y = [],[]



def rad(degree):
    return degree*np.pi/180;

def sin(a):
    return np.sin(rad(a))

def cos(a):
    return np.cos(rad(a))
def babochka(t):
    ur = exp(cos(t)) -2*cos(4*t) + (sin(t/12)**5)
    x.append(sin(t) * ur)
    y.append(cos(t) * ur)
    obj.set_data(x,y)

def hearth(t):
    x.append(16*(sin(t) ** 3))
    y.append(13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t))
    obj.set_data(x,y)
    
    
    
    
    plt.axis('equal')

    	
a = int(input("Какой график:\n1)Бабочка\n2)Сердце"))
if (a==1):
    z = 5
    ax.set_xlim(-z, z)
    ax.set_ylim(-z, z)
    ani = FuncAnimation(fig, babochka, frames=np.arange(-0,12*np.pi,0.1), interval = 35 )
elif (a==2):
    ani = FuncAnimation(fig, hearth, frames=np.arange(0,2*np.pi,0.1), interval = 35 )
    z = 20
    ax.set_xlim(-z, z)
    ax.set_ylim(-z, z)
else:
    exit()

    


ani = FuncAnimation(fig, hearth, frames=np.arange(-200,200,2), interval = 35 )
ani.save("skfks.gif",writer = "pillow")
print("done")