import turtle as t

t.speed(0)
t.shape('turtle')
t.bgcolor('black')
colors = ['orange', 'skyblue', 'yellow']

i = 0
while True:
    t.fd(i)
    t.color(colors[i % 3])
    t.lt(119)
    i += 1
