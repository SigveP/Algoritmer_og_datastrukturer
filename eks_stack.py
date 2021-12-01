""" 
EKSEMPEL Stack

I dette eksemplet bruker jeg Stack(klassen) til
å holde pekere til vinduene som finnes, så når 
Stacken bruker pop() skal det nyeste vinduet bli
borte for det ikke har noen peker. 
Funker egentlig ikke sånn for 
PyQt6.QtWidgets.QApplication har pekere til 
alle vinduene, burde tenkt på det før jeg lagde
eksempelet.
Men syntes det viser hvordan man kan bruke Stack 
selv om jeg valgte litt feil med hva jeg skulle 
ha en peker til.
"""
from datastrukturer import Stack
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from PyQt6.QtGui import QCloseEvent
from sys import argv

# en klasse som arver fra QWidget


class Window(QWidget):
    def __init__(self, num: int) -> None:  # funksjonen som kjører da et objekt er lagd
        super().__init__()  # kjører __init__ funksjonen til den klassen har arvet fra

        self.num = num  # tall
        self.haschild = False  # har et undervindu

        # tekst som viser hvilket tall vinduet har
        label = QLabel(text=f'window = {num}')
        # knapp til å lage et undervindu
        button = QPushButton(text='Create Window')
        # kobler knappen til lag vindu funksjonen
        button.clicked.connect(self.create_window)

        layout = QVBoxLayout()  # en vertikal beholder
        layout.addWidget(label)  # legger teksten inn i beholderen
        layout.addWidget(button)  # legger knappen inn i beholderen
        # gjør beholderen synlig (ikke hva den faktisk gjør)
        self.setLayout(layout)

        self.show()  # viser vinduet

    def create_window(self):  # en metode som lager et undervindu
        if not self.haschild:  # ser om vinduet ikke har et undervindu
            self.haschild = True  # setter har undervindu til sant
            # lager et nytt vindu med et nummer høyere
            windows.append(Window(self.num+1))

    # metode som kjører når brukeren prøver å lukke et vindu (klassen)
    def closeEvent(self, a0: QCloseEvent) -> None:
        if not self.haschild:  # ser om ikke har undervindu
            windows.pop()  # fjerner seg selv fra vindu stabellen (stack)
            # setter forrige vindu sin har undervinduverdi til usant
            windows.peek().haschild = False
            return super().closeEvent(a0)  # fortsetter til den vanlige lukke metoden
        else:  # hvis har undervindu
            a0.ignore()  # holder vinduet åpent


# en stabell (stack) som jeg hadde lyst skulle holde pekere til
# vinduer som automatisk lukker seg uten, men de gjør ikke det
# så de har sikkert en peker i QApplication.
windows = Stack()
app = QApplication(argv)  # styrer alt som har noe med PyQt6 å gjøre

windows.append(Window(0))  # lager et vindu med tallet 0

exit(app.exec())  # lukker programmet da det er ferdig å kjøre
