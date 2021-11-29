user_input = int(input("Input number from 3 to 9: "))
if user_input in range(3, 10):
    for x in range(1, user_input + 1):
        for y in range(1, x - 1):
            print(y, end=" ")
        for y in range(x - 1, 0, -1):
            print(y, end=" ")
        print()
else:
    print("Wrong input")
