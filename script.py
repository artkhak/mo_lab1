import matplotlib.pyplot as plt
from powell import powell
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
f_min = f(x_min)

# Вывод графика
xs = [i / 1000 for i in range(0, 2000, 1)]
ys = [f(x) for x in xs]

plt.plot(xs, ys, 'b-', label='ЦФ')
plt.scatter(x_min, f_min, marker='x', c='r', s=100, label='Точка оптимума')

plt.ylabel("y")
plt.xlabel("x")
plt.grid(True)

x_ticks = [i / 10 for i in range(0, 22, 1)]
plt.xticks(x_ticks)
plt.xlim(0, 2)

y_ticks = [i / 10 for i in range(0, 130, 10)]
plt.yticks(y_ticks)
plt.ylim(0, 12)

plt.legend()

plt.show()

# Вывод выходных данных
print(f'Точка оптимума - {x_min}')
print(f'Оптимальное значение ЦФ - {f_min}')
print(f'Количество итераций - {calculation_data.iteration_count}')
print(f'Количество вычислений функции - {calculation_data.function_call_count}')
print(f'Коэффициент сходимости - {calculation_data.alpha_calculator.alpha()}')
