import turtle as t
import random

t.speed(0)
t.shape('turtle')
t.bgcolor('black')
colors = ['deeppink', 'orange', 'gold', 'greenyellow', 'deepskyblue', 'magenta']

for i in range(300):
    t.penup()

    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    t.goto(x, y)

    c = random.choice(colors)
    t.color(c)

    t.pendown()
    draw = random.choice([t.circle, t.dot])
    size = random.randint(1, 100)
    draw(size)
