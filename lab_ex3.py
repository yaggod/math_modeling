from const import g
def MechEn(m,h,v):
    return ((m*(v**2))/2)+m*h*g
m=int(input("Масса тела (кг) "))
h=int(input("Высота полета (м) "))
v=int(input("Скорость тела  (м/c) "))
print(MechEn(m,h,v))