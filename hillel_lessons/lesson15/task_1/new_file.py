file_name = input('Создаем файл. Введите название: ')
f = open(file_name, 'w')
while True:
    s = input()
    if s == '':
        break
    f.write(s+'\n')
f.close()
