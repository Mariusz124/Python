from sympy import Symbol
from sympy import symbols
from sympy import factor
from sympy import expand
from sympy import pprint
from  sympy import init_printing
from sympy import Symbol, pprint, init_printing

def print_series(n):
    # Inicjalizacja wyswietlania w odwrotnej kolejnosci
    init_printing(order='rev-lex')

    x = Symbol('x')
    series = x
    for i in range(2,n+1):
        series = series + (x**i)/i
        pprint(series)

if __name__ == '__main__':
    n = (input('podaj liczbe elementów szeregu: '))
    print_series(int(n))