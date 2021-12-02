import random
# Способ решения путем вывода общего количества уникальных значений
lst_1 = [random.randint(0, 10) for x in range(5)]
lst_2 = [random.randint(0, 10) for y in range(5)]

print(f" {len([x for x in lst_1 + lst_2 if (lst_1 + lst_2).count(x) == 1])} уникальных значений")

# Способ решения путем вывода  количества уникальных значений для каждого списка
# lst_1 = [random.randint(0, 10) for x in range(5)]
# lst_2 = [random.randint(0, 10) for y in range(5)]

# print(f"В первом списке {len([x for x in lst_1 if lst_1.count(x) == 1 and x not in lst_2])} уникальных значений, "
#       f"а во втором {len([x for x in lst_2 if lst_2.count(x) == 1 and x not in lst_1])}"
#       )












