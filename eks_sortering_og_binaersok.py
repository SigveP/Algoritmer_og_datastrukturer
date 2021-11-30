from random import randint
from datastrukturer.sortering import *
import datastrukturer.binarysearch as bins
import requests

# henter data gjennom en api
whiskyapi = requests.get(
    url='https://whiskyhunter.net/api/auctions_data/'
)
# lagrer dataen i en variabel
whiskydata = whiskyapi.json()


# funksjon som henter et bestemt felt i en liste med ordbøker(python hashtable)
# tar inn en liste og en string, og returnerer en liste
def list_from_list_of_dictonaries(data: list, field: str) -> list:
    result = []  # liste som skal returneres
    for entry in data:  # går gjennom
        # henter og legger feltet inn i returneringslisten
        result.append(entry[field])
    return result  # returnerer resultatet


# alle brukelige tallfelt https://whiskyhunter.net/api/auctions_data/ returnerer
all_intfields = (
    'winning_bid_max',
    'winning_bid_mean',
    'winning_bid_min',
    'auction_trading_volume',
    'auction_lots_count'
)
# henter et tilfeldig felt
field = all_intfields[randint(0, len(all_intfields) - 1)]
fieldlist = list_from_list_of_dictonaries(
    whiskydata, field)  # lager en liste med feltet
sorted_fieldlists = {  # en ordbok som inneholder sorterte versjoner av listen (alle burde være like)
    'insertion': insertionsort.iterative(fieldlist.copy()),
    'selection': selectionsort.iterative(fieldlist.copy()),
    'merge': mergesort(fieldlist.copy()),
    'quick': quicksort(fieldlist.copy()),
    'heap': heapsort(fieldlist.copy())
}


def main():  # hovedfunksjon
    # tekst som viser hvilke sorteringer man kan velge mellom
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

    while True:  # while løkke
        x = input('num: ')  # spør brukeren om et tall
        if x == 'q':  # hvis brukeren skrev inn q, stopp løkken
            break  # stopper løkken
        try:
            x = int(x)  # gjør x om til en int

            try:
                x1 = int(input('sort: '))  # henter sorteringsvalget
                # ser om valget er ugyldig
                if not x1 >= 0 and not x < len(sorted_fieldlists):
                    continue  # fortsetter while løkken
            except ValueError:  # går hit bruker ikke har skrevet et tall
                continue  # fortsetter while løkken

            key = list(sorted_fieldlists.keys())[
                x1]  # henter sorteringsnøkkelen
            # ser om tallet brukeren skrev inn er i sorteringslisten de valgte
            if bins.recursive(sorted_fieldlists[key], x):
                # skriver ut at tallet er i listen og hvilken sortering de valge (så de sikker på at sorteringen funker)
                print(f'{x} in {field}!\nsort: {key}\n')

        # kommer hit hvis brukeren ikke har skrevet inn et tall eller at binearsøket ikke fant målet (den returnerer ValueError)
        except ValueError:
            # skriver ut at x ikke er i noen liste
            print(f'{x} not in {field}!\n')
            continue  # fortsetter while løkken


if __name__ == "__main__":  # kjører bare hovedfunksjonen hvis denne filen ble kjørt
    main()  # hovedfunksjon
