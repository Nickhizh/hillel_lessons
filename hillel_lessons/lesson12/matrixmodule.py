"""
Этот модуль экспортирует функцию помогающую подсчитать и вывести
сумму значений каждой строки и столюбца матрицы
M и N значения которой задает пользователь вручную
"""

from random import random


def calcmatrix(m=int(input("M=")), n=int(input("N="))):
    """
    Подсчет значений столбцов и строк в матрице
    """

    a = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(int(random()*11))
            print("%3d" % b[j], end='')
        a.append(b)
        print('   |', sum(b))

    for i in range(m):
        print(" --", end='')
    print()

    for i in range(m):
        s = 0
        for j in range(n):
            s += a[j][i]
        print("%3d" % s, end='')
    print()
