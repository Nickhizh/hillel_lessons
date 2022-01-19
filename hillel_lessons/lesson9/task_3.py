# Вариант для одной строчки
print([x for x in range(2, 101) if not [n for n in range(2, x) if not x % n]])

# Вариант функции
def findprime():
    for i in range(1, 101):
        primes = []
        for a in range(2, i+1):
            if i % a == 0:
                primes.append(a)
                if len(primes) > 1:
                    break
        if len(primes) == 1:
            print(*primes, sep=", ", end=' ')


findprime()


