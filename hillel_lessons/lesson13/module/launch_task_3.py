from random import randint
import mysortmodule

a = []
for i in range(10):
    a.append(randint(1, 99))

print(a)
mysortmodule.bubble(a)
print(a)

help(mysortmodule)
