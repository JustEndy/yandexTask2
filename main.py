import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint

from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False

        self.btn.clicked.connect(self.run)

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, e):
        if self.do_paint:
            try:
                self.do_paint = False
                r = randint(10, 100)
                x, y = randint(10, 490), randint(10, 390)
                qp = QPainter(self)
                qp.begin(self)
                a, b, c = randint(0, 255), randint(0, 255), randint(0, 255)
                qp.setBrush(QColor(a, b, c))
                print(r)
                qp.drawEllipse(x - r, y - r, r*2, r*2)
                print(x - r, y - r, x + r, y + r)
                qp.end()
            except Exception as e:
                print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())