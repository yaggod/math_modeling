def mltp(a):
    b=a[0]
    for (i),n in np.ndenumerate(a):
        b=b*n
    return b
import numpy as np
b=np.array([1,2,3,5,43,5,2])
print("Сумма всех значений массива равна",mltp(b))