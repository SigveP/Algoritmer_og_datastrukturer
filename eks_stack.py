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


class Window(QWidget):
    def __init__(self, num: int) -> None:
        super().__init__()

        self.num = num
        self.haschild = False

        label = QLabel(text=f'window = {num}')
        button = QPushButton(text='Create Window')
        button.clicked.connect(self.create_window)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)

        self.show()

    def create_window(self):
        if not self.haschild:
            self.haschild = True
            windows.append(Window(self.num+1))

    def closeEvent(self, a0: QCloseEvent) -> None:
        if not self.haschild:
            windows.pop()
            windows.peek().haschild = False
            return super().closeEvent(a0)
        else:
            a0.ignore()


windows = Stack()
app = QApplication(argv)

windows.append(Window(0))

exit(app.exec())
