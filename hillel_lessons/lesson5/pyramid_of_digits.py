user_input = input("Input number from 3 to 9: ")                 # Ввод пользователя

if user_input.isdigit() and int(user_input) in range(3, 10):     # Проверка на верность ввода
    for x in range(1, int(user_input) + 1):                      # Перебор значений от 1 до ввода пользователя
        for y in range(1, x + 1):                                # Вывод чисел в выбранном диапазоне
            print(y, end="")
        for y in range(x - 1, 0, -1):                            # Зеркальный вывод тех же чисел в том же ряду
            print(y, end="")
        print()                                                  # Для того чтобы след. итерация была в новой строке
else:
    print("Wrong input. Use only number in range 3 to 9")        # Сообщение при не верном вводе



