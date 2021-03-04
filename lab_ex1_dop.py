def poww(a,b=1):
    n=int(a)
    for i in range(1,b,1):
        a=a*n
    return a

num=st=-1
while (num<=0):
    num=float(input("Какое число возвести в степень "))
while (st<=0):
    st=int(input("В какую степень "))
print(poww(num,st))