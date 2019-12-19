class AlphaCalculator:
    """
    Класс для расчета коэффициента сходимости.
    """
    def __init__(self):
        """
        Конструктор.
        """
        self.x_k = None
        self.x_k_1 = None
        self.x_k_2 = None

    def new_x(self, x):
        """
        Добавляет новое значение x.
        """
        self.x_k = self.x_k_1
        self.x_k_1 = self.x_k_2
        self.x_k_2 = x

    def alpha(self):
        """
        Коэффициент сходимости.
        """
        if self.x_k is None or self.x_k_1 is None or self.x_k_2 is None:
            return None

        return abs(self.x_k_1 - self.x_k_2) / abs(self.x_k - self.x_k_1)
