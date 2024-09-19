
from matplotlib import pyplot as plt
from matplotlib import animation
import math

def create_circle():
    circle = plt.Circle((0, 0),0.05)
    return circle
def update_radius(i,circle):
    circle.radius = i*0.5
    return circle,
def create_animation():
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10,10),ylim=(-10,10))
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)
    anim = animation.FuncAnimation(
        fig,update_radius,fargs = (circle,),frames=30, interval=50)
    plt.title('Prosta animacjakoła')
    plt.show()

if __name__ =='__main__':
    create_animation()

'''''
g = 9.8
def get_intervals(u, theta):

    t_flight = 2*u*math.sin(theta)/g
    intervals = []
    start = 0
    interval = 0.005
    while start < t_flight:
        intervals.append(start)
        start+= interval
    return intervals

def  update_position(i, circle, intervals, u, theta):

    t = intervals[i]
    x = u*math.cos(theta)*t
    y = u*math.sin(theta)*t - 0.5*g*t*t
    circle.center = x,y
    return circle,

def create_animation(u,theta):

    intervals = get_intervals(u,theta)
    xmin = 0
    xmax = u*math.cos(theta)*intervals[-1]
    ymin = 0
    t_max = u*math.sin(theta)/g
    ymax = u*math.sin(theta)*t_max - 0.5*g*t_max**2
    fig = plt.gcf()
    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
    circle = plt.Circle((xmin, ymin),1.0)
    ax.add_patch(circle)
    anim = animation.FuncAnimation(fig,update_position, fargs = (circle, intervals, u,theta),frames = len(intervals), interval = 1, repeat=False)
    plt.title('animacja rzuconej piłki')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

if __name__== '__main__':
    try:
        u = float(input('Wpisz predkośc poczatkowa (m/s):'))
        theta = float(input('Wpisz kont rzutu (stopnie):'))
    except ValueError:
        print('Wprowadzone dane są nieprawidłowe.')
    else:
        theta = math.radians(theta)
        create_animation(u,theta)
'''''