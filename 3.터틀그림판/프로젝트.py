from myfunctions import *
import turtle as t

t.shape('turtle')

t.onkeypress(go_right, 'Right')
t.onkeypress(go_up, 'Up')
t.onkeypress(go_left, 'Left')
t.onkeypress(go_down, 'Down')
t.onkeypress(pen_updown, 'Return') # Enter 키
t.onkeypress(change_color, 'c')  # c 대소문자 구분해야 함
t.onkeypress(clear, 'Escape')  # esc 키

t.listen()
t.mainloop()
