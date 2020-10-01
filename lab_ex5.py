print("Введите делимое")
a=int(input())
print("Введите делитель")
b=int(input())
if b==0:
    print("Делитель равен 0")
    exit()
if a%b==0:
    print("Делится нацело")
else:
    aaaa="Не делится нацело, остаток равен"
    print(aaaa, a%b)
aaaa="Частное равно"
print(aaaa, int(a/b))
