# импортирую модуль для упрощенной замены пунктуационных символов
import re

some_string = re.sub(r'[^\w\s]', "", input(" Введите текст: \n"))
some_dict = {}
for key in some_string.split():

    # Перевожу все ключи в нижний регистр и назначаю ключам значения повторений
    key = key.lower()
    some_dict[key] = some_dict.setdefault(key, 0) + 1

for key, value in some_dict.items():
    print(f'Слово "{key}" встречается {value} раз')



