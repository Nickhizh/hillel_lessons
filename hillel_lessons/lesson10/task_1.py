from datetime import datetime

def time_of_function(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@time_of_function
def linsearch(sequence, look_for):
    for i in range(len(sequence)):
        if sequence[i] == look_for:
            return i
    return -1


@time_of_function
def binsearch(sequence, look_for):
    low = 0
    hight = len(sequence) - 1

    while low <= hight:
        mid = low + hight
        guess = sequence[mid]
        if guess == look_for:
            return mid
        if guess > look_for:
            return mid - 1
        else:
            low = mid + 1
    return None


a = [i for i in range(1, 10000000)]

print(linsearch(a, 9999999))
print(binsearch(a, 9999999))
