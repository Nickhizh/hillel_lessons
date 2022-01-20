class TriangleChecker:
    def __init__(self, storony):
        self.storony = storony

    def triangle(self):
        if all(isinstance(side, (int, float)) for side in self.storony):
            if all(side > 0 for side in self.storony):
                sortstorony = sorted(self.storony)
                if sortstorony[0] + sortstorony[1] > sortstorony[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'

