import tkinter as tk


def print_label():
    label.configure(text='힘내세요!')


window = tk.Tk()  # 화면 만들기
window.title("tkinter 연습")  # 화면 제목
window.geometry('400x300')  # 화면 크기

font = ('맑은 고딕', 20, 'bold')
label = tk.Label(text='라벨', font=font)  # 라벨 만들기
button = tk.Button(text='클릭!', font=font, command=print_label)  # 버튼 만들기

label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)  # 라벨 위치 지정
button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)  # 버튼 위치 지정

window.mainloop()  # 만든 화면을 실행하기
