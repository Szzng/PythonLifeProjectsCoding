from matplotlib import pyplot as plt

x_values = range(-100, 101)
y_values = []
for x in x_values:
    y_values.append(x ** 2)

plt.plot(x_values, y_values)
plt.grid()
plt.savefig('2차함수.png')
plt.show()
