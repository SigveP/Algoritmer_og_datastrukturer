from .maler import LinkedListBase
from .maler import OneDirNode as Node


class LinkedList(LinkedListBase):
    def __init__(self, *values) -> None:
        super().__init__()

        for value in values:
            self.append(value)

    def append(self, value) -> None:
        if self.length < 0:
            self.start = Node(value)
            self.end = self.start
            self.length = 0
            return
        self.end.next = Node(value)
        self.end = self.end.next
        self.length += 1

    def get(self, index: int) -> Node:
        selected = self.start
        for i in range(index-1):
            selected = selected.next
        return selected

    def insert(self, index: int, value):
        if index == 0:
            prev_next = self.start
            self.start = Node(value, prev_next)
            self.length += 1
            return
        node = self.get(index)
        prev_next = node.next
        node.next = Node(value, prev_next)
        self.length += 1

    def pop(self, index: int):
        node = self.get(index)
        value = node.value
        if index == 0:
            self.start = self.start.next
        node.next = node.next.next
        self.length -= 1
        return value
