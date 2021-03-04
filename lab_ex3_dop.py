num=int(input("Введите число "))
c=[]
while(num>0):
    b=int(num%10)
    num=(num-b)/10
    print(b, end='')