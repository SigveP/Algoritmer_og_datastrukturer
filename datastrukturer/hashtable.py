from .linkedlist import LinkedList


class HashTable:
    def __init__(self) -> None:
        self.table = [False for i in range(8)]

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
        elif self.table[table_index] == False:
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

    def __iter__(self):
        self.iter = [0, 0]
        return self

    def __next__(self):
        value = ()
        if self.iter[0] > 8:
            raise StopIteration
        for i in self.table[self.iter[0]:]:
            if i == False:
                self.iter[0] += 1
                self.iter[1] = 0
                continue
            elif isinstance(i, LinkedList):
                if self.iter[1] > len(i) - 1:
                    self.iter[0] += 1
                    self.iter[1] = 0
                    continue
                else:
                    value = i[self.iter[1]]
                    self.iter[1] += 1
                    break
            else:
                value = i
                self.iter[0] += 1
                self.iter[1] = 0
                break
        if value == ():
            raise StopIteration
        return value

    def __len__(self):
        i = 0
        for j in self:
            i += 1
        return i
