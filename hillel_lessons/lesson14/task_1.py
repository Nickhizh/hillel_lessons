a, b = input('Введи первое значение: \n'), input('Введи второе значение: \n')

try:
    a = int(a)
    b = int(b)
except:
    a = str(a)
    b = str(b)
print(a+b)

