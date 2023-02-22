import turtle as t
import random

t.speed(0)
t.shape('turtle')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(100):
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()

    t.color(random.choice(colors))
    random.choice([t.circle, t.dot])(random.randint(1, 100))
