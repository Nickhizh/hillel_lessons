class Counter:

    def __init__(self, mini: int, maxi: int):
        self.mini = mini
        self.maxi = maxi
        self.cur = mini

    # Увеличение счетчика на 1 (инкремент)
    def increment(self):
        self.cur += 1
        if self.cur > self.maxi:
            self.cur = self.mini

    def __repr__(self):
        return f'Счетчик(Старт={self.mini}, Финиш={self.maxi})'


if __name__ == '__main__':
    counter = Counter(0, 20)
    print(counter)
    for _ in range(20):
        counter.increment()
        print(counter.cur)
    print('Сброс')
    counter.increment()
    print(counter.cur)

