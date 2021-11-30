# import random
# num_for_guess = random.choice(range(1, 101))
#
# attempt = 0
# user_input = 0
#
# while user_input != num_for_guess:
#     user_input = int(input("Отгадай число в диапазоне от 1 до 100: "))
#     if user_input > 100 or user_input.isalpha():
#         print("no")
#     attempt += 1
#     if user_input < num_for_guess:
#         print(f"Попытка № {attempt}. Ваше число меньше загаданного, попробуйте еще раз")
#     elif user_input > num_for_guess:
#         print(f"Попытка № {attempt}. Ваше число больше загаданного, попробуйте еще раз")
# print(f"Верно! ты угадал с {attempt} раза")
user_input = int(input("  "))
x = user_input.isalpha('a')
print(x)