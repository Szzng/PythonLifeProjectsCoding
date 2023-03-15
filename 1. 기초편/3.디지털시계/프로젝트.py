import tkinter as tk
import time


def clock():
    now = time.strftime("%Y년 %m월 %d일 \n %H:%M:%S")
    label.configure(text=now)
    label.after(1000, clock)


window = tk.Tk()
window.title("디지털시계")
window.geometry('400x300')

font = ('맑은 고딕', 25, 'bold')
label = tk.Label(text='시작 버튼을 누르세요', font=font)
button = tk.Button(text='시작', font=font, width=4, height=1, command=clock)

label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

window.mainloop()
