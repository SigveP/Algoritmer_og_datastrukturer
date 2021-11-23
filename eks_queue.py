from datastrukturer import Queue
from os import system
from time import sleep
from random import randint


class Worm:
    def __init__(self, length: int) -> None:
        self.worm = Queue(*[(0, i) for i in range(length)])
        self.head = (0, length-1)
        self.length = length
        self.dir = 0

    def move(self) -> None:
        if self.dir == 0:
            new_head = ((self.head[0]+1) % 20, self.head[1])
        elif self.dir == 1:
            new_head = (self.head[0], (self.head[1]+1) % 20)
        elif self.dir == 3:
            new_head = ((self.head[0]-1) % 20, self.head[1])
        else:
            new_head = (self.head[0], (self.head[1]-1) % 20)
        self.head = new_head
        self.worm.enqueue(new_head)
        self.worm.dequeue()

    def change_dir(self, r: bool) -> None:
        if r:
            self.dir += 1
        else:
            self.dir -= 1
        self.dir %= 4


def printscreen(blocked: list) -> None:
    visible = [['  ' for j in range(20)] for i in range(20)]
    for i in blocked:
        visible[i[1]][i[0]] = '▒▒'
    for i in visible:
        print(''.join(i))


w = Worm(10)
for i in range(32000):
    system('cls')
    if not randint(0, 9):
        w.change_dir((True, False)[randint(0, 1)])
    w.move()
    printscreen(w.worm)
    sleep(0.032)
