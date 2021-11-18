def mergesort(array: list) -> list:
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    x1 = mergesort(array[:middle])
    x2 = mergesort(array[middle:])
    arrayindex = 0
    while True:
        if not len(x1):
            array[arrayindex:] = x2
            break
        elif not len(x2):
            array[arrayindex:] = x1
            break
        elif x1[0] < x2[0]:
            array[arrayindex] = x1.pop(0)
        else:
            array[arrayindex] = x2.pop(0)
        arrayindex += 1
    return array
