class MyError(Exception):
    def __init__(self, text):
        self.txt = text

a = input("Введите положительное число: ")

try:
    a = int(a)
    if a < 0:
        raise MyError("Вы ввели отрицательное число")
except ValueError:
    print("Ошибка.Вы ввели не число")
except MyError as mr:
    print(mr)
else:
    print(a)