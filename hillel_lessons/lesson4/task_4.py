n = input("ведите слова через пробел: ")
s = n.split(" ")
y = s[0]
f = s[1]
r = y[::-1]
u = f[::-1]

if len(s) == 2:
    print(r.title(), u.title())
else:
    print("Неверный ввод")
