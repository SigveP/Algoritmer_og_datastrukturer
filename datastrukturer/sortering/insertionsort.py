def iterative(array: list) -> list:
    for i in range(1, len(array)):
        value = array[i]
        index = i

        while array[index-1] > value and index:
            array[index] = array[index-1]
            index -= 1
        array[index] = value

    return array


def recursive(array: list, i=1) -> list:
    value = array[i]
    index = i

    while array[index-1] > value and index:
        array[index] = array[index-1]
        index -= 1
    array[index] = value

    if i + 1 < len(array):
        recursive(array, i + 1)
    return array
