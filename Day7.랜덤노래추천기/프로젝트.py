import tkinter as tk
import random

playlist = []


def add():
    music = entry.get()
    if len(music) > 0:
        playlist.append(music)
        entry.delete(0, tk.END)
        label.configure(text='< ' + music + ' > 추가 완료! \n더 추가해보세요!')


def end():
    add_btn.place_forget()
    end_btn.place_forget()
    entry.place_forget()
    recommend_btn.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    label.configure(text='노래를 추천해드릴게요!')


def recommend():
    music = random.choice(playlist)
    label.configure(text=music + '\n추천합니다!')


window = tk.Tk()
window.title("랜덤 노래 추천기")
window.geometry('600x400')

font = ('맑은 고딕', 25, 'bold')
label = tk.Label(window, text="당신이 좋아하는 노래를 알려주세요.", font=font, wraplength=500)
entry = tk.Entry(window, font=font, width=20, borderwidth=4)
add_btn = tk.Button(window, text="추가", font=font, width=5, height=1, bg='skyblue', fg='white', command=add)
end_btn = tk.Button(window, text="완료", font=font, width=5, height=1, bg='pink', fg='white', command=end)
recommend_btn = tk.Button(window, text="노래 추천", font=font, width=20, height=1, bg='pink', fg='white', command=recommend)

label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
add_btn.place(relx=0.4, rely=0.8, anchor=tk.CENTER)
end_btn.place(relx=0.6, rely=0.8, anchor=tk.CENTER)
window.mainloop()
