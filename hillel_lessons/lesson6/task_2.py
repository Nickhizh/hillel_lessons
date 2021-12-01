import random

my_list = [random.randint(0, 50) for i in range(10)]        # Формирование случайного списка
print(my_list)

k = C = int(input("Введите число от 0 до 10: "))            # k, С - индекс и значение
my_list.append(1)                                           # Добавляется значение в конец списка
for i in range(len(my_list) - 1, k, -1):                    # Сдвиг влево
    my_list[i] = my_list[i - 1]
my_list[k] = C                                              # Замена значения по индексу k на значение C
print(my_list)
