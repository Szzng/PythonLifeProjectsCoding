import turtle as t
import random

t.speed(0)
t.shape('turtle')
t.bgcolor('black')
colors = ['deeppink', 'orange', 'gold', 'greenyellow', 'deepskyblue', 'magenta']

for i in range(300):
    t.penup()
    t.goto(random.randint(-400, 400), random.randint(-400, 400))
    t.pendown()

    t.color(random.choice(colors))
    random.choice([t.circle, t.dot])(random.randint(1, 100))
