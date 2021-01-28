import matplotlib.pyplot as plt
import math
from math import pi
# F = -kv
# k = 6 pi*n*R
# n = вязкость 

g = 9.81

def rad(degree):
    return degree*pi/180;
def sin(a):
    return math.sin(rad(a))
def cos(a):
    return math.cos(rad(a))





def tr_plot(v0 = 90, angle = 60, all_time = 100, t_int = 0.001,Radius = 1, n_vz = 1,mass = 50):
    
    k = 6*pi*Radius*n_vz
    amout = int(all_time/t_int)
    x = [0]
    y = [0]
    vx = v0*cos(angle)
    vy = v0*sin(angle)
    # plt.plot([0,vx],[0,vy])
    # plt.show()
    
    for i in range(1,amout):
        # y
        y_acc = ((-k*vy) - mass*g)/mass
        yS = vy*t_int + (y_acc*t_int*t_int)/2
        vy = vy + y_acc*t_int
        y.append(y[i-1] + yS)
        
        # x
        x_acc = (-k*vx)/mass
        xS = vx*t_int + (x_acc*t_int*t_int)/2
        vx = vx + x_acc*t_int
        x.append(x[i-1] + xS)
        
        if (y[i] < 0):
#            print(y[i])
            break
    
    
    
    plt.plot(x,y)
    plt.show()
    print("Завершено")
    
    
    
tr_plot(v0 = float(input("Начальная скорость, м/c: ")), 
        angle = float(input("Начальный угол полета, градусы: ")), 
        all_time = float(input("Общее время, секунды: ")), 
        t_int = float(input("Временной интервал, секунды: ")),
        Radius = float(input("Радиус тела, метры: ")), 
        n_vz = float(input("Коэффициент вязкости среды, м2/с: ")),
        mass = float(input("Масса тела, кг: ")))
