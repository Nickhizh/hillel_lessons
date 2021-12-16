print([x for x in range(1, 101) if not [n for n in range(2, x) if not x % n]])
