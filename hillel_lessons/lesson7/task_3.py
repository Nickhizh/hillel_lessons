some_string = input("Введите текст для подсчета повторяющихся слов: \n")
some_dict = {}

for key in some_string.split():
    key = key.lower()
    some_dict[key] = some_dict.setdefault(key, 0) + 1

for key, value in some_dict.items():
    print(f'Слово "{key}" встречается {value} раз')



