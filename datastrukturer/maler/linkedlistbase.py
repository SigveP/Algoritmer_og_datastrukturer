class LinkedListBase:
    def __init__(self) -> None:
        self.start = None
        self.end = None
        self.length = -1

    def __len__(self):
        return self.length + 1

    def __getitem__(self, key: int):
        return self.get(key + 1).value

    def __iter__(self):
        self.iternode = self.start
        return self

    def __next__(self):
        if self.iternode != None:
            result = self.iternode.value
            self.iternode = self.iternode.next
            return result
        else:
            raise StopIteration

    def __str__(self) -> str:
        return str([*self])
