import random
# случайный список целый чисел
lst = [random.randint(0, 10) for x in range(10)]

# Для наглядности вывод списка начального
print(lst)

# Вывод нового списка из уникальных чисел
# реверс списка и превращение его в кортеж
print(tuple([x for x in lst if lst.count(x) == 1][::-1]))




