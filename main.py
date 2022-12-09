from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QPoint
from random import randint
from PyQt5 import uic
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.balls = [] # (x, y, r, color)
        self.btn.clicked.connect(self.process)

    def process(self):
        r = randint(0, 100)
        x, y = randint(r, self.width() - r), randint(r, self.height() - r)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.balls.append((x, y, r, color))
        self.update()

    def paintEvent(self, a0):
        painter = QPainter(self)
        for ball in self.balls: # ball - (pos, r)
            x, y, r, color = ball
            painter.setBrush(QBrush(color))
            painter.drawEllipse(QPoint(x, y), r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())