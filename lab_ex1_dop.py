import matplotlib.pyplot as plt
import numpy as np
import math
import random

def LissExp1(B=1,A=1,a=2,b=3,mn=-10,mx=10,amout=1000,beta = math.pi/2):
    t = np.linspace(mn,mx,amout)
    t1 = np.linspace(mn,mx,amout)
    #beta = math.pi/2
    

    x =  A*(np.sin(a*t + beta))
    y = B*(np.sin(b*t))
    a = plt.plot(x,y)
    plt.show()

a = random.randint(-10,0)
b = random.randint(-10,0)
print(a,b)


i=1
while (True):
  LissExp1(beta=(2*np.pi*50)/(i*10),a=a,b=b)
  i = i+1
