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
        DV_Grid_Width = 0.33 * width - 40
        self.DV_toolboxmain.setGeometry(QRect(10, 10, DV_Grid_Width, 350))
        self.DV_toolbox = QWidget()

        self.DV_Grid = QGridLayout(self.DV_toolbox)
        self.DV_Grid.setSpacing(10)
        self.DV_Grid.setObjectName(u"DV_Grid")
        self.DV_Grid.setSizeConstraint(QLayout.SetFixedSize)
        # self.DV_Grid.setContentsMargins(5, 5, 25, 25)
        font.setBold(True)

        # Headings of the Design variable inputs
        DV_Header1 = QLabel("Name", self.DV)
        DV_Header1.setFont(font)
        self.DV_Grid.addWidget(DV_Header1, 0, 0, 1, 1)
        DV_Header2 = QLabel("Unit", self.DV)
        DV_Header2.setFont(font)
        self.DV_Grid.addWidget(DV_Header2, 0, 1, 1, 1)
        DV_Header3 = QLabel("DS Lower\nLimit", self.DV)
        DV_Header3.setAlignment(Qt.AlignCenter)
        DV_Header3.setFont(font)
        self.DV_Grid.addWidget(DV_Header3, 0, 2, 1, 1)
        DV_Header4 = QLabel("Range", self.DV)
        DV_Header4.setFont(font)
        DV_Header4.setAlignment(Qt.AlignCenter)
        DV_Header4.setFixedWidth(DV_Grid_Width*0.4)
        self.DV_Grid.addWidget(DV_Header4, 0, 3, 1, 2)
        DV_Header5 = QLabel("DS Upper\nLimit", self.DV)
        DV_Header5.setAlignment(Qt.AlignCenter)
        DV_Header5.setFont(font)
        self.DV_Grid.addWidget(DV_Header5, 0, 5, 1, 1)


        # Generating a table with design variables as per X-ray file
        x_size = len(self.p.x)
        for i in range(0, x_size):
            DV_name = QLabel(self.p.x[i]["name"])
            DV_name.setFixedWidth(DV_Grid_Width*0.175)
            self.DV_Grid.addWidget(DV_name, 2*i+1, 0, 2, 1)
            setattr(self.DV_Grid, self.p.x[i]["name"], DV_name)

        for i in range(0, x_size):
            DV_unit = QLabel(self.p.x[i]["unit"])
            DV_unit.setFixedWidth(DV_Grid_Width*0.075)
            self.DV_Grid.addWidget(DV_unit, 2*i+1, 1, 2, 1)
            setattr(self.DV_Grid, "unit" + str(i), DV_unit)

        for i in range(0, x_size):
            DV_dsl = QLineEdit(str(self.p.x[i]["dsl"]))
            DV_dsl.setMaximumWidth(DV_Grid_Width*0.1)
            self.DV_Grid.addWidget(DV_dsl, 2*i+1, 2, 2, 1)
            setattr(self.DV_Grid, "dsl" + str(i), DV_dsl)

        for i in range(0, x_size):
            DV_l = QLineEdit(str(self.p.x[i]["l"]))
            DV_l.setMaximumWidth(DV_Grid_Width*0.15)
            self.DV_Grid.addWidget(DV_l, 2*i+1, 3, 1, 1)
            setattr(self.DV_Grid, "l" + str(i), DV_l)

        for i in range(0, x_size):
            DV_range = QSlider()
            DV_range.setOrientation(Qt.Horizontal)
            # DV_range.
            DV_range.setMaximumWidth(DV_Grid_Width*0.5)
            self.DV_Grid.addWidget(DV_range, 2*i+2, 3, 1, 2)
            setattr(self.DV_Grid, "range" + str(i), DV_range)

        for i in range(0, x_size):
            DV_u = QLineEdit(str(self.p.x[i]["u"]))
            DV_u.setMaximumWidth(DV_Grid_Width*0.15)
            self.DV_Grid.addWidget(DV_u, 2*i+1, 4, 1, 1)
            setattr(self.DV_Grid, "u" + str(i), DV_u)

        for i in range(0, x_size):
            DV_dsu = QLineEdit(str(self.p.x[i]["dsu"]))
            DV_dsu.setMaximumWidth(DV_Grid_Width*0.1)
            self.DV_Grid.addWidget(DV_dsu, 2*i+1, 5, 2, 1)
            setattr(self.DV_Grid, "dsu" + str(i), DV_dsu)

        test = getattr(self.DV_Grid, self.p.x[0]["name"])
        test.setText("Z_2222")

        # Setting dimensions for the Design Variable table
        for i in range(0, len(self.p.x)):
            self.DV_Grid.setRowMinimumHeight(2*i+1, 25)
            self.DV_Grid.setRowMinimumHeight(2*i+2, 25)




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
