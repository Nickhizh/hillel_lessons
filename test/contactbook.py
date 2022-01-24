import pickle
import os

UI = '''
1. Добавить контакт
2. Все контакты
3. Поиск
4. Изменить контакт
5. Удалить контакт
6. Сохранить и выйти
'''


class Person(object):

    def __init__(self, name=None, surname=None, address=None, phone=None, birthday=None):
        self.name = name
        self.surname = surname
        self.address = address
        self.phone = phone
        self.birthday = birthday

    def __str__(self):
        return "{} {:>15} {:>14} {:>15} {:>15}".format(self.name, self.surname, self.address, self.phone, self.birthday)


class Application(object):

    def __init__(self, database):
        self.database = database
        self.persons = {}
        if not os.path.exists(self.database):
            file_pointer = open(self.database, 'wb')
            pickle.dump({}, file_pointer)
            file_pointer.close()
        else:
            with open(self.database, 'rb') as person_list:
                self.persons = pickle.load(person_list)

    def add(self):
        # Добавить новый контакт
        name, surname, address, phone, birthday = self.getdetails()
        if name not in self.persons:
            self.persons[name] = Person(name, surname, address, phone, birthday)
        else:
            print("Такой контакт уже существует")

    def viewall(self):
        # Просмотреть список контактов
        if self.persons:
            print("{:>5} {:>15} {:>15} {:>15} {:>18}".format('Имя', 'Фамилия', 'Адрес', 'Телефон', 'Дата рождения'))
            for person in self.persons.values():
                print(person)
        else:
            print("Записная книжка пуста")

    def search(self):
        # Поиск по имени
        name = input("Введите имя: ")
        if name in self.persons:
            print(self.persons[name])
        else:
            print("Контакт не найден")

    def getdetails(self):
        # Получение данных для изменения
        name = input("Имя: ")
        surname = input("Фамилия: ")
        address = input("Адрес: ")
        phone = input("Номер телефона:")
        birthday = input("Дата рождения:")
        return name, surname, address, phone, birthday

    def update(self):
        # Изменение контакта
        name = input("Введите имя: ")
        if name in self.persons:
            print("Найдено. Продолжить изменения.")
            name, surname, address, phone, birthday = self.getdetails()
            self.persons[name].__init__(name, surname, address, phone, birthday)
            print("Изменено")
        else:
            print("Контакт не найден")

    def delete(self):
        # Удаление контакта
        name = input("Введите Имя для удаления: ")
        if name in self.persons:
            del self.persons[name]
            print("Контакт удален")
        else:
            print("Контакт не найден")

    def __del__(self):
        with open(self.database, 'wb') as db:
            pickle.dump(self.persons, db)

    def __str__(self):
        return UI


def main():
    app = Application('mycontacts.data')
    choice = ''
    while choice != '7':
        print(app)
        choice = input('Введите цифру: ')
        if choice == '1':
            app.add()
        elif choice == '2':
            app.viewall()
        elif choice == '3':
            app.search()
        elif choice == '4':
            app.update()
        elif choice == '5':
            app.delete()
        elif choice == '6':
            print("Сохранено")
        else:
            print("Неверный ввод.")


if __name__ == '__main__':
    main()
