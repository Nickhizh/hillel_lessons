import random

lst_1 = [random.randint(0, 50) for i in range(10)]
lst_2 = [random.randint(0, 50) for i in range(10)]
print(len(set([x for x in lst_1 if x in lst_2])))
