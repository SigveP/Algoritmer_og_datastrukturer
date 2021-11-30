from datastrukturer import Queue
from os import system
from time import sleep
from functools import partial
from random import randint
import keyboard

# en klasse som inneholder en tuple og metode


class Food:
    def __init__(self) -> None:  # kjører da objekt lagd
        self.new_pos()  # metode new_pos

    def new_pos(self):  # gir klassen en ny posisjon
        # setter posisjonen sin til et par tilfeldige tall
        self.pos = (randint(0, 19), randint(0, 19))

# en mark klasse som tar inn lengde og et Food objekt


class Worm:
    def __init__(self, length: int, food: Food) -> None:  # kjører da objekt lagd
        self.worm = Queue(*[(0, i) for i in range(length)]
                          )  # lager en kø (queue)
        self.head = (0, length-1)  # setter hode til siste del i køen
        self.dir = 0  # retning
        self.food = food  # lagrer en peker til Food objektet

    def move(self) -> None:  # bevelgelse metode
        if self.dir == 0:  # ser om skal til høyre
            # lager et nytt hode som er en til høyere (eller helt til venstre)
            new_head = ((self.head[0]+1) % 20, self.head[1])
        elif self.dir == 1:  # ser om skal ned
            new_head = (self.head[0], (self.head[1]+1) %
                        20)  # nytt hode ned (eller topp)
        elif self.dir == 2:  # ser om skal til venstre
            # nytt hode en til venstre (eller helt til høyre)
            new_head = ((self.head[0]-1) % 20, self.head[1])
        else:  # hvis ikke høyre, ned, venstre
            new_head = (self.head[0], (self.head[1]-1) %
                        20)  # nytt hode opp (eller bunn)
        self.head = new_head  # setter det nye hode til egent hode
        self.worm.enqueue(new_head)  # legger hode inn i kroppen
        if not new_head == self.food.pos:  # hvis ikke over Food objektet
            self.worm.dequeue()  # fjerner den første verdien i køen (queue)
        else:  # hvis over Food objektet
            self.food.new_pos()  # Food objekt metode new_pos

    # metode til å bytte retning, tar inn om skal til høyere og
    # det som blir sendt inn av keyboard modulen
    def change_dir(self, r: bool, *args) -> None:
        if r:  # hvis høyre
            self.dir += 1  # roterer retningen mot høyre
        else:
            self.dir -= 1  # roterer retningen mot venstre
        self.dir %= 4  # gjør 4 til 0 og -1 til 3


# funksjon som viser plasseringen til marken og maten i terminalen den
# tar inn en liste av mark deler og mat plasseringen
def printscreen(blocked: list, food: tuple) -> None:
    # lager en 2d liste med dobbel mellomrom på alle verdiene
    visible = [['  ' for j in range(20)] for i in range(20)]
    # endrer mat plasseringens verdi med en halv gjennomsiktig blokk
    visible[food.pos[1]][food.pos[0]] = '▒▒'
    for i in blocked:  # for hver mark del
        visible[i[1]][i[0]] = '██'  # endrer plassering verdi til blokk
    system('cls')  # fjerner alt i terminalen
    for i in visible:  # for hver linje i listen
        print('|' + ''.join(i) + '|')  # skriver ut linjen


f = Food()  # Food objekt
w = Worm(5, f)  # Worm objekt med lengde 5

# kobler venstre piltast til markens change_dir metode
keyboard.on_release_key('left', partial(w.change_dir, False))
# kobler høyere piltast til markens change_dir metode
keyboard.on_release_key('right', partial(w.change_dir, True))

system('color 73')  # endrer terminal fargene

for i in range(32000):  # ikke en while løkke
    w.move()  # beveger marken
    printscreen(w.worm, f)  # skriver ut på terminalen
    sleep(0.064)  # venter 0,064 sekunder
