def powell(function, interval, start_x, delta, ex, ef, calculation_data=None):
    """
    Ищет точку минимума методом Пауэлла.
    :param function: Функция для поиска.
    :param interval: Интервал для поиска.
    :param start_x: Стартовая точка.
    :param delta: Дельта, для поиска соседних точек.
    :param ex: Допустимое отклонение по аргументу.
    :param ef: Допустимое отклонение по значению.
    :param calculation_data: Данные о расчете.
    :return: Точка минимума.
    """
    # Получаем минимальную и максимальную точку интервала.
    interval_min = min(interval)
    interval_max = max(interval)

    # Получаем три точки для дальнейшего поиска.
    x1 = start_x
    x2 = x1 + delta
    x3 = x2 + delta if function(x1) > function(x2) else x1 - delta

    # Сортируем точки.
    if x3 < x1:
        [x1, x2, x3] = [x3, x1, x2]

    # Проверяем, что минимальная точка входит в интервал.
    # Если точка не входит в интервал, то заменяем ее на минимальную точку интервала.
    x1 = interval_min if x1 < interval_min else x1

    # Проверяем, что максимальная точка входит в интервал.
    # Если точка не входит в интервал, то заменяем ее на максимальную точку интервала.
    x3 = interval_max if x3 > interval_max else x3

    # Получаем значене итерациями, через рекурсивный метод.
    return powell_recursive(function, interval, x1, x2, x3, delta, ex, ef, calculation_data)


def powell_recursive(function, interval, x1, x2, x3, delta, ex, ef, calculation_data=None):
    """
    Рекурсивно ищет точку минимума функции методом Пауэлла.
    :param function: Функция для поиска.
    :param interval: Интервал для поиска.
    :param x1: Минимальная точка для поиска.
    :param x2: Центральная точка для поиска.
    :param x3: Максимальная точка для поиска.
    :param delta: Дельта, для поиска соседних точек.
    :param ex: Допустимое отклонение по аргументу.
    :param ef: Допустимое отклонение по значению.
    :param calculation_data: Данные о расчете.
    :return: Точка минимума.
    """
    if calculation_data is not None:
        calculation_data.add_iteration()

    # Получаем минимальную и максимальную точку интервала.
    interval_min = min(interval)
    interval_max = max(interval)

    # Получаем значения функции в переданных точках.
    f1 = function(x1)
    if calculation_data is not None:
        calculation_data.add_function_call()
    f2 = function(x2)
    if calculation_data is not None:
        calculation_data.add_function_call()
    f3 = function(x3)
    if calculation_data is not None:
        calculation_data.add_function_call()

    # Определяем минимальное значение функции из полученных.
    f_min = min(f1, f2, f3)

    # Получаем точку, в которой функция имеет значение f_min.
    x_min = x1 if f1 == f_min else x2 if f2 == f_min else x3

    # Получаем параметры аппроксимирующего квадратичного полинома.
    a1 = (f2 - f1) / (x2 - x1)
    a2 = ((f3 - f1) / (x3 - x1) - (f2 - f1) / (x2 - x1)) / (x3 - x2)

    # Получаем стационарную точку.
    x_stat = (x2 + x1) / 2 - a1 / (2 * a2)

    # Проверяем вхождение стационарной точки в диапазон допустимых значений.
    # Должно входить в интервал значений для поиска и быть больще, чем x1 - delta, и меньше, чем x3 + delta.
    # Если в диапазон не входит, то заменяем ближайшим допустимым.
    x_stat = max(interval_min, x1 - delta, x_stat)
    x_stat = min(interval_max, x3 + delta, x_stat)

    # Получаем значение функции в стационарной точке.
    f_stat = function(x_stat)

    if calculation_data is not None:
        calculation_data.add_function_call()

    # Проверяем условие найденности решения.
    # Если условие выполняется, то принимаем за точку минимума стационарную точку или минимальную точку из переданных,
    # в зависимости от того, в какой точке функция принимает наименьшее значение.
    if abs(f_min - f_stat) < ef and abs(x_min - x_stat) < ex:
        x_min = x_stat if f_stat < f_min else x_min
        if calculation_data is not None:
            calculation_data.alpha_calculator.new_x(x_min)
        return x_min

    # Выбираем новые точки для дальнейшего поиска.
    xs = sorted([x1, x2, x3, x_stat])
    x_min_index = xs.index(x_min)
    x1 = xs[0] - delta if x_min_index == 0 else xs[x_min_index - 1]
    x2 = xs[x_min_index]
    x3 = xs[3] + delta if x_min_index == 3 else xs[x_min_index + 1]

    # Проверяем, что минимальная точка входит в интервал.
    # Если точка не входит в интервал, то заменяем ее на минимальную точку интервала.
    x1 = interval_min if x1 < interval_min else x1

    # Проверяем, что максимальная точка входит в интервал.
    # Если точка не входит в интервал, то заменяем ее на максимальную точку интервала.
    x3 = interval_max if x3 > interval_max else x3

    if calculation_data is not None:
        calculation_data.alpha_calculator.new_x(x_min)

    # Возвращаем точку минимума, полученную в следующией итерации.
    return powell_recursive(function, interval, x1, x2, x3, delta, ex, ef, calculation_data)


class CalculationData:
    """
    Класс для сбора данных расчета.
    """

    def __init__(self):
        """
        Конструктор.
        """
        self.iteration_count = 0
        self.function_call_count = 0
        self.alpha_calculator = AlphaCalculator()

    def add_iteration(self):
        """
        Добавляет итерацию.
        """
        self.iteration_count += 1

    def add_function_call(self):
        """
        Добавляет вызов функции.
        """
        self.function_call_count += 1


def f(x):
    """
    Заданая функция.
    :param x: Аргумент функции.
    :return: Значение функции.
    """
    return 1 / 4 * x ** 4 + x ** 2 - 8 * x + 12


class AlphaCalculator:
    """
    Класс для расчета коэффициента сходимости.
    """

    def __init__(self):
        """
        Конструктор.
        """
        self.x_k = None
        self.x_k1 = None
        self.x_k2 = None

    def new_x(self, x):
        """
        Добавляет новое значение x.
        """
        [self.x_k, self.x_k1, self.x_k2] = [self.x_k1, self.x_k2, x]

    def alpha(self):
        """
        Коэффициент сходимости.
        """
        if self.x_k is None or self.x_k1 is None or self.x_k2 is None:
            return None

        return abs(self.x_k1 - self.x_k2) / abs(self.x_k - self.x_k1)


import matplotlib.pyplot as plt

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
