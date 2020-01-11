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
