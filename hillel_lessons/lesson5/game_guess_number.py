import random
# Программа загадывает число
num_for_guess = random.choice(range(1, 101))

# Счетчик попыток
attempt = 0

# Цикл длится до тех пор пока ввод пользователя не будет равен загаданному числу
while True:
    user_input = input("Отгадай число в диапазоне от 1 до 100: ")

# Проверка на соответствие ввода нужным параметрам
    if user_input.isdigit() and int(user_input) <= 100:
        attempt += 1

# Вывод информации о том, введеное число больше или меньше.
        if int(user_input) < num_for_guess:
            print(f"Попытка № {attempt}. "
                  f"Ваше число меньше загаданного, попробуйте еще раз"
                  )
        elif int(user_input) > num_for_guess:
            print(f"Попытка № {attempt}. "
                  f"Ваше число больше загаданного, попробуйте еще раз"
                  )
        else:
            print(f"Верно! ты угадал с {attempt} раза")
            break
# Сообщение если ввод содержит буквы или цифру больше 100
    else:
        print("Введено неправильное значение")

