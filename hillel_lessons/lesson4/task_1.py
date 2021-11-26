num1 = list(input("Введите число: "))
num2 = [int(x) for x in num1]

flag = 0
for x in range(0, 10):
    y = num2.count(x)
    if y > 1:
        print("Найден дубль")
        flag = 1
        break

if flag == 0:
    print("Дубль не найден")
