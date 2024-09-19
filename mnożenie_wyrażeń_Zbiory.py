from sympy import Symbol
from sympy import symbols
from sympy import factor
from sympy import expand
from sympy import pprint
from  sympy import init_printing
from sympy import simplify
from sympy import sympify
from sympy.core.sympify import SympifyError
from sympy import expand, sympify
from sympy import Symbol, solve,pprint
from sympy.plotting import plot
from sympy import Symbol
from sympy import Poly, Symbol, solve_poly_inequality
from sympy import Symbol, Poly, solve_rational_inequalities
from sympy import FiniteSet
from fractions import Fraction
'''''
def product(expr1 , expr2):
    prod = expand(expr1*expr2)
    print(prod)

if __name__ =='__main__':
    expr1 = input('Wpisz pierwsze wyrazenie')
    expr2 = input('Wpisz drugie wyrazenie')
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Nieprawidłowe dane wejsciowe!')
    else:
        product(expr1, expr2)
'''''
'''''
expr = input('Wprowadz wyrażenie')
expr = sympify(expr)
y = Symbol('y')
print(solve(expr, y))
solutions = solve(expr, 'y')
expr_y = solutions[0]
print(expr_y)
'''''
'''''
from sympy import FiniteSet, pi

def time_period(length):
    g = 9.8
    T = 2*pi*(length/g)**0.5

    return T

if __name__ == '__main__':
    L =FiniteSet(15,18, 21,22.5,25)

    for l in L:
        t = time_period(l/100)
        print('długosc: {0} cm, okres ruchu {1:.3f} s'.format(float(l),float(t)))
'''''
from sympy import FiniteSet, pi
def time_period(length,g):
    T = 2*pi*(length/g) ** 0.5

    return T
if __name__ =='__main__':
    L = FiniteSet(15, 18, 21, 22.5, 25)
    g_values = FiniteSet(9.8, 9.78, 9.83)
    print('{0:^15}{1:^35}{2:^15}'.format('Długosc(cm)','przyspieszenie ziemskie(m/s^2)', 'okres ruchu'))
    for elem in L*g_values:
        l = elem[0]
        g = elem[1]
        t = time_period(l/100, g)

        print('{0:^15} {1:^35} {2:^15.3f}'.format(float(l),float(g),float(t)))