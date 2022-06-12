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
from PySide6.QtGui import QGuiApplication, QIcon, QFont, QIntValidator, QDoubleValidator
from PySide6.QtWidgets import QApplication, QPushButton, QTableWidgetItem, \
    QDialog, QLabel, QLineEdit, QTableWidget, QApplication, QMainWindow, QMenuBar, QSizePolicy,\
    QStatusBar, QTabWidget, QWidget, QGridLayout, QSlider, QScrollArea, QLayout, QToolBox

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
        # self.setFixedSize(0.33*width, height)
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
        self.onlyDouble = QDoubleValidator()
        self.sample_size_input.setValidator(self.onlyInt)
        self.sample_size_input.setGeometry(QRect(500, 20, 120, 30))

        # Main Tab Windows
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(QRect(10, 100, 0.33*width - 20, 400))
        self.DV = QWidget()
        self.DV.setEnabled(True)
        self.tabWidget.addTab(self.DV, "Design Variables")
        self.QOI_P = QWidget()
        self.tabWidget.addTab(self.QOI_P, "Quantities of Interest and Parameters")
        self.tabWidget.setFont(font)

        # Design Variables Tab
        self.DV_toolboxmain = QToolBox(self.DV)
        self.DV_toolboxmain.setGeometry(QRect(10, 10, 0.33*width - 40, 100))
        self.DV_toolbox = QWidget()

        self.DV_Grid = QGridLayout(self.DV_toolbox)
        self.DV_Grid.setSpacing(10)
        self.DV_Grid.setObjectName(u"DV_Grid")
        self.DV_Grid.setSizeConstraint(QLayout.SetFixedSize)
        self.DV_Grid.setContentsMargins(5, 5, 5, 5)
        font.setBold(True)

        # Headings of the Design variable inputs
        DV_Header1 = QLabel("Name", self.DV)
        DV_Header1.setFont(font)
        self.DV_Grid.addWidget(DV_Header1, 0, 0, 1, 1)
        DV_Header2 = QLabel("Unit", self.DV)
        DV_Header2.setFont(font)
        self.DV_Grid.addWidget(DV_Header2, 0, 1, 1, 1)
        DV_Header3 = QLabel("DS Lower Limit", self.DV)
        DV_Header3.setFont(font)
        self.DV_Grid.addWidget(DV_Header3, 0, 2, 1, 1)
        DV_Header4 = QLabel("Range", self.DV)
        DV_Header4.setFont(font)
        DV_Header4.setAlignment(Qt.AlignCenter)
        self.DV_Grid.addWidget(DV_Header4, 0, 3, 1, 2)
        DV_Header5 = QLabel("DS Upper Limit", self.DV)
        DV_Header5.setFont(font)
        self.DV_Grid.addWidget(DV_Header5, 0, 5, 1, 1)


        # Generating a table with design variables as per X-ray file
        self.name_1 = QLabel("X", self.DV_toolbox)
        self.name_1.setFont(font)
        self.DV_Grid.addWidget(self.name_1, 1, 1, 1, 1)

        self.DS_lower_1 = QLineEdit(str(self.p.x[0]["dsl"]), self)
        self.DS_lower_1.setValidator(self.onlyDouble)
        # self.DS_lower_1.setMaximumWidth(50)
        self.DV_Grid.addWidget(self.DS_lower_1, 1, 2, 1, 1)

        self.horizontalSlider = QSlider(self.DV_toolbox)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.DV_Grid.addWidget(self.horizontalSlider, 2, 1, 1, 2)

        # Testing For loop
        print(len(self.p.y))

        # self.DV_Grid.setRowMinimumHeight(0, 50)
        # self.DV_Grid.setRowMinimumHeight(1, 50)
        self.DV_Grid.setColumnMinimumWidth(0, 100)
        self.DV_Grid.setColumnMinimumWidth(1, 50)


        self.DV_toolboxmain.addItem(self.DV_toolbox, "Select the Design Variable values as per requirement:")
        ##  Tab thing to make sure




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
