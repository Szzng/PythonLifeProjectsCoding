import tkinter as tk

questions = [
    '1. 처음 보는 사람과도 어렵지 않게 이야기를 나누는 편인가요?',
    '2. 자유 시간에 다양한 관심사를 탐구하는 것을 좋아하나요?',
    '3. 다른 사람이 울고 있으면 자신도 울고 싶어질 때가 많나요?',
    '4. 일이 잘못될 때를 대비해 여러 대비책을 세우는 편인가요?'
]
answers = []


def start():
    yes.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
    no.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

    label.configure(text=questions.pop(0))
    button.configure(text="다음 질문", command=go_next)


def go_next():
    value = selected.get()
    if value == 'nothing':
        button.configure(text='대답해주세요!')
    else:
        answers.append(value)
        selected.set('nothing')

        if len(questions) != 0:  # 질문이 남았다면
            label.configure(text=questions.pop(0))
            button.configure(text='다음 질문')
        else:  # 질문이 끝났다면
            label.configure(text='결과가 나왔습니다. 당신의 MBTI는!')
            button.configure(text='결과보기', command=end)
            yes.place_forget()
            no.place_forget()


def end():
    results = [['E', 'I'], ['N', 'S'], ['F', 'T'], ['J', 'P']]
    mbti = ''
    for i in range(len(answers)):
        if answers[i] == 'yes':
            mbti += results[i][0]
        else:
            mbti += results[i][1]

    label.configure(text='당신의 MBTI는 ' + mbti + '입니다.')
    button.place_forget()


window = tk.Tk()
window.title("MBTI 판별 프로그램")
window.geometry('640x400')

font = ('맑은 고딕', 25, 'bold')
label = tk.Label(window, text="당신의 MBTI는?", font=font, wraplength=500)
button = tk.Button(window, text="시작하기", font=font, width=15, height=1,  bg='pink', fg='white', command=start)
label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

selected = tk.StringVar()
selected.set('nothing')

yes = tk.Radiobutton(window, text="Yes", font=font, fg='blue', variable=selected, value='yes')
no = tk.Radiobutton(window, text="No", font=font, fg='red', variable=selected, value='no')

window.mainloop()
