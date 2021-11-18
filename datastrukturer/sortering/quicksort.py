def partition(array: list, l, h) -> list:
    pivot = array[h]
    i = l

    for j in range(l, h):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[h] = array[h], array[i]
    return i


def quicksort(array: list, l=-1, h=-1) -> list:
    if l == -1 and h == -1:
        l = 0
        h = len(array) - 1
    if l < h:
        pi = partition(array, l, h)

        quicksort(array, l, pi - 1)
        quicksort(array, pi + 1, h)
    return array
