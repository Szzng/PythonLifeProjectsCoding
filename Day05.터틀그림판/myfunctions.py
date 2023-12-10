import turtle as t
import random


def go_right():
    t.setheading(0)
    t.fd(10)


def go_up():
    t.setheading(90)
    t.fd(10)


def go_left():
    t.setheading(180)
    t.fd(10)


def go_down():
    t.setheading(270)
    t.fd(10)


def pen_updown():
    if t.isdown():
        t.penup()
    else:
        t.pendown()


def change_color():
    colors = ['red', 'green', 'blue', 'orange', 'black']
    choice = random.choice(colors)
    t.color(choice)


def clear():
    t.clear()
    t.pencolor('black')
