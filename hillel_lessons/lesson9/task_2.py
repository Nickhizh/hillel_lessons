print(list(map(lambda x, y=2: x ** y,
               [int(i) for i in input("Введите числа: ").split()])))
