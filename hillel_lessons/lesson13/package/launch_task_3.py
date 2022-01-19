import mypack
from random import randint

mypack.joke1()
mypack.joke2()
mypack.joke3()


a = []
for i in range(10):
    a.append(randint(1, 99))

print(a)
mypack.bubble(a)
print(a)
