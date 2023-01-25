import matplotlib.pyplot as plt

x = range(-100, 100)
y = []
for value in x:
    y.append(value ** 2)

plt.plot(x, y)
plt.grid()
plt.savefig('2차함수.png')
plt.show()