import tkinter as tk

questions = ['1. 주기적으로 새로운 친구를 만든다.', '2. 자유 시간 중 상당 부분을 다양한 관심사를 탐구하는 데 할애한다.',
             '3. 다른 사람이 울고 있는 모습을 보면 자신도 울고 싶어질 때가 많다.', '4. 일이 잘못될 때를 대비해 여러 대비책을 세우는 편이다.']
answers = []


def start():
    yes.place(relx=0.3, rely=0.5, anchor="center")
    no.place(relx=0.7, rely=0.5, anchor="center")
    selected.set('nothing')

    label.configure(text=questions.pop(0))
    button.configure(text="다음 질문", command=go_next)


def go_next():
    value = selected.get()
    if value == 'nothing':
        button.configure(text='대답해주세요!')
    else:
        answers.append(value)
        selected.set('nothing')

        if len(questions) != 0:
            label.configure(text=questions.pop(0))
            button.configure(text='다음 질문')
        else:
            yes.place_forget()
            no.place_forget()

            label.configure(text='결과가 나왔습니다. 당신의 MBTI는!')
            button.configure(text='결과 보기', command=end)


def end():
    results = [['E', 'I'], ['N', 'S'], ['F', 'T'], ['J', 'P']]
    mbti = ''
    for i in range(len(answers)):
        if answers[i] == 'yes':
            mbti += results[i][0]
        else:
            mbti += results[i][1]

    label.configure(text='당신의 MBTI는 ' + mbti + '입니다.')
    label.place(relx=0.5, rely=0.5, anchor="center")
    button.place_forget()


window = tk.Tk()
window.title("MBTI 테스트")
window.geometry('640x400')

font = ('맑은 고딕', 30, 'bold')
label = tk.Label(window, text="당신의 MBTI는?", font=font, wraplength=500)
button = tk.Button(window, text="시작하기", font=font, width=20, height=2, command=start)
selected = tk.StringVar()
yes = tk.Radiobutton(window, text="Yes", font=font, fg='blue', variable=selected, value='yes')
no = tk.Radiobutton(window, text="No", font=font, fg='red', variable=selected, value='no')

label.place(relx=0.5, rely=0.2, anchor="center")
button.place(relx=0.5, rely=0.8, anchor="center")
window.mainloop()
