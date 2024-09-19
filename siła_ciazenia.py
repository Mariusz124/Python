
from pylab import  plot,  show

import matplotlib.pyplot as plt
from pylab import plot, show, title, xlabel, ylabel, legend

# Funkcja służaca do narysowania wykresu
def draw_graph(x, y):
    plt.plot(x, y,marker = 'o')
    plt.xlabel('odległośc w metrach ')
    plt.ylabel('Siła ciązenia wnewtonach')
    plt.title('Zalezność siły ciążenia od odległości')
    plt.show()

def generate_F_r():
    r = range(100, 1001, 50)
    F=[]

    G = 6.674*(10**-11)
    m1 = 0.5
    m2 = 1.5

    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)

    draw_graph(r, F)

if __name__=='__main__':
    generate_F_r()




