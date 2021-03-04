res1=int(0)
res2=int()
print("Уравнение вида: X^2+X+C=0")
x2=int(input("Введите коэффицент при X^2 "))
x1=int(input("Введите коэффицент при X "))
c=int(input("Введите значение C "))
print(x2, end='x^2')
if x1>=0:
    print(" +",x1, end='x')
else:
    print(x1, end='x')
if c>=0:
    print(" +", c, end="c = 0")
else:
    print(c, "c = 0")
d=(x1**2)-(4*x2*c)
if d<0:
    print("\nНе имеет решений")
else:
    res1 =(-1*x1+(d**(1/2)))/(2*x2)
    res2 =(-1*x1-(d**(1/2)))/(2*x2)
if (res1==res2!=0):
    print("Результат - ", res1)
elif (res1!=res2):
    print("Результаты - ", res1, "и", res2)
