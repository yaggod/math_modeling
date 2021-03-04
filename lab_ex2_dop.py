import numpy as np
def fibb(n):
    a=np.array([0,1])
    a=np.resize(a,n)
    for i in range(2,n,1):
        a[i]=a[i-1]+a[i-2]
    return a[n-1]

print(fibb(int(input("Какое число из ряда Фиббоначи вы хотите получить: "))))