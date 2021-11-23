num1 = input("Text: ")
num2 = [int(i) for i in arr1]
N = len(num1)
for x in range(0, N):
    for y in range(x + 1, N):
        if num2[x] == num2[y]:
            print("Есть дубли")
            quit()
print("Нет дублей")
