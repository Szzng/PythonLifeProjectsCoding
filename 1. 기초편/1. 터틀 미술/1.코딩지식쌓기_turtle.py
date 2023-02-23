# 터틀 기본 명령어 익히기
# import turtle as t
# t.shape('turtle')
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.lt(60)
# t.fd(100)

# 터틀에게 반복 명령어 내리기
import turtle as t
t.shape('turtle')
colors = ['red', 'orange', 'yellow', 'green', 'blue']
for c in colors:
    t.color(c)
    t.fd(200)
    t.lt(144)
