"""
Create GUI to interact with User
The function should provide a user interface:

"""
# Importing Modules
import os
import sys
import string
import importlib
import ctypes
from pathlib import Path

from PySide6.QtCore import Qt, QPoint, QRect
from PySide6.QtGui import QGuiApplication, QIcon, QFont, QIntValidator
from PySide6.QtWidgets import QApplication, QPushButton, QTableWidgetItem, \
    QDialog, QLabel, QLineEdit, QTableWidget, QApplication, QMainWindow, QMenuBar, QSizePolicy,\
    QStatusBar, QTabWidget, QWidget

# Do not touch
class gui_main(QDialog):
    def __init__(self, problem):
        super().__init__()

        # Importing problem x-ray file
        module = importlib.import_module("_03_Design_Problems." + problem)
        problem = getattr(module, problem)
        self.p = problem()
        self.sample_size = self.p.sampleSize

        # window title, icon and geometry
        screensize = QGuiApplication.primaryScreen().availableSize()
        width = screensize.width()
        height = screensize.height() - 40
        self.setGeometry(500, 200, 0.33*width, height)
        self.setFixedSize(0.33*width, height)
        self.move(QPoint(0.67*width, 0))
        self.setWindowTitle("User Interface")
        self.setWindowIcon(QIcon(str(Path('../icon.png'))))

        # Need to remove it ----------------------------------------------------------
        self.setWindowIcon(QIcon(str(Path('../../icon.png'))))

        # Run Button and Sample Size
        self.update_button = QPushButton("Update", self)
        self.update_button.setGeometry(QRect(500, 60, 120, 35))
        self.update_button.clicked.connect(self.update_values)

        self.label_sample_size = QLabel("Sample Size:", self)
        self.label_sample_size.setGeometry(QRect(420, 20, 120, 30))
        font = QFont()
        font.setPointSize(10)
        self.label_sample_size.setFont(font)

        self.sample_size_input = QLineEdit("300", self)
        self.onlyInt = QIntValidator()
        self.sample_size_input.setValidator(self.onlyInt)
        self.sample_size_input.setGeometry(QRect(500, 20, 120, 30))

        # Main Tab Windows
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(10, 100, 0.33*width - 20, 401))
        self.DV = QWidget()
        self.DV.setObjectName("DV")
        self.DV.setEnabled(True)
        self.tabWidget.addTab(self.DV, "Design Variables")
        self.QOI_P = QWidget()
        self.QOI_P.setObjectName("QOI_P")
        self.tabWidget.addTab(self.QOI_P, "Quantities of Interest & Parameters")




        print("GUI is called " + str(problem))
        print("D = ", self.p.d)
        print("M = ", self.p.m)
        print("NP = ", self.p.np)

        self.show()

    def update_values(self):
        self.sample_size = self.sample_size_input.text()
        print(self.sample_size)

    def run_gui_main(self):
        print("Need to call SolutionSpace")

# Setting up same icon to show on the task bar
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app = QApplication(sys.argv)
w2 = gui_main("S0001_x_Simple_Transmission")
sys.exit(app.exec())
