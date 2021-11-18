def iterative(array: list) -> list:
    for i1 in range(len(array)):
        minindex = i1
        for i2 in range(i1, len(array)):
            if array[i2] < array[minindex]:
                minindex = i2
        temp = array[i1]
        array[i1] = array[minindex]
        array[minindex] = temp
    return array


def recursive(array: list, i: int = 0) -> list:
    minindex = i
    for x in range(i, len(array)):
        if array[x] < array[minindex]:
            minindex = x
    temp = array[i]
    array[i] = array[minindex]
    array[minindex] = temp
    if i < len(array)-1:
        array = recursive(array, i + 1)
    return array
