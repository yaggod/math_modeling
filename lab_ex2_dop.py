a=float(input())
b=float(input())
c=float(input())
if (a+b<c) or (b+c<a) or (c+a<b):
    print("Треугольника не существует")
elif (a==b==c):
    print("Треугольник равносторонний")
elif (a==b) or (b==c) or (c==b):
    print("Треугольник равнобедренный")
else:
    print("Треугольник произвольный")
    
