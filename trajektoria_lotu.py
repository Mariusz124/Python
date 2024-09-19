from pylab import plot, show, title, xlabel, ylabel, legend
from matplotlib import pyplot as plt
import math


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('współzedna x')
    plt.ylabel('współzedna y')
    plt.title ('Trajektoria rzutu piłką')

def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start += interval
    return numbers
def draw_trajectory(u, theta):
    theta = math.radians( theta)
    g = 9.8
    # Czeas lotu
    t_flight = 2*u*math.sin(theta)/g
    # określenie punktów czasu
    intervals = frange(0, t_flight, 0.001)
    # Lista współrzędnych x i y
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    draw_graph(x, y)
if __name__ == '__main__':
    u_list = [20, 40, 60]
    theta = 45
    for u in u_list:
        draw_trajectory(u, theta)
    # Dodajemy do wykresu legende i wyswietlamy go
    plt.legend(['20', '40', '60'])
    plt.show()