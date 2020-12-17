import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
obj, = plt.plot([],[],'o',color='r',label='Ball')
x, y = [],[]

R = float(input("Введите R "))
def cicloid(i):
    x.append(R*i - R*np.sin(i))
    y.append(R - R*np.cos(i))
    obj.set_data(x,y)
    
def astroid(i):
    x.append(R*(np.cos(i) ** 3))
    y.append(R*(np.sin(i) ** 3))
    obj.set_data(x,y)
    
    
edge = 10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
a = input("Какой график:\n1)Циклоида\n2)Астроида\n")
if (a=="1"):
    print("fasj")
    ani = FuncAnimation(fig, cicloid, frames=np.arange(-0,10,0.1), interval = 67)
    print(type(ani))
elif (a=="2"):
    ani = FuncAnimation(fig, astroid, frames=np.arange(-1,1,0.001), interval = 67)
else:
    exit()


ani.save("skfks.gif",writer = "pillow")
print("done")