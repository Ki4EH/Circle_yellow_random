import sys

import random
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.initUI()
        self.ok = False

    def initUI(self):
        self.pushButton.clicked.connect(self.start)

    def start(self):
        self.ok = True

    def paintEvent(self, event):
        if self.ok:
            self.qp = QPainter(self)
            self.qp.begin(self)
            self.draw()
            self.qp.end()
            self.update()

    def draw(self):
        for i in range(random.randint(10, 50)):
            self.qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            x = random.randint(100, 500)
            y = random.randint(100, 500)
            z = random.randint(100, 500)
            v = random.randint(100, 500)
            self.qp.drawEllipse(x, y, z, v)

    def circle(self):
        self.draw = True

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
