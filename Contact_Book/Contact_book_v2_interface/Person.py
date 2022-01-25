"""
Этот модуль содержит класс Person, который содержит всю информацию о контакте
- Имя
- Номер телефона
- Почта
- Адрес
- День рождения
"""


class Person:

	def __init__(self, name, phone, email, address, birthday):
		"""
		Определяю и объявляю все значения которые должны быть в контакте
		"""
		self.name = name
		self.phone = phone
		self.email = email
		self.address = address
		self.birthday = birthday

	def get_name(self):
		"""
		Доступ к имени контакта, возвращает строковое значение
		"""
		return self.name

	def get_info(self):
		"""
		Возвращает все данные контакта
		"""
		return [self.name, self.phone, self.email, self.address, self.birthday]
