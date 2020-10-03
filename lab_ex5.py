import sys
print("Введите делимое")
a=int(input())
print("Введите делитель")
b=int(input())
if b==0:
    print("Делитель равен 0")
    sys.exit()
if a%b==0:
    print("Делится нацело")
else:
    print("Не делится нацело, остаток равен", a%b)
print("Частное равно", int(a/b))
