from datastrukturer import HashTable
from enum import Enum
import tkinter as tk


def load(file: str) -> HashTable:
    ht = HashTable()
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for entry in f:
                entry = entry.split(':')
                ht.add(entry[0], entry[1][:-1])
        return ht
    except:
        return ht


def save(file, ht: HashTable) -> None:
    with open(file, 'w', encoding='utf-8') as f:
        for k, v in ht:
            f.write(f'{k}:{v}\n')


class GetType(Enum):
    add = 0
    update = 1


class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('eks_hashtable')
        self.minsize(300, 100)

        self.hashtable = load('eks_data/eks_hashtable_data')

        self.buttona = tk.Button()  # add
        self.buttonb = tk.Button()  # update value
        self.buttonc = tk.Button()  # save
        self.listbox = tk.Listbox()
        self.scrollbar = tk.Scrollbar()

        self.buttona.configure(text='Add', command=self.add_ht)
        self.buttonb.configure(text='Change', command=self.update_ht)
        self.buttonc.configure(text='Save', command=lambda: save(
            'eks_data/eks_hashtable_data', self.hashtable))
        self.listbox.configure(width=60, yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listbox.yview)

        self.buttona.grid(column=0, row=0, sticky=(tk.W, tk.E))
        self.buttonb.grid(column=1, row=0, sticky=(tk.W, tk.E))
        self.buttonc.grid(column=2, row=0, sticky=(tk.W, tk.E))
        self.listbox.grid(column=0, row=1, columnspan=3)
        self.scrollbar.grid(column=3, row=0, rowspan=2, sticky=(tk.N, tk.S))

        self.update_listbox()

    def update_listbox(self) -> None:
        self.listbox.delete('0', tk.END)
        for i in self.sort(self.hashtable):
            self.listbox.insert(tk.END, i)

    def sort(self, ht: list, recursed: int = 0) -> list:
        if isinstance(ht, HashTable):
            temp = []
            for k, v in ht:
                temp.append(f'{k} - {v}')
            ht = temp
        values = "0123456789abcdefghijklmnopqrstuvwxyzæøå"
        groups = [[] for i in range(len(values))]
        for i in ht:
            for j in values:
                if len(i) <= recursed:
                    break
                elif i[recursed].lower() == j:
                    groups[values.index(j)].append(i)
                    break
        for group in groups:
            for i in group:
                ht.remove(i)
            if len(group):
                ht += self.sort(group, recursed + 1)
        return ht

    def add_ht(self) -> None:
        GetWindow(self, 'Key', GetType.add)

    def update_ht(self) -> None:
        value = self.listbox.get(self.listbox.curselection()).split(' - ')[0]
        GetWindow(self, value, GetType.update)


class GetWindow(tk.Tk):
    def __init__(self, parent: Window, label: str, action: GetType) -> None:
        super().__init__()

        self.title(label)
        self.parent = parent

        if action == GetType.add:
            self.keylabel = tk.Label(self, text=f'{label}: ')
            self.keyentry = tk.Entry(self)
        elif action == GetType.update:
            self.keylabel = tk.Label(self, text=label)
            self.label = label

        self.valuelabel = tk.Label(self, text=f'Value: ')
        self.valueentry = tk.Entry(self)

        if action == GetType.add:
            self.confirmbutton = tk.Button(
                self, text='Confirm', command=self.add)
        elif action == GetType.update:
            self.confirmbutton = tk.Button(
                self, text='Confirm', command=self.update)

        if action == GetType.add:
            self.keylabel.grid(column=0, row=0)
            self.keyentry.grid(column=1, row=0)
        elif action == GetType.update:
            self.keylabel.grid(column=1, row=0)

        self.valuelabel.grid(column=0, row=1)
        self.valueentry.grid(column=1, row=1)

        self.confirmbutton.grid(
            column=0, row=2, columnspan=2, sticky=(tk.W, tk.E))

    def add(self) -> None:
        self.parent.hashtable.add(self.keyentry.get(), self.valueentry.get())
        self.parent.update_listbox()
        self.destroy()

    def update(self) -> None:
        self.parent.hashtable[self.label] = self.valueentry.get()
        self.parent.update_listbox()
        self.destroy()


root = Window()
root.mainloop()
