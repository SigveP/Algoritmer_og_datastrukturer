def largestindex(array: list) -> int:
    result = 0
    max = 0
    for i in range(len(array)):
        if array[i] > max:
            result = i
            max = array[i]
    return result


def heapsort(array: list) -> list:
    for i in range(len(array), 0, -1):
        front = largestindex(array[:i-1])
        array[0], array[front] = array[front], array[0]
        if array[0] > array[i-1]:
            array[0], array[i-1] = array[i-1], array[0]
    return array
