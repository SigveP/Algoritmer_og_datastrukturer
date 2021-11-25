from datastrukturer import binarysearch as bs
from random import randint

randomlist = [randint(-100, 100) for i in range(1000000)]
inlist = False

print('I have a list with 1.000.000 numbers from -100 to 100\nTry to find one of them.')
while not inlist:
    x = input('\nGuess: ')
    try:
        inlist = bool(bs.recursive(randomlist, int(x)))
        print(f'{x} in list')
        inlist = True
    except ValueError:
        print(f'{x} not in list. try again')
