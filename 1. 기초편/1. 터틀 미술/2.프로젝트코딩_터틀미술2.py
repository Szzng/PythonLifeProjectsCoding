import turtle as t
import random

t.speed(0)
t.shape('turtle')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(300):
    t.penup()
    t.goto(random.randint(-350, 350), random.randint(-350, 350))
    t.pendown()

    t.color(random.choice(colors))
    random.choice([t.circle, t.dot])(random.randint(1, 100))
