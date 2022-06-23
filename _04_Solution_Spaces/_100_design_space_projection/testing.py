from PySide6.QtWidgets import (QWidget, QRadioButton, QHBoxLayout, QVBoxLayout,
                                QLabel, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        rb1 = QRadioButton("Large", self)
        rb1.toggled.connect(self.updateLabel)

        rb2 = QRadioButton("Middle", self)
        rb2.toggled.connect(self.updateLabel)

        rb3 = QRadioButton("Small", self)
        rb3.toggled.connect(self.updateLabel)

        self.label = QLabel('', self)

        vbox.addWidget(rb1)
        vbox.addWidget(rb2)
        vbox.addWidget(rb3)

        vbox.addSpacing(15)

        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QRadioButton')
        self.show()

    def updateLabel(self, value):
        rbtn = self.sender()

        if rbtn.isChecked() == True:
            self.label.setText(rbtn.text())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()