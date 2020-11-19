import sympy as sp
x = sp.symbols('x')
Exp1 = sp.Abs(x**2 + 2*x - 3) + 3*(x+1)
Exp2 = ((x-1)*(x+2))/((x-3)*(x+4))
Res1 = sp.reduce_abs_inequality(Exp1, "<",x)
Res2 = sp.reduce_abs_inequality(Exp2, "<=",x)
print(Res1,"\n",Res2)