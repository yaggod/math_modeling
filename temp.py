import matplotlib.pyplot as plt
import numpy as np 
from math import sin,cos,pi
# F = -kv
# k = 6 pi*n*R
# n = вязкость 



def rad(degree):
    return degree*pi/180;
def tr_plot(v0 = 100, angle = 90, all_time = 100, t_int = 5,Radius = 1, n_vz = 1,mass = 50):
    
    k = 6*pi*Radius*n_vz
    amout = int(all_time/t_int)
    
    vx = v0*cos(rad(angle))
    vy = v0*sin(rad(angle))
    for i in range(1,amout):
       
    
    
    
    
    plt.plot([0,vx],[0,vy])
    plt.show()
    
    
    
tr_plot()