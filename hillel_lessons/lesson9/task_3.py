s = [x for x in range(1, 101) if x not in [i for sub in [list(range(2 * j, 101, j)) for j in range(2, 100 // 2)] for i in sub]]
print(s)

f = filter(in_function|None)