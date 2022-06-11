"""
Create GUI to interact with User
The function should provide a user interface:

"""
# Importing Modules
import os
import string
import sys
import importlib
from pathlib import Path

from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtWidgets import QApplication, QPushButton, QTableWidgetItem, \
    QDialog, QLabel, QLineEdit, QTableWidget

# Do not touch
class gui_main(QDialog):
    def __init__(self, problem):
        super().__init__()

        # Importing problem x-ray file
        module = importlib.import_module("_03_Design_Problems." + problem)
        problem = getattr(module, problem)
        self.p = problem()

        # window title, icon and geometry
        screensize = QGuiApplication.primaryScreen().availableSize()
        width = screensize.width()
        height = screensize.height() - 40
        self.setGeometry(500, 200, 0.33*width, height)
        self.setFixedSize(0.33*width, height)
        self.move(QPoint(0.67*width, 0))
        self.setWindowTitle("User Interface")
        self.setWindowIcon(QIcon(str(Path('../../icon.png'))))



        print("GUI is called " + str(problem))
        print("D = ", self.p.d)
        print("M = ", self.p.m)
        print("NP = ", self.p.np)

        self.show()

    def run_gui_main(self):
        print("Need to call SolutionSpace")


app = QApplication(sys.argv)
w2 = gui_main("S0001_x_Simple_Transmission")
sys.exit(app.exec())
