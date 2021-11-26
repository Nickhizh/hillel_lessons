num1 = list(input("Введите число: "))
num2 = [int(x) for x in num1]

trigger = 0
for x in range(0, 10):
    y = num2.count(x)
    if y > 1:
        print("Найден дубль")
        trigger = 1
        break

if trigger == 0:
    print("Дубль не найден")