from control_functions import *
import turtle as t

t.shape('turtle')

t.onkeypress(go_right, 'Right')
t.onkeypress(go_up, 'Up')
t.onkeypress(go_left, 'Left')
t.onkeypress(go_down, 'Down')
t.onkeypress(pen_updown, 'Return')
t.onkeypress(change_color, 'c')  # c 대소문자 구분
t.onkeypress(clear, 'Escape')  # esc key

t.listen()
t.mainloop()
