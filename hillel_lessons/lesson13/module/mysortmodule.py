"""
Этот модуль экспортирует набор функций помогающих провести:
Сортировку выбором
Сортировку вставками
Сортировка методом "Пузырька"
"""
__all__ = ["sel", "insertion", "bubble"]


def sel(array):
    """Поиск на необработанном срезе массива или списка минимального значения
    в дальнейшем обмен этого значения с первым элементом необработанного среза.
    На следующем шаге необработанный срез уменьшается на один элемент.
    """
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]


def insertion(arr):
    """Сегментирует список на две части: отсортированную и неотсортированную.
    Перебирает второй сегмент и вставляет текущий элемент
    в правильную позицию первого сегмента.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def bubble(array):
    """Итерация по списку, сравнивая элементы попарно и меняя их местами,
    пока более крупные элементы не «всплывут» в начало списка,
    а более мелкие не останутся на «дне».
    """
    length = len(array)
    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp



