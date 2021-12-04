# Ввод пользователя
user_input = input("Input number from 3 to 9: ")
# Проверка на верность ввода
if user_input.isdigit() and int(user_input) in range(3, 10):

    # Перебор значений от 1 до ввода пользователя
    for x in range(1, int(user_input) + 1):

        # Вывод чисел в выбранном диапазоне
        for y in range(1, x + 1):
            print(y, end="")
        # Зеркальный вывод тех же чисел в том же ряду
        for y in range(x - 1, 0, -1):
            print(y, end="")
        # Для того чтобы след. итерация была в новой строке
        print()

# Сообщение при не верном вводе
else:
    print("Wrong input. Use only number in range 3 to 9")
