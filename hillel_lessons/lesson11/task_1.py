import random


def sort_fun():
    # сортируем столбы по возрастанию сумм
    list_sum = [sum([matrix[index_col][i] for index_col in range(m)]) for i in
                range(m)]
    flag = True
    while flag:
        flag = False
        for i in range(m - 1):
            j = i + 1
            if list_sum[i] > list_sum[j]:
                list_sum[i], list_sum[j] = list_sum[j], list_sum[i]
                flag = True
                for line in range(m):
                    matrix[line][i], matrix[line][j] = matrix[line][j], \
                                                       matrix[line][i]

    # сортруем элементы столбцов по условию
    for coll in range(m):
        if not coll % 2:
            flag = True
            while flag:
                flag = False
                for i in range(m - 1):
                    j = i + 1
                    if matrix[i][coll] > matrix[j][coll]:
                        matrix[i][coll], matrix[j][coll] = matrix[j][coll], \
                                                           matrix[i][coll]
                        flag = True
        else:
            flag = True
            while flag:
                flag = False
                for i in range(m - 1):
                    j = i + 1
                    if matrix[i][coll] < matrix[j][coll]:
                        matrix[i][coll], matrix[j][coll] = matrix[j][coll], \
                                                           matrix[i][coll]
                        flag = True
    print("Отсортировано", *matrix, sep='\n')


m = int(input('m = '))

matrix = [[random.randint(1, 50) for j in range(m)] for i in range(m)]

print("До сортировки", *matrix, sep='\n')

print()

sort_fun()

