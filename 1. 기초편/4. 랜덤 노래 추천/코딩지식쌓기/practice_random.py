import tkinter as tk
import random


# 행운의 뽑기
def good_luck():
    # 리스트 데이터를 고친다면, 교실에서 친구들 발표 뽑기 등으로 활용가능
    coupons = ['1천원', '2천원', '3천원', '5천원', '1만원', '꽝']
    pick = random.choice(coupons)
    label.configure(text='행운의 쿠폰은 바로!! \n' + pick + '!!!')
    button.configure(text='재도전')


window = tk.Tk()
window.title("행운의 뽑기")
window.geometry('400x300')

font = ('맑은 고딕', 30, 'bold')
label = tk.Label(text='행운의 할인 쿠폰 뽑기', font=font)
button = tk.Button(text='뽑기', font=font, width=4, height=2, command=good_luck)

label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
window.mainloop()
