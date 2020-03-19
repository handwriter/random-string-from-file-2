import random
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog

from design import Ui_Form as Design


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_file)

    def open_file(self):
        try:
            with open(QFileDialog.getOpenFileName()[0], 'r') as text:
                try:
                    self.label.setText(f"{random.choice(text.readlines())}")
                except IndexError:
                    self.label.setText('Ошибка')
        except:
            pass


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())
