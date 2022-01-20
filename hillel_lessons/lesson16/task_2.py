class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # В задании указано что должен быть атрибут с оценками, я вывел это как
    # кол-во выполненных ДЗ
    def __repr__(self):
        return f"{self.name} {self.age} года. " \
               f"Выполнено {self.grade}\\20 домашних заданий "


class Group:
    lst = [
        Student("Владимир", 22, 10),
        Student("Екатерина", 20, 14),
        Student("Мария", 21, 18),
        Student("Алексей", 48, 20),
        Student("Михаил", 21, 2),
        ]


print(Group.lst)

