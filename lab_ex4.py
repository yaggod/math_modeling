print("Число элементов ряда Фибоначчи")
a=int(input())
b=[0, 1]
n=int(0)
while n<a:
    c=b[n]+b[n+1]
    b.append(c)
    n=n+1
print(b[1:n+2])