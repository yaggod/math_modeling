import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

amount = 3;
siy = 365*24*60*60
sid = 24*60*60
yearcount = 2
t = np.linspace(0, yearcount*siy, sid)

G = 6.67e-11
K = 9e9



fig, ax = plt.subplots()




def solveG(coef, mList, xList, yList, N, index):
    resultX=0; resultY = 0;
    for i in range(N):
        if i == index:
            continue
        chY = (coef* mList[i] * (yList[index] - yList[i]))
        chX =(coef* mList[i] * (xList[index] - xList[i]))
        zn = ((xList[index] - xList[i])**2 +  (yList[index] - yList[i])**2)**1.5
        resultX -= chX/zn;
        resultY -= chY/zn;
    return resultX, resultY;

def solveK(coef, qList, xList, yList, N, index, m):
    resultX =0; resultY = 0;
    for i in range(N):
        if i == index:
            continue
        ch = (coef* qList[i]*qList[index])/m
        cY = ch/(yList[index] - yList[i])
        cX = ch/(xList[index] - xList[i])
        zn = ((xList[index] - xList[i])**2 +  (yList[index] - yList[i])**2)**1.5
        resultX += cX/zn;
        resultY += cY/zn;
    return resultX, resultY

def solvePr(mList, qList, xList, yList, N, index):
    gx, gy = solveG(G, mList, xList, yList, N, index)
    kx, ky = solveK(K, qList, xList, yList, N, index, mList[index])
    return kx+gx, gy+ky;
    
def solveDiff(cort, t):
    ln = int(len(cort)/4)
    x,y,vx,vy = cort[:ln], cort[ln : 2*ln],cort[2*ln:3*ln],cort[3*ln:];
    
    dvx_dt = []; dvy_dt = []
    for i in range(amount):
        dvx, dvy = solvePr(masses,qs,x,y,amount,i) 
        dvx_dt.append(dvx)
        dvy_dt.append(dvy)   
    return np.concatenate((vx,vy, np.array(dvx_dt) , np.array(dvy_dt) ));

def createAnimObjs(amount):
    lines = []; balls = [];
    for i in range(amount):
        line, = plt.plot([],[],'o',color='r',label='Ball')
        ball, = plt.plot([],[],'-',color='r',label='Ball')
        lines.append(line); balls.append(ball)
    return lines,balls


def Animate(frame):
    print(frame)
    for i in range(len(t)):
        balls[i].set_data(xr[frame][i], yr[frame][i])
        # lines[i].set_data(xr[i][:frame], yr[i][:frame])
    
    
x0 = np.array([149e9,149e9,0])
y0 = np.array([0,0,149e9])
vx0 = np.array([0,1,15e3])
vy0 = np.array([3e4,3e4,0])
cort = np.concatenate((x0, y0, vx0, vy0))

balls, lines = createAnimObjs(int(len(cort)/4))

masses = [1.1e30, 2.1e30, 3.6e30]
qs = [1,1e20, 2.1e20, 3.1e20]

solve = odeint(solveDiff, cort,t)
solve = np.split(solve, len(solve)/3)
xr = solve[0::4]
yr = solve[1::4]


ani = FuncAnimation(fig, Animate, frames=len(t))


ani.save("adfkjfk.gif", writer="pillow")






























