import random

# lst_1 = [random.randint(0, 10) for x in range(5)]
# lst_2 = [random.randint(0, 10) for y in range(5)]
# print(lst_1)
# print(lst_2)
# print([z for z in lst_1 if z not in lst_2])
# print(len([z for z in lst_1 if z not in lst_2]))

# print(list(set(lst_1)))

lst_1 = [1, 3, 3]
lst_2 = [1, 5, 4]
print(f"В lst_1 {len([z for z in lst_1 if z not in lst_2])} уникальных цифры, а в lst_2 {len([z for z in lst_2 if z not in lst_1])}")

