import tkinter as tk
import random

musics = []


def add():
    music = entry.get()
    if len(music):
        musics.append(music)
        entry.delete(0, tk.END)
        label.configure(text='< ' + music + ' > 추가 완료! \n더 추가해보세요!')


def end():
    addButton.place_forget()
    endButton.place_forget()
    entry.place_forget()
    recommendButton.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    label.configure(text='노래를 추천해드릴게요!')


def recommend():
    music = random.choice(musics)
    label.configure(text=music + '! \n추천합니다!')


window = tk.Tk()
window.title("랜덤 노래 추천기")
window.geometry('640x400')

font = ('맑은 고딕', 25, 'bold')
label = tk.Label(window, text="당신이 좋아하는 노래를 알려주세요.", font=font, wraplength=500)
entry = tk.Entry(window, font=font, width=20, borderwidth=4)
addButton = tk.Button(window, text="추가", font=font, width=5, height=2, command=add)
endButton = tk.Button(window, text="완료", font=font, width=5, height=2, command=end)
recommendButton = tk.Button(window, text="노래 추천", font=font, width=20, height=2, command=recommend)

label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
addButton.place(relx=0.4, rely=0.8, anchor=tk.CENTER)
endButton.place(relx=0.6, rely=0.8, anchor=tk.CENTER)
window.mainloop()
