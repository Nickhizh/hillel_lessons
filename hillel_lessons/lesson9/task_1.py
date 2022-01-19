""" Сначала сделал функцию с вводом значений через консоль, но потом перечитал
условие и сделал согласно нему. Часть старого кода закоментил
"""

def findsum(nums, dgt):
    # nums = [int(x) for x in input("Введите числа: ").split()]
    # dgt = int(input("Введите число: "))
    size = len(nums)

    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if nums[i] + nums[j] == dgt:
                print(f"Пары для {dgt} найдены: {nums[i]} и {nums[j]}")
                return True
    print(f"Пары для {dgt} не найдены")
    return False


num1 = [1, 2, 3, 4]
num2 = 6
bom1 = [1, 20, 12, 5, 104, 8]
bom2 = 20


findsum(num1, num2)
findsum(bom1, bom2)
