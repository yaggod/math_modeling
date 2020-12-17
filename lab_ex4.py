import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
obj, = plt.plot([],[],'o',color='r',label='Ball')

x, y = [],[]

C = 0.3
D = 0.33

def xf(n):
    if n>0:
        return  (xf(n-1)**2) - (yf(n-1)**2) + C
    return 0.1


def yf(n):
    if n>0:
        return 2*xf(n-1)*xf(n-1) + D
    return 0.1
def func(n):
    print("\r\t\r", n)
    x.append( xf(n) )
    y.append( yf(n) )
    obj.set_data(x,y)


ani = FuncAnimation(fig, func, frames=np.arange(0,25,1), interval = 67)
ani.save("skfks.gif",writer = "pillow")
print("done")
