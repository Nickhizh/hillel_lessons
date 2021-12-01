import random

my_list = [random.randint(0, 50) for i in range(10)]        # Формирование случайного списка

print(my_list)
k = int(input("Введите число от 0 до 10: "))                # Ввод индекса
for i in range(k + 1, len(my_list)):                        # Сдвиг влево
    my_list[i - 1] = my_list[i]
my_list.pop()                                               # Удаление последнего элемента списка
print(my_list)



