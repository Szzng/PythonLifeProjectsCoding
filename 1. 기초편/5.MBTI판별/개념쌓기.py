import tkinter as tk


def submit():
    value = selected.get()
    if value == 'nothing':  # 아무것도 선택하지 않았다면
        button.configure(text='대답해주세요!')
    else:  # 선택했다면
        button.configure(text=value + ' 선택 완료!')


window = tk.Tk()
window.title("좋아하는 음식 조사")
window.geometry('600x800')

font = ('맑은 고딕', 30, 'bold')
label = tk.Label(window, text="다음 중 가장 좋아하는 음식을 고르세요!", font=font, wraplength=500)
button = tk.Button(window, text="완료", font=font, width=20, height=2, command=submit)
label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

selected = tk.StringVar()
selected.set('nothing')

food = ['치킨', '피자', '떡볶이', '햄버거', '돈까스', '라면']
for i in range(len(food)):
    radiobutton = tk.Radiobutton(window, text=food[i], font=font, variable=selected, value=food[i])
    radiobutton.place(relx=0.5, rely=0.2 + (i * 0.1), anchor=tk.CENTER)

window.mainloop()
