# Вариант для одной строчки
# print([x for x in range(2, 101) if not [n for n in range(2, x) if not x % n]])

def findprime():
    for i in range(1, 101):
        deli = []
        for a in range(2, i+1):
            if i % a == 0:
                deli.append(a)
                if len(deli) > 1:
                    break
        if len(deli) == 1:
            print(*deli, sep=", ", end=' ')


findprime()


