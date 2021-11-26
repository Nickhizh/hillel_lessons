num = input("Введите число: ")
flag = 0
for i in range(len(num) - 1):
    if num[i] == num[i + 1]:
        print("Найдены примыкающие дубли")
        flag = 1
        break
if flag == 0:
    print("Примыкающие дубли не найдены")
