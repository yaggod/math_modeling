import sympy
a, x, y, alpha, p, o = sympy.symbols('a x y ap p o*')
ch = (sympy.exp(alpha)+sympy.exp(-alpha))/2
sh = (sympy.exp(alpha)-sympy.exp(-alpha))/2
ch = ch.subs(alpha, p)
sh = sh.subs(alpha, p)
x = (a*sh)/(ch-sympy.cos(o))
y = (a*sympy.sin(p))/(ch-sympy.cos(o))
p1 = float(input("Введите p: "))
o1 = float(input("Введите o: ")) 
a1=0
while (a1<1 or a1>5):
    a1 = float(input("Введите a: "))
x = x.subs([(p,p1),(o,o1),(a,a1)])
y = y.subs([(p,p1),(o,o1),(a,a1)])
print(x.evalf(),"\n",y.evalf())
