def iterative(array, find):
    left = 0
    right = len(array)

    while left < right:
        middle = (left + right) // 2
        value = array[middle]

        if value == find:
            return middle
        elif left == middle or right == middle:
            raise ValueError(f"{find} not in list")
        elif value < find:
            left = middle
        elif value > find:
            right = middle


def recursive(array, find, left=-1, right=-1):
    if left == -1 and right == -1:
        left = 0
        right = len(array)

    middle = (left + right) // 2
    value = array[middle]

    if value == find:
        return middle
    elif left == middle or right == middle:
        raise ValueError(f"{find} not in list")
    elif value < find:
        return recursive(array, find, middle, right)
    elif value > find:
        return recursive(array, find, left, middle)
