from .maler import LinkedListBase
from .maler import TwoDirNode as Node


class Stack(LinkedListBase):
    def __init__(self, *values) -> None:
        self.start = Node(values[0])
        self.end = self.start
        self.length = 0

        for value in values:
            self.append(value)

    def append(self, value) -> None:
        if self.length < 0:
            self.start = Node(value)
            self.end = self.start
            self.length = 0
            return
        self.end.next = Node(value)
        self.end.next.prev = self.end
        self.end = self.end.next
        self.length += 1

    def pop(self):
        value = self.end.value
        self.end = self.end.prev
        self.end.next = None
        self.length -= 1
        return value

    def peek(self):
        return self.end.value
