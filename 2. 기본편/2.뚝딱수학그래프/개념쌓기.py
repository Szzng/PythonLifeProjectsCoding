import matplotlib.pyplot as plt

x_values = range(-100, 100)
y = []
for x in x_values:
    y.append(x ** 2)

plt.plot(x_values, y)
plt.grid()
plt.savefig('2차함수.png')
plt.show()
