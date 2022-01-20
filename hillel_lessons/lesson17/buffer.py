class Buffer:

    def __init__(self):
        # конструктор без аргументов
        self.num = []

    def add(self, *a):
        # добавлена следующая часть последовательности
        self.num.extend(a)
        while len(self.num) >= 5:
            print(sum(self.num[:5]))
            del self.num[0:5]

    def get_current_part(self):
        # возврат сохраненных в текущий момент элементов последовательности
        # в порядке, в котором они были добавлены
        pass
        print(self.num)
        return self.num


# Тестирование работы
test = Buffer()
test.add(6, 8, 1)
test.get_current_part()
test.add(4, 5, 6, 2, 5, 8)
test.get_current_part()
test.add(2, 11,)
test.get_current_part()
test.add(1, 2, 3, 4,)
test.get_current_part()
