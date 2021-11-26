num = int(input("Введите число: "))
x1 = num % 10
x = num // 10
flag = 0
while x > 0:
    x2 = x % 10
    if x1 != x2:
        x = x // 10
        x1 = x2
    else:
        flag = 1
        print("Найден примыкающий дубль", x1)
        break
if flag == 0:
    print("Дублей рядом нет")