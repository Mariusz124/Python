'''
Wyznaczene dominaty listy
'''
'''
from collections import Counter


def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]


if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    mode = calculate_mode(scores)
    print('dominata ocen na liscie jest {0} '.format(mode))
'''
import matplotlib.pyplot as plt
def fib(n):
    if n==1:
        return 1
    if n == 2:
        return [1,1]
    # n>2
    a=1
    b=1
    # Pierwsze dwa elementy ciagu
    series = [a,b]
    for i in range(n):
        c = a+b
        series.append(c)
        a=b
        b=c
        return series
def plot_ratio(series):
    ratios = []
    for i in range(len(series)-1):
        ratios.append(series[i+1]/series[i])
    plt.plot(ratios)
    plt.title('współczynnik pomiędzy ciagiem Fibonacciego\ni złotym podziałem')
    plt.ylabel('Wspólczynnik')
    plt.xlabel('Liczba')
    plt.show()
if __name__ == '__main__':
    #Liczba wartosci w ciagu Fibonacciego
    num = 100
    series = fib(num)
    plot_ratio(series)

