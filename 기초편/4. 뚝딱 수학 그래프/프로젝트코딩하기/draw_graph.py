import matplotlib.pyplot as plt

formula = input("x로 이루어진 함수식을 입력하세요 (예시: 3*x**2+2*x) : ")

x_values = range(-100, 100)
y = []

for x in x_values:
    try:
        y.append(eval(formula))
    except:
        print("잘못된 입력입니다. 올바른 함수식을 입력하세요.")
        break

if len(y) == len(x_values):
    plt.plot(x_values, y)
    plt.grid()
    plt.savefig('입력받은 함수.png')
    plt.show()
