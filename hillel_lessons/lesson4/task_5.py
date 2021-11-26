s = input("Ввод: ")
ch = input("Какой символ найти? Ввод: ")

i = s.find(ch)

for x in s:
    print("индекс символа: ", i)
    i = s.find(ch, i + 1)
    if i == -1:
        break
