import math

import matplotlib.pyplot as plt
from sympy.plotting import plot
from sympy import Symbol, solve, Derivative,sin,sympify,Integral
from sympy.core.sympify import SympifyError

def grad_ascent(x0, f1x, x):
    epsilon = 1e-6
    step_size = 1e-4
    x_old =x0
    x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    while abs(x_old - x_new)> epsilon:
        x_old = x_new
        x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    return x_new

if __name__ =='__main__':
    f = input('Podaj funkcje jednej zmiennej: ')
    var = input('Podaj zmienna, wzgledem której nalezy wyznaczyc pochodna funkcji :')
    var0= float(input('Podaj wartosc poczatkowa funkcji: '))
    try:
        f = sympify(f)
    except SympifyError:
        print('wpisana funkcja jest nieprawidłowa')
    else:
        var = Symbol(var)
        d = Derivative(f,var).doit()
        var_max = grad_ascent(var0,d,var)
        print('{0}: {1}'.format(var.name,var_max))
        print('wartosc maksymalna: {0}'.format(f.subs({var:var_max})))




