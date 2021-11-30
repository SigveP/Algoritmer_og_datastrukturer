from random import randint
from datastrukturer.sortering import *
import datastrukturer.binarysearch as bins
import requests

whiskyapi = requests.get(
    url='https://whiskyhunter.net/api/auctions_data/'
)
whiskydata = whiskyapi.json()


def list_from_list_of_dictonaries(data: list, field: str) -> list:
    result = []
    for entry in data:
        result.append(entry[field])
    return result


all_intfields = (
    'winning_bid_max',
    'winning_bid_mean',
    'winning_bid_min',
    'auction_trading_volume',
    'auction_lots_count'
)
field = all_intfields[randint(0, len(all_intfields) - 1)]
fieldlist = list_from_list_of_dictonaries(whiskydata, field)
sorted_fieldlists = {
    'insertion': insertionsort.iterative(fieldlist.copy()),
    'selection': selectionsort.iterative(fieldlist.copy()),
    'merge': mergesort(fieldlist.copy()),
    'quick': quicksort(fieldlist.copy()),
    'heap': heapsort(fieldlist.copy())
}


def main():
    print(
        f'Try to find an entry in the {field} from whiskyhunter!',
        '-'*50,
        'Available sorts:',
        '  0. insertion',
        '  1. selection',
        '  2. merge',
        '  3. quick',
        '  4. heap',
        sep='\n',
        end='\n\n'
    )

    while True:
        x = input('num: ')
        if x == 'q':
            break
        try:
            x = int(x)

            try:
                x1 = int(input('sort: '))
                if not x1 >= 0 and not x < len(sorted_fieldlists):
                    continue
            except ValueError:
                continue

            key = list(sorted_fieldlists.keys())[x1]
            if bins.recursive(sorted_fieldlists[key], x):
                print(f'{x} in {field}!\nsort: {key}\n')

        except ValueError:
            print(f'{x} not in {field}!\n')
            continue


if __name__ == "__main__":
    main()
