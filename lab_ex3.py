import sympy as sp
x = sp.symbols("x")
Exp = x**2 + x + 1/x + 1/x**2
Exp =Eq(Exp,4)
Exp = sp.solve(Exp,x)
for i in Exp:
    print(i)


            # 2 Часть
e, M, E = sp.symbols('e M E')
Exp = E - e*sp.sin(E)
Exp = Eq(Exp,M)
Exp = Exp.subs([(e, 8/10),(M, 9)])
Exp = sp.solve(Exp)