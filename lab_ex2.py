import sympy as sp
x,y,z = sp.symbols("x y z")
Exp = (x*(y**2)-2*(x*y*z)+x*(z**2)+(y**2)-2*(y*z)+(z**2))/((x**2)-1)
Exp = sp.simplify(Exp)
print(Exp)

            #2 часть

alpha = sp.symbols("Ap")
a = (1+sp.sin(alpha))
b = (1-sp.sin(alpha))
Exp = sp.sqrt(a/b)+sp.sqrt(b/a)
Exp = sp.expand(Exp)
Exp = sp.simplify(Exp)
print(Exp)