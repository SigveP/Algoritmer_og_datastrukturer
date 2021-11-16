from .maler import LinkedListBase
from .maler import OneDirNode as Node


class Queue(LinkedListBase):
    def __init__(self, *values) -> None:
        self.start = None
        self.end = None
        self.length = -1

        for value in values:
            self.enqueue(value)

    def enqueue(self, value) -> None:
        if self.length < 0:
            self.start = Node(value)
            self.end = self.start
            self.length = 0
            return
        self.end.next = Node(value)
        self.end.next.prev = self.end
        self.end = self.end.next
        self.length += 1

    def dequeue(self):
        value = self.start.value
        self.start = self.start.next
        self.length -= 1
        return value

    def peek(self):
        return self.start.value
