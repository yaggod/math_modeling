num=int(input("Введите число "))
sp=[]
res=int(0)
for i in range(1,num,1):
    if num%i==0:
        sp.append(i)
print("Множители числа",num,"-",sp)
leng=len(sp)
for i in range(0,leng,1):
    res=res+sp[i]
print("Сумма всех множителей",num,"-",res)
if res==num:
    print("Число совершенное")
else:
    print("Число не совершенное")