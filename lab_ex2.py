from lab_ex1 import g,Pln,Bolz,Eyl
from math import sin,cos,sqrt
def first():
    h=100
    beta=(30*3.14)/180
    alpha=(3.14/3)*3.14/180
    tg=(sin(beta)/cos(beta))
    tgA=(sin(alpha)/cos(alpha))
    h=100
    Chisl=g*h*tg**2
    Znam1=2*(cos(alpha))**2
    Znam2=(1-tg*tgA)
    Znam=Znam1*Znam2
    return (sqrt(Chisl/Znam))
def second():
    a1=(2/sqrt(3.14))
    T=200
    a2=(Pln)/(Bolz*T)**(3/2)
    a3=Eyl**(-1*(Eyl/(Bolz*T)))
    a4=Eyl**(200/2)
    return a1*a2*a3*a4

    
    
    
    
    
    
    
#
