
import matplotlib.pyplot as plt
import random

def transformation_1(p):
    x = p[0]
    y = p[1]
    return x+1,y-1

def transformation_2(p):
    x = p[0]
    y = p[1]
    return x+1, y+1

def transform(p):
    # Lista funkcji przekształcen
    transformations = [transformation_1, transformation_2]
    # Losowo wybieramy i wywołujemy jedna z funkcji przekształcen
    t = random.choice(transformations)
    x, y =t(p)
    return x, y
def build_trajectory(p,n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    return x,y

if __name__ == '__main__':
    # Punkt poczatkowy
    p=(1, 1)
    n = int(input('Podaj liczbe iteracji:'))
    x, y = build_trajectory(p, n)
    # Wyswietlenie wykresu
    plt.plot(x , y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()