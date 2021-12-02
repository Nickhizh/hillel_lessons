num = int(input("Ввод числа: "))
for i in range(1, num):
    a = str(i)
    b = str(i ** 2)
    if a == b[-len(a):] and int(a) <= num:
        print(a + "*" + a + "=" + b)
