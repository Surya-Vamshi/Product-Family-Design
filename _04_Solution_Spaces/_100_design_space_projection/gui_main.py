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
    QStatusBar, QTabWidget, QWidget, QGridLayout, QSlider, QScrollArea

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
        self.update_button.setStyleSheet("border-radius: 5px; background-color : #66CC00; border-style: outset;"
                                         "border-width: 1px; border-color: black;")
        self.update_button.clicked.connect(self.update_values)

        self.label_sample_size = QLabel("Sample Size:", self)
        self.label_sample_size.setGeometry(QRect(420, 20, 120, 30))
        font = QFont()
        font.setPointSize(10)
        self.label_sample_size.setFont(font)

        self.sample_size_input = QLineEdit(str(self.sample_size), self)
        self.onlyInt = QIntValidator()
        self.sample_size_input.setValidator(self.onlyInt)
        self.sample_size_input.setGeometry(QRect(500, 20, 120, 30))

        # Main Tab Windows
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(QRect(10, 100, 0.33*width - 20, 400))
        self.DV = QWidget()
        self.DV.setObjectName("DV")
        self.DV.setEnabled(True)
        self.tabWidget.addTab(self.DV, "Design Variables")
        self.QOI_P = QWidget()
        self.tabWidget.addTab(self.QOI_P, "Quantities of Interest and Parameters")
        self.tabWidget.setFont(font)

        # Design Variables Tab
        self.DV_scrollArea = QScrollArea(self.DV)
        # self.DV_scrollArea.setGeometry(QRect(10, 10, 0.33*width - 40, 60))
        self.DV_scrollArea.move(10, 10)
        self.DV_scrollArea.setFixedWidth(0.33*width - 40)
        self.DV_scrollArea.setMaximumHeight(60)
        self.DV_scrollArea.setWidgetResizable(True)
        self.DV_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.DV_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.DV_Grid = QGridLayout(self.DV_scrollArea)
        # self.DV_scrollArea.setWidget(self.DV)
        self.DV_Grid.setContentsMargins(0, 0, 0, 0)
        font.setBold(True)

        self.DV_Header_1 = QLabel("X", self.DV)
        self.DV_Header_1.setFont(font)
        self.DV_Grid.addWidget(self.DV_Header_1, 0, 0, 1, 1)
        self.DV_Header_2 = QLabel("X", self.DV)
        self.DV_Header_2.setFont(font)
        self.DV_Grid.addWidget(self.DV_Header_2, 0, 1, 1, 1)
        self.DV_Header_3 = QLabel("X", self.DV)
        self.DV_Header_3.setFont(font)
        self.DV_Grid.addWidget(self.DV_Header_3, 0, 2, 1, 1)


        self.name_1 = QLabel("X", self.DV_scrollArea)
        self.name_1.setFont(font)
        self.DV_Grid.addWidget(self.name_1, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.DV_scrollArea)
        self.DV_Grid.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.DV_scrollArea)
        self.DV_Grid.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.name_2 = QLabel("Name", self.DV_scrollArea)
        self.DV_Grid.addWidget(self.name_2, 1, 0, 1, 1)

        self.horizontalSlider = QSlider(self.DV_scrollArea)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.DV_Grid.addWidget(self.horizontalSlider, 2, 1, 1, 2)




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
w2 = gui_main("S0002_x_Simple_Transmission")
sys.exit(app.exec())
