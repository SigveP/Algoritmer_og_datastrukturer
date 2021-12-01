""" 
EKSEMPEL HashTable

I dette eksempelet lar jeg egentlig bare brukeren
gjøre hva de vil med en HashTable, den blir kjørt
i et vindu og kan også lagres, tilfelle de vil 
fortsette på den senere.
"""
from datastrukturer import HashTable
from enum import Enum
import tkinter as tk

# tar inn en filbane og laster inn en lagret HashTable


def load(file: str) -> HashTable:
    ht = HashTable()  # lager en HashTable
    try:
        with open(file, 'r', encoding='utf-8') as f:  # åpner filen i lese funskjon
            for entry in f:  # for hver linje i filen
                entry = entry.split(':')  # deler innholdet i to
                # legger det inn i HashTable-en
                ht.add(entry[0], entry[1][:-1])
        return ht  # returnerer HashTable-en
    except:  # hvis ikke kunne åpne fil (eller en annen feil)
        return ht  # returnerer den tomme HashTable-en

# funksjon til å lagre en HashTable
# den tar inn filbane til hvor den skal lagres og en Hashtable


def save(file, ht: HashTable) -> None:
    with open(file, 'w', encoding='utf-8') as f:  # åpner filbanen som skriv
        for k, v in ht:  # for nøkkel og verdi i HashTable-en
            f.write(f'{k}:{v}\n')  # skriver "{nøkkel}:{verdi}\n" inn i filen

# lager et Enum som heter GetType


class GetType(Enum):
    add = 0
    update = 1

# lager en klasse som arver fra Tk klassen til tkinter


class Window(tk.Tk):
    def __init__(self) -> None:  # Kjører da objekt lagd
        super().__init__()  # kjører __init__ metoden til Tk

        self.title('eks_hashtable')  # toppteksten til vinduet
        self.minsize(300, 100)  # minimum størrelsen til vinduet

        # prøver å laste inn en HashTable fra "eks_data/eks_hashtable_data"
        self.hashtable = load('eks_data/eks_hashtable_data')

        self.buttona = tk.Button()  # add
        self.buttonb = tk.Button()  # update value
        self.buttonc = tk.Button()  # save
        self.listbox = tk.Listbox()  # listeboks
        self.scrollbar = tk.Scrollbar()  # rullefelt (i følge google translate)

        # kobler knapp a til legg til metoden
        self.buttona.configure(text='Add', command=self.add_ht)
        # kobler knapp b til verdi endringsmetoden
        self.buttonb.configure(text='Change', command=self.update_ht)
        self.buttonc.configure(text='Save', command=lambda: save(
            'eks_data/eks_hashtable_data', self.hashtable))  # kobler knapp c til lagre funksjonen
        # kobler listeboksen til rullefeltet
        self.listbox.configure(width=60, yscrollcommand=self.scrollbar.set)
        # kobler rullefeltet til listeboksen
        self.scrollbar.configure(command=self.listbox.yview)

        # plasserer knapp a strekt ut på 0:0
        self.buttona.grid(column=0, row=0, sticky=(tk.W, tk.E))
        # plasserer knapp b strekt ut på 1:0
        self.buttonb.grid(column=1, row=0, sticky=(tk.W, tk.E))
        # plasserer knapp c strekt ut på 2:0
        self.buttonc.grid(column=2, row=0, sticky=(tk.W, tk.E))
        # plasserer listeboksen på 0-3:1
        self.listbox.grid(column=0, row=1, columnspan=3)
        # plasserte rullefeltet strekt ut fra topp til bunn på 3:0-1
        self.scrollbar.grid(column=3, row=0, rowspan=2, sticky=(tk.N, tk.S))

        self.update_listbox()  # metode update_listbox

    # metode som oppdaterer listeboksen med å slette alt innholdet og plassere inn det nye innholdet
    def update_listbox(self) -> None:
        self.listbox.delete('0', tk.END)  # tømmer listeboksen
        for i in self.sort(self.hashtable):  # for hver i metode sort med HashTable
            # plasserer verdien på slutten av listeboksen
            self.listbox.insert(tk.END, i)

    # metode for å sortere HashTable-er
    # den tar inn en list eller HashTable og hvor mange rekursjoner den er på
    def sort(self, ht: list, recursed: int = 0) -> list:
        if isinstance(ht, HashTable):  # ser om ht er HashTable
            temp = []  # liste
            for k, v in ht:  # for nøkkel, verdi i ht (HashTable)
                # legger "{nøkkel} - {verdi}" inn i temp
                temp.append(f'{k} - {v}')
            ht = temp  # gjør ht til temp
        # verdiene det blir sortert etter
        values = "0123456789abcdefghijklmnopqrstuvwxyzæøå"
        groups = [[] for i in range(len(values))]  # en liste per verdi
        for i in ht:  # for hver i ht (liste)
            for j in values:  # for hver i verdiene
                if len(i) <= recursed:  # hvis i er kortere enn ganger rekursert
                    break  # til neste i
                elif i[recursed].lower() == j:  # hvis i[rekursjon] er j
                    # verdiens gruppe legger til i
                    groups[values.index(j)].append(i)
                    break  # til neste i
        for group in groups:  # for hver gruppe
            for i in group:  # for hver verdi i gruppe
                ht.remove(i)  # ht (liste) fjern verdi
            if len(group):  # hvis gruppe ikke er tom
                # ht (liste) legger til metode sort med gruppe og rekursert + 1
                ht += self.sort(group, recursed + 1)
        return ht  # returnerer ht (liste)

    # metode for å legge til en ny verdi
    def add_ht(self) -> None:
        # lager et vindu for å legge til en verdi
        GetWindow(self, 'Key', GetType.add)

    # metode for å endre en verdi
    def update_ht(self) -> None:
        # henter vendien brukeren har trykket på
        value = self.listbox.get(self.listbox.curselection()).split(' - ')[0]
        # lager et vindu for å endre verdi
        GetWindow(self, value, GetType.update)

# vindu som arver fra Tk, som er til å legge til og endre verdier
# den tar in overvinduet, en tekst og en GetType


class GetWindow(tk.Tk):
    def __init__(self, parent: Window, label: str, action: GetType) -> None:
        super().__init__()  # kjører __init__ metoden til Tk

        self.title(label)  # setter toppteksten til label
        self.parent = parent  # pekker overvinduet variablen ditt den skal

        if action == GetType.add:  # hvis skal legge til verdi
            self.keylabel = tk.Label(self, text=f'{label}: ')  # tekst
            self.keyentry = tk.Entry(self)  # felt
        elif action == GetType.update:  # hvis skal endre verdi
            self.keylabel = tk.Label(self, text=label)  # tekst
            self.label = label  # string

        self.valuelabel = tk.Label(self, text=f'Value: ')  # tekst
        self.valueentry = tk.Entry(self)  # felt

        if action == GetType.add:  # hvis legg inn
            self.confirmbutton = tk.Button(
                self, text='Confirm', command=self.add)  # knapp koblet til metode add
        elif action == GetType.update:  # hvis endre
            self.confirmbutton = tk.Button(
                self, text='Confirm', command=self.update)  # knapp koblet til metode update

        if action == GetType.add:  # hvis legg inn
            self.keylabel.grid(column=0, row=0)  # plasserer tekst
            self.keyentry.grid(column=1, row=0)  # plasserer felt
        elif action == GetType.update:  # hvis endre
            self.keylabel.grid(column=1, row=0)  # plaserer tekst

        self.valuelabel.grid(column=0, row=1)  # plasserer tekst
        self.valueentry.grid(column=1, row=1)  # plasserer felt

        self.confirmbutton.grid(
            column=0, row=2, columnspan=2, sticky=(tk.W, tk.E))  # plasserer knapp

    # legg til metode
    def add(self) -> None:
        # henter data fra feltene og legger de inn i overvinduets HashTable
        self.parent.hashtable.add(self.keyentry.get(), self.valueentry.get())
        self.parent.update_listbox()  # oppdaterer overvinduets listeboks
        self.destroy()  # fjerner seg selv

    # endre metode
    def update(self) -> None:
        # setter den valgte verdien i overvinduets verdi til verdi feltet
        self.parent.hashtable[self.label] = self.valueentry.get()
        self.parent.update_listbox()  # oppdaterer overvinduets listeboks
        self.destroy()  # fjerner seg selv


root = Window()  # lager et vindu
root.mainloop()  # kjører vinduet
