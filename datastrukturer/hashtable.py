from .linkedlist import LinkedList


class HashTable:
    def __init__(self) -> None:
        self.table = [i for i in range(8)]

    def hash(self, key) -> int:
        key = hash(key)
        return key % 8

    def convert(self, index: int) -> None:
        row = self.table[index]
        self.table[index] = LinkedList(row)

    def add(self, key, value):
        table_index = self.hash(key)
        if isinstance(self.table[table_index], LinkedList):
            self.table[table_index].append((key, value))
        elif isinstance(self.table[table_index], tuple):
            self.convert(table_index)
            self.table[table_index].append((key, value))
        else:
            self.table[table_index] = (key, value)

    def get(self, key):
        table_index = self.hash(key)
        if isinstance(self.table[table_index], LinkedList):
            linkedlist = self.table[table_index]
            for row in linkedlist:
                if row[0] == key:
                    item = row
                    break
        elif isinstance(self.table[table_index], tuple):
            item = self.table[table_index]
        else:
            raise KeyError
        return item

    def setvalue(self, key, value):
        table_index = self.hash(key)
        if isinstance(self.table[table_index], LinkedList):
            i = 0
            for item in self.table[table_index]:
                if item[0] == key:
                    break
                i += 1
            self.table[table_index].pop(i)
            self.table[table_index].insert(i, (key, value))
        elif isinstance(self.table[table_index], tuple):
            self.table[table_index] = (key, value)
        else:
            raise KeyError

    def __getitem__(self, key):
        return self.get(key)[1]

    def __setitem__(self, key, value):
        self.setvalue(key, value)
