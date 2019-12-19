from AlphaCalculator import AlphaCalculator


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
