"""
Create GUI to interact with User
The function should provide a user interface:

"""
# Importing Modules
import os
import string
import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication, QPushButton, QTableWidgetItem, \
    QDialog, QLabel, QLineEdit, QTableWidget

# Do not touch
class UserInterface(QDialog):
    def __init__(self):
        super().__init__()

        # window title, icon and geometry
        self.setGeometry(500, 200, 400, 400)
        qtRectangle = self.frameGeometry()
        self.move(qtRectangle.bottomLeft())
        self.setFixedSize(400, 400)
        self.setWindowTitle("User Interface")
        print("No window")
        self.show()
        btn1 = QPushButton("Run", self)
        btn1.setGeometry(200, 340, 80, 40)
        btn1.clicked.connect(self.run_merge)

    def run_merge(self):
        self.error1.setText("Please a Select Model")
        self.error1.setGeometry(20, 280, 360, 40)
        self.error1.setStyleSheet("border-radius: 5px; background-color: #D92000")
        self.error1.setAlignment(Qt.AlignCenter)
        self.error1.setHidden(False)

        print("Need to call SolutionSpace")


def gui_main(problem):
    w = UserInterface()
    w.show()
    print("GUI is called " + str(problem[0]))
