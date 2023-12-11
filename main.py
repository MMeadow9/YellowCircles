import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.do_paint = False
        print(self.pushButton.size())

        self.circles = []

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        color = QColor(randint(235, 255), randint(200, 245), randint(0, 40))
        qp.setBrush(color)
        diameter = randint(15, 200)
        circle = (randint(0, 690), randint(161, 380), diameter, diameter)
        self.circles.append((circle, color))
        [(qp.setBrush(circle[1]), qp.drawEllipse(*circle[0]))
         for circle in self.circles]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())