def findsum():
    nums = [int(x) for x in input("Введите числа: ").split()]
    dgt = int(input("Введите число: "))
    size = len(nums)

    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if nums[i] + nums[j] == dgt:
                print(f"Пары для {dgt} найдены: {nums[i]} и {nums[j]}")
                return True
    print(f"Пары для {dgt} не найдены")
    return False


findsum()
