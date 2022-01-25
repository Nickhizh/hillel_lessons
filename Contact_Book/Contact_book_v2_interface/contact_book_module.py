"""
Этот модуль ведет работу с txt файлом
	- Извлечение данных
	- Сортировка данных
	- Бинарный поиск
	- Редактура данных
"""

from Person import Person
from tempfile import mkstemp
from shutil import move
import os

people_list = []


def sort_contacts():
	"""
	Этот метод сортирует текстовый файл по имени в алфавитном порядке.
	"""

	parse_file()
	people_list.sort(key=lambda x: x.get_name())

	dir_path = os.path.dirname(os.path.realpath(__file__))
	os.chdir(dir_path)
	file_path = os.path.abspath("contacts.txt")

	fh, abs_path = mkstemp()
	with os.fdopen(fh, 'w') as new_file:
		for p in people_list:
			info_list = p.get_info()
			for x in info_list:
				new_file.write(x+'\n')

	os.remove(file_path)
	move(abs_path, file_path)
	parse_file()


def string_format(l_info):
	"""
	Этот метод форматирует список в строку для использования в граф. интерфейсе
	"""
	output = ''
	output += '\n\n'
	output += '\nИмя: '+l_info[0]
	output += '\nНомер телефона: '+l_info[1]
	output += '\nEmail: '+l_info[2]
	output += '\nАдрес: '+l_info[3]
	output += '\nДата рождения: '+l_info[4][0:2]+'/' +\
		l_info[4][2:4]+'/'+l_info[4][4:len(l_info[4])]
	output += '\n\n'
	return output


def disp_fav():
	"""
	Функция фильтрует все избранные контакты
	в список контактов и возвращает в виде строки.
	"""
	sort_contacts()
	string_output = ''
	fav_list = list(filter(lambda p: p.get_fav() == True, people_list))
	if len(fav_list) == 0:
		return '\n\nУ Вас нет избранных контактов'
	for f in fav_list:
		string_output = string_format(f.get_info()) 
	return string_output


def search(name):
	"""
	Этот метод определяет, есть ли человек в книге контактов,
	вызывает метод бинарного поиска и возвращает соответствующий ответ
	"""
	string_output = ''
	try:
		person = search_name(name)
		string_output = string_format(person.get_info())
	except:
		string_output = '\n\nКонтакт НЕ найден! Попробуйте еще раз.\n\n'
	return string_output


def search_name(name): 
	"""
	Бинарный поиск контакта по имени
	"""
	sort_contacts()
	arr = people_list
	var1 = len(people_list)-1
	var2 = 0
	x = name
	while var2 <= var1:

		mid = var2 + (var1 - var2)//2

		if arr[mid].get_name() == x:
			return arr[mid]
		elif arr[mid].get_name() < x: 
			var2 = mid + 1
		else:
			var1 = mid - 1
	return -1


def add_contact(list_info):
	"""
	Добавление нового контакта
	"""
	f = open("contacts.txt", "a")
	for x in list_info:
		f.write(x + '\n')
	f.close()
	sort_contacts()


def replace(file_path, pattern, subst, start=0):
	"""
	Вспомогательный метод, созданный для редактирования файла.
	"""

	fh, abs_path = mkstemp()
	ctr = 0
	with os.fdopen(fh, 'w') as new_file:
		with open(file_path) as old_file:
			for line in old_file:
				if ctr >= start:
					new_file.write(line.replace(pattern, subst))
				else:
					new_file.write(line)
				ctr += 1

	os.remove(file_path)
	move(abs_path, file_path)


def edit(name, list_info):
	"""
	Функция вносит правки в существующий контакт
	"""
	sort_contacts()
	names = []
	for p in people_list:
		names.append(p.get_name())
	i = names.index(name)
	start = i * 5

	dir_path = os.path.dirname(os.path.realpath(__file__))
	os.chdir(dir_path)
	file_path = os.path.abspath("contacts.txt")

	old_info = search_name(name).get_info()
	for indx in range(0, 5):
		if list_info[indx] != '':
			replace(file_path, old_info[indx], list_info[indx], start)


def get_names(word):
	sort_contacts()
	names = []
	for p in people_list:
		if word.lower() in p.get_name().lower():
			names.append(p.get_name())
	return names


def parse_file():
	"""
	Эта функция парсит файл contact.txt.
	"""
	global people_list
	people_list = []
	with open('contacts.txt', 'r') as f:
		f_contents = f.readlines()
		while len(f_contents) > 4:
			name = f_contents.pop(0).strip()
			phone = f_contents.pop(0).strip()
			email = f_contents.pop(0).strip()
			address = f_contents.pop(0).strip()
			birthday = f_contents.pop(0).strip()
			p = Person(name, phone, email, address, birthday)
			people_list.append(p)


if __name__ == '__main__':
	pass
