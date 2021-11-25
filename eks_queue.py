from datastrukturer import Queue
from os import system
from time import sleep
from functools import partial
from random import randint
import keyboard


class Food:
    def __init__(self) -> None:
        self.new_pos()

    def new_pos(self):
        self.pos = (randint(0, 19), randint(0, 19))


class Worm:
    def __init__(self, length: int, food: Food) -> None:
        self.worm = Queue(*[(0, i) for i in range(length)])
        self.head = (0, length-1)
        self.dir = 0
        self.food = food

    def move(self) -> None:
        if self.dir == 0:
            new_head = ((self.head[0]+1) % 20, self.head[1])
        elif self.dir == 1:
            new_head = (self.head[0], (self.head[1]+1) % 20)
        elif self.dir == 2:
            new_head = ((self.head[0]-1) % 20, self.head[1])
        else:
            new_head = (self.head[0], (self.head[1]-1) % 20)
        self.head = new_head
        self.worm.enqueue(new_head)
        if not new_head == self.food.pos:
            self.worm.dequeue()
        else:
            self.food.new_pos()

    def change_dir(self, r: bool, *args) -> None:
        if r:
            self.dir += 1
        else:
            self.dir -= 1
        self.dir %= 4


def printscreen(blocked: list, food: tuple) -> None:
    visible = [['  ' for j in range(20)] for i in range(20)]
    visible[food.pos[1]][food.pos[0]] = '▒▒'
    for i in blocked:
        visible[i[1]][i[0]] = '██'
    system('cls')
    for i in visible:
        print('|' + ''.join(i) + '|')


f = Food()
w = Worm(5, f)

keyboard.on_release_key('left', partial(w.change_dir, False))
keyboard.on_release_key('right', partial(w.change_dir, True))

system('color 73')

for i in range(32000):
    w.move()
    printscreen(w.worm, f)
    sleep(0.064)
