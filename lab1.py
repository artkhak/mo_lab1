from powell import powell
import matplotlib.pyplot as plt
import numpy as np
from CalculationData import CalculationData


def f(x):
    """
    Заданая функция.
    :param x: Аргумент функции.
    :return: Значение функции.
    """
    return 1 / 4 * x ** 4 + x ** 2 - 8 * x + 12


interval = [0, 2]
calculation_data = CalculationData()
ex = 0.00001
ef = 0.00001
delta = 0.1
x_min = powell(f, interval, interval[0], delta, ex, ef, calculation_data)
print(x_min)

f_min = f(x_min)

# Вывод графика
xs = np.arange(0, 2, 0.001)
ys = [f(x) for x in xs]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x_axis_major_ticks = np.arange(0, 2, 0.5)
x_axis_minor_ticks = np.arange(0, 2, 0.1)

y_axis_major_ticks = np.arange(0, 12, 2)
y_axis_minor_ticks = np.arange(0, 12, 1)

ax.set_xticks(x_axis_major_ticks)
ax.set_xticks(x_axis_minor_ticks, minor=True)
ax.set_yticks(y_axis_major_ticks)
ax.set_yticks(y_axis_minor_ticks, minor=True)

ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

ax.plot(xs, ys, 'b-')
ax.scatter(x_min, f_min, marker='x', c='r', s=100)

plt.ylabel("f(x)")
plt.xlabel("x")
plt.grid(True)

plt.xlim(0, 2)
plt.ylim(0, 12)

plt.show()

print(f'{calculation_data.iteration_count}')
