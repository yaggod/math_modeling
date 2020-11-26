import matplotlib.pyplot as plt
import numpy as np 


#           Парабола
def Parabola(name="Парабола",a=1,b=1,c=1,mn=-5,mx=5,amout=100):
    x = np.linspace(mn,mx,amout)
    y = a*(x**2)+b*x+c
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y=x^2")
    plt.title(name)
    plt.show  
#           Гипербола
def Hyperbola(name="Гипербола",mn=-5,mx=5,amout=100,k=5):
    x = np.linspace(mn,mx,amout)
    y = k/x
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y=k/x")
    plt.title(name)
    plt.show  
    
    
    