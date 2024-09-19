

import turtle
from random import randint
def kwadrat(nazwa,dlugosc):
    for i in range(4):
        nazwa.forward(dlugosc)
        nazwa.left(90)
def skomplikowany(nazwa):
    for i in range(50):
        nazwa.forward(i)
        nazwa.right(80)
zolwik = turtle.Turtle()
zolwik.speed(1)
zolwik.pencolor('red')

kwadrat(zolwik,100)
kwadrat(zolwik,200)

# skomplikowany(zolwik)
# turtle.exitonclick()
# FIGURA ORDER ORŁA BIAŁEGO!!!!
from turtle import *
import turtle
import random
# fillcolor('red')
# def figura(ile,bok):
#     for i in range(ile):
#         fd(bok)
#         rt(360/ile)
# figura(3,100)
#
# def rysunek1():
#     begin_fill()
#     for i in range(4):
#         figura(3,100)
#         rt(360/4)
#     end_fill()
# rysunek1()
# turtle.done()
# t=turtle.Turtle()
# t.pensize(7)
# t.shape('turtle')    # CHODZENIE ZÓLWIA PO PLANSZY!!!!
# t.color('red')
# window= turtle.Screen()
# def up():
#     t.color(random.choice(['red','green','blue']))
#     t.forward(100)
# def left():
#     t.left(30)
# def right():
#     t.right(30)
#
# def click(x,y):
#     t.color(random.choice(['red', 'green', 'blue']))
#     t.goto(x,y)
#
# window.onkey(up,'Up')
# window.onkey(left,'Left')
# window.onkey(right,'Right')
# window.onkey(turtle.bye,'q')
# window.onclick(click)
# window.listen()
# window.mainloop()