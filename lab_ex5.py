from math import pi,sin
def SCrcl():
    """ 
    круг
    """
    r=float(input("Введите радиус окружности "))
    return pi*(r**2)
def SPr1():
    """ 
    прямоугольник через стороны
    """
    a=float(input("Введите первую сторону прямоугольника "))
    b=float(input("Введите вторую сторону прямоугольника "))
    return a*b
def SPr2():
    """ 
    прямоугольник через диагонали и синус
    """
    a=float(input("Введите диагональ прямоугольника "))
    angle=float(input("Введите угол между диагоналями прямоугольника "))
    angle=angle*pi/180
    return ((a**2)/2)*sin(angle)
def STreug2():
    """ 
    треугольник через основание и высоту
    """
    a=float(input("Введите длину основания "))
    b=float(input("Введите длину высоты к основанию "))
    return a*h      
def STreug1():
    """ 
    прямоугольный треугольник 
    """
    a=float(input("Введите первый катет "))
    b=float(input("Введите второй катет "))
    return a*b/2
n=0
print("Какая фигура?\n1)Прямоугольник\n2)Круг\n3)Треугольник")
while (n<1)or(n>3):
    n=int(input("Напиши "))
if (n==2):
    print(SCrcl())
elif (n==1):
    print("Какая формула?\n1)Через стороны\n2)Через диагонали и угол")
    n=0
    while (n<1)or(n>2):
        n=int(input("Напиши "))
    if (n==1):
        print(SPr1())
    elif (n==1):
        print(SPr2())
elif (n==3):
    print("Какая формула?\n1)Через катеты\n2)Через основание и высоту")
    n=0
    while (n<1)or(n>2):
        n=int(input("Напиши "))
    if (n==1):
        print(STreug1())
    elif (n==1):
        print(STreug2())       