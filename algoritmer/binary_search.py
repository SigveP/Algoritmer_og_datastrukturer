def iterative(array, find):
    left = 0
    right = len(array)
    while left < right:
        middle_index = (left + right) // 2
        middle = array[middle_index]
        if middle == find:
            return middle_index
        elif middle < find:
            left = middle_index
        elif middle > find:
            right = middle_index


def recursive(array, find, left=-1, right=-1):
    if left == -1 and right == -1:
        left = 0
        right = len(array)
    middle_index = (left + right) // 2
    middle = array[middle_index]
    if middle == find:
        return middle_index
    elif middle < find:
        return recursive(array, find, middle_index, right)
    elif middle > find:
        return recursive(array, find, left, middle_index)
