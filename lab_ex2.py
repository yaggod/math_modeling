import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
obj, = plt.plot([],[],'o',color='r',label='Ball')

x = np.arange(-180,180,1)
y = np.arange(-180,180,1)



def rad(degree):
    return degree*np.pi/180;

def circlepainter(r):
    x_coord = r*x
    y_coord = r*y
    obj.set_data(x_coord,y_coord)
    
    
            
    
x = np.sin(rad(x))
y = np.cos(rad(y))
    	


plt.axis('equal')
ax.set_xlim(-50,50)
ax.set_ylim(-50,50)
    


ani = FuncAnimation(fig, circlepainter, frames=np.arange(0,10,0.2), interval = 35 )
ani.save("skfks.gif",writer = "pillow")
print("done")