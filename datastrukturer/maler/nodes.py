class OneDirNode:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class TwoDirNode:
    def __init__(self, value, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
