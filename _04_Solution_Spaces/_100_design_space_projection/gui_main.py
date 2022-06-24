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
from PySide6.QtGui import QGuiApplication, QIcon, QFont, QIntValidator, QDoubleValidator, QColor
from PySide6.QtWidgets import QApplication, QPushButton, QTableWidgetItem, \
    QDialog, QLabel, QLineEdit, QTableWidget, QApplication, QMainWindow, QMenuBar, QSizePolicy, \
    QStatusBar, QTabWidget, QWidget, QGridLayout, QSlider, QScrollArea, QLayout, QToolBox, QCheckBox, QColorDialog,\
    QRadioButton, QListWidget, QListWidgetItem


# Do not touch
class gui_main(QDialog):
    def __init__(self, problem):
        super().__init__()

        # Importing problem x-ray file
        module = importlib.import_module("_03_Design_Problems." + problem)
        self.problem = getattr(module, problem)
        self.p = []
        self.p.append(self.problem())
        self.currentProdNum = 0
        self.ProdNames = ["Product 1"]

        ## Debugging Start
        new_module = importlib.import_module("_100_design_space_projection.temp." + problem)
        self.problem_class = getattr(new_module, problem)
        self.p.append(self.problem().copy())
        self.ProdNames.append("Product 2")
        self.p.append(self.problem_class())
        self.ProdNames.append("Product 3")
        p2 = self.problem_class()

        self.p[1].x[0]["dsl"] = 500
        self.p[1].x[1]["u"] = 2000
        print("Product 1: ", self.p[0].x[0]["dsl"])
        print("Product 2: ", self.p[1].x[0]["dsl"])
        print("Product 3: ", self.p[2].x[0]["dsl"])
        print("Product P2: ", p2.x[0]["dsl"])
        ## End

        # window title, icon and geometry
        screensize = QGuiApplication.primaryScreen().availableSize()
        width = screensize.width()
        height = screensize.height() - 40
        font = QFont()
        font.setPointSize(10)
        self.setGeometry(500, 200, 0.33 * width, height)
        # self.setFixedSize(0.33*width, height)
        self.move(QPoint(0.67 * width, 0))
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
        self.label_sample_size.setFont(font)

        self.sample_size_input = QLineEdit(str(self.p[self.currentProdNum].sampleSize), self)
        self.onlyInt = QIntValidator()
        self.onlyDouble = QDoubleValidator()
        self.sample_size_input.setValidator(self.onlyInt)
        self.sample_size_input.setGeometry(QRect(500, 20, 120, 30))

        # Refresh Tab Window call
        self.init_product_data()

        print("GUI is called " + str(problem))
        print("D = ", self.p[self.currentProdNum].d)
        print("M = ", self.p[self.currentProdNum].m)
        print("NP = ", self.p[self.currentProdNum].np)

        self.show()

    def init_product_data(self):
        screensize = QGuiApplication.primaryScreen().availableSize()
        width = screensize.width()
        # Sample Size input update
        self.sample_size_input.setText(str(self.p[self.currentProdNum].sampleSize))

        # Main Tab Windows
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(QRect(10, 100, 0.33 * width - 20, 400))
        self.DV = QWidget()
        self.DV.setEnabled(True)
        self.tabWidget.addTab(self.DV, "Design Variables")
        self.QOI_P = QWidget()
        self.tabWidget.addTab(self.QOI_P, "Quantities of Interest and Parameters")
        font = QFont()
        font.setPointSize(10)
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
        DV_Header4.setFixedWidth(DV_Grid_Width * 0.4)
        self.DV_Grid.addWidget(DV_Header4, 0, 3, 1, 2)
        DV_Header5 = QLabel("DS Upper\nLimit", self.DV)
        DV_Header5.setAlignment(Qt.AlignCenter)
        DV_Header5.setFont(font)
        self.DV_Grid.addWidget(DV_Header5, 0, 5, 1, 1)

        # Generating a table with design variables as per X-ray file
        x_size = len(self.p[self.currentProdNum].x)
        for i in range(0, x_size):
            DV_name = QLabel(self.p[self.currentProdNum].x[i]["name"])
            DV_name.setFixedWidth(DV_Grid_Width * 0.175)
            self.DV_Grid.addWidget(DV_name, 2 * i + 1, 0, 2, 1)
            setattr(self.DV_Grid, "name" + str(i), DV_name)

        for i in range(0, x_size):
            DV_unit = QLabel(self.p[self.currentProdNum].x[i]["unit"])
            DV_unit.setFixedWidth(DV_Grid_Width * 0.075)
            self.DV_Grid.addWidget(DV_unit, 2 * i + 1, 1, 2, 1)
            setattr(self.DV_Grid, "unit" + str(i), DV_unit)

        for i in range(0, x_size):
            DV_dsl = QLineEdit(str(self.p[self.currentProdNum].x[i]["dsl"]))
            DV_dsl.setMaximumWidth(DV_Grid_Width * 0.1)
            self.DV_Grid.addWidget(DV_dsl, 2 * i + 1, 2, 2, 1)
            setattr(self.DV_Grid, "dsl" + str(i), DV_dsl)

        for i in range(0, x_size):
            DV_l = QLineEdit(str(self.p[self.currentProdNum].x[i]["l"]))
            DV_l.setMaximumWidth(DV_Grid_Width * 0.15)
            self.DV_Grid.addWidget(DV_l, 2 * i + 1, 3, 1, 1)
            setattr(self.DV_Grid, "l" + str(i), DV_l)

        for i in range(0, x_size):
            DV_range = QSlider()
            DV_range.setOrientation(Qt.Horizontal)
            # DV_range.
            DV_range.setMaximumWidth(DV_Grid_Width * 0.5)
            self.DV_Grid.addWidget(DV_range, 2 * i + 2, 3, 1, 2)
            setattr(self.DV_Grid, "range" + str(i), DV_range)

        for i in range(0, x_size):
            DV_u = QLineEdit(str(self.p[self.currentProdNum].x[i]["u"]))
            DV_u.setMaximumWidth(DV_Grid_Width * 0.15)
            self.DV_Grid.addWidget(DV_u, 2 * i + 1, 4, 1, 1)
            setattr(self.DV_Grid, "u" + str(i), DV_u)

        for i in range(0, x_size):
            DV_dsu = QLineEdit(str(self.p[self.currentProdNum].x[i]["dsu"]))
            DV_dsu.setMaximumWidth(DV_Grid_Width * 0.1)
            self.DV_Grid.addWidget(DV_dsu, 2 * i + 1, 5, 2, 1)
            setattr(self.DV_Grid, "dsu" + str(i), DV_dsu)

        # test = getattr(self.DV_Grid, self.p[self.currentProdNum].x[0]["name"])
        # test.setText("Z_2222")

        # Setting dimensions for the Design Variable table
        for i in range(0, x_size):
            self.DV_Grid.setRowMinimumHeight(2 * i + 1, 25)
            self.DV_Grid.setRowMinimumHeight(2 * i + 2, 25)

        # Adding DV_toolbox to toolboxmain
        self.DV_toolboxmain.addItem(self.DV_toolbox, "Select the Design Variable values as per requirement:")
        ##  Tab thing to make sure

        # Quantities of Interest and Parameters Tab
        self.QOI_P_toolboxmain = QToolBox(self.QOI_P)
        QOI_P_Grid_Width = 0.33 * width - 40
        self.QOI_P_toolboxmain.setGeometry(QRect(10, 10, QOI_P_Grid_Width, 350))
        self.QOI_P_toolbox1 = QWidget()
        self.QOI_P_toolbox2 = QWidget()

        # Creating Quantities of Interest Tab1
        self.QOI_P_Grid1 = QGridLayout(self.QOI_P_toolbox1)
        self.QOI_P_Grid1.setSpacing(10)
        self.QOI_P_Grid1.setSizeConstraint(QLayout.SetFixedSize)
        font.setBold(True)

        # Headings of the Design variable inputs
        QOI_P_Header1 = QLabel("Visible", self.QOI_P)
        QOI_P_Header1.setFont(font)
        self.QOI_P_Grid1.addWidget(QOI_P_Header1, 0, 0, 1, 1)
        QOI_P_Header2 = QLabel("Active", self.QOI_P)
        QOI_P_Header2.setFont(font)
        self.QOI_P_Grid1.addWidget(QOI_P_Header2, 0, 1, 1, 1)
        QOI_P_Header3 = QLabel("Name", self.QOI_P)
        QOI_P_Header3.setFont(font)
        self.QOI_P_Grid1.addWidget(QOI_P_Header3, 0, 2, 1, 1)
        QOI_P_Header4 = QLabel("Unit", self.QOI_P)
        QOI_P_Header4.setFont(font)
        self.QOI_P_Grid1.addWidget(QOI_P_Header4, 0, 3, 1, 1)
        QOI_P_Header5 = QLabel("Lower Limit", self.QOI_P)
        QOI_P_Header5.setAlignment(Qt.AlignCenter)
        QOI_P_Header5.setFont(font)
        self.QOI_P_Grid1.addWidget(QOI_P_Header5, 0, 4, 1, 1)
        QOI_P_Header6 = QLabel("Upper Limit", self.QOI_P)
        QOI_P_Header6.setAlignment(Qt.AlignCenter)
        QOI_P_Header6.setFont(font)
        self.QOI_P_Grid1.addWidget(QOI_P_Header6, 0, 5, 1, 1)
        QOI_P_Header7 = QLabel("Select Color", self.QOI_P)
        QOI_P_Header7.setAlignment(Qt.AlignCenter)
        QOI_P_Header7.setFont(font)
        self.QOI_P_Grid1.addWidget(QOI_P_Header7, 0, 6, 1, 1)

        # Generating a table with Quantities of Interest as per X-ray file
        y_size = len(self.p[self.currentProdNum].y)

        for i in range(0, y_size):
            QOI_P_visible = QCheckBox()
            QOI_P_visible.setChecked(True)
            self.QOI_P_Grid1.addWidget(QOI_P_visible, i + 1, 0, 1, 1)
            setattr(self.QOI_P_Grid1, "visible" + str(i), QOI_P_visible)

        for i in range(0, y_size):
            QOI_P_active = QCheckBox()
            if self.p[self.currentProdNum].y[i]["active"] == 1:
                QOI_P_active.setChecked(True)
            self.QOI_P_Grid1.addWidget(QOI_P_active, i + 1, 1, 1, 1)
            setattr(self.QOI_P_Grid1, "active" + str(i), QOI_P_active)

        for i in range(0, y_size):
            QOI_P_name = QLabel(self.p[self.currentProdNum].y[i]["name"])
            QOI_P_name.setFixedWidth(QOI_P_Grid_Width * 0.175)
            self.QOI_P_Grid1.addWidget(QOI_P_name, i + 1, 2, 1, 1)
            setattr(self.QOI_P_Grid1, self.p[self.currentProdNum].y[i]["name"], QOI_P_name)

        for i in range(0, y_size):
            QOI_P_unit = QLabel(self.p[self.currentProdNum].y[i]["unit"])
            QOI_P_unit.setFixedWidth(QOI_P_Grid_Width * 0.075)
            self.QOI_P_Grid1.addWidget(QOI_P_unit, i + 1, 3, 1, 1)
            setattr(self.QOI_P_Grid1, "unit" + str(i), QOI_P_unit)

        for i in range(0, y_size):
            QOI_P_l = QLineEdit(str(self.p[self.currentProdNum].y[i]["l"]))
            QOI_P_l.setMaximumWidth(QOI_P_Grid_Width * 0.15)
            self.QOI_P_Grid1.addWidget(QOI_P_l, i + 1, 4, 1, 1)
            setattr(self.QOI_P_Grid1, "l" + str(i), QOI_P_l)

        for i in range(0, y_size):
            QOI_P_u = QLineEdit(str(self.p[self.currentProdNum].y[i]["u"]))
            QOI_P_u.setMaximumWidth(QOI_P_Grid_Width * 0.15)
            self.QOI_P_Grid1.addWidget(QOI_P_u, i + 1, 5, 1, 1)
            setattr(self.QOI_P_Grid1, "u" + str(i), QOI_P_u)

        for i in range(0, y_size):
            [r, b, g] = self.p[self.currentProdNum].y[i]["color"]
            text = "#%02x%02x%02x" % (r, g, b)
            QOI_P_colorbtn = QPushButton(text)
            QOI_P_colorbtn.setStyleSheet("background-color: #%02x%02x%02x" % (r, g, b))
            QOI_P_colorbtn.clicked.connect(self.selectColor)
            self.QOI_P_Grid1.addWidget(QOI_P_colorbtn, i + 1, 6, 1, 1)
            setattr(self.QOI_P_Grid1, "color" + str(i), QOI_P_colorbtn)

        # Setting dimensions for the Quantities of Interest table
        for i in range(0, y_size):
            self.QOI_P_Grid1.setRowMinimumHeight(i + 1, 25)

        # Creating Parameters Tab2
        self.QOI_P_Grid2 = QGridLayout(self.QOI_P_toolbox2)
        self.QOI_P_Grid2.setSpacing(10)
        self.QOI_P_Grid2.setSizeConstraint(QLayout.SetFixedSize)
        font.setBold(True)

        # Headings of the Design variable inputs
        QOI_P_Header1 = QLabel("Name", self.QOI_P)
        QOI_P_Header1.setFixedWidth(QOI_P_Grid_Width * 0.35)
        QOI_P_Header1.setFont(font)
        self.QOI_P_Grid2.addWidget(QOI_P_Header1, 0, 0, 1, 1)
        QOI_P_Header2 = QLabel("Unit", self.QOI_P)
        QOI_P_Header2.setFixedWidth(QOI_P_Grid_Width * 0.15)
        QOI_P_Header2.setFont(font)
        self.QOI_P_Grid2.addWidget(QOI_P_Header2, 0, 1, 1, 1)
        QOI_P_Header3 = QLabel("Value", self.QOI_P)
        QOI_P_Header3.setMaximumWidth(DV_Grid_Width * 0.5)
        QOI_P_Header3.setFont(font)
        self.QOI_P_Grid2.addWidget(QOI_P_Header3, 0, 2, 1, 1)

        # Generating a table with Parameters as per X-ray file
        para_size = len(self.p[self.currentProdNum].p)

        for i in range(0, para_size):
            QOI_P_name = QLabel(self.p[self.currentProdNum].p[i]["name"])
            QOI_P_name.setFixedWidth(QOI_P_Grid_Width * 0.35)
            self.QOI_P_Grid2.addWidget(QOI_P_name, i + 1, 0, 1, 1)
            setattr(self.QOI_P_Grid2, self.p[self.currentProdNum].p[i]["name"], QOI_P_name)

        for i in range(0, para_size):
            QOI_P_unit = QLabel(self.p[self.currentProdNum].p[i]["unit"])
            QOI_P_unit.setFixedWidth(QOI_P_Grid_Width * 0.15)
            self.QOI_P_Grid2.addWidget(QOI_P_unit, i + 1, 1, 1, 1)
            setattr(self.QOI_P_Grid2, "unit" + str(i), QOI_P_unit)

        for i in range(0, para_size):
            QOI_P_value = QLineEdit(str(self.p[self.currentProdNum].p[i]["value"]))
            QOI_P_value.setMaximumWidth(DV_Grid_Width * 0.5)
            self.QOI_P_Grid2.addWidget(QOI_P_value, i + 1, 2, 1, 1)
            setattr(self.QOI_P_Grid2, "value" + str(i), QOI_P_value)

        # Setting dimensions for the Parameters table
        for i in range(0, para_size):
            self.QOI_P_Grid2.setRowMinimumHeight(i + 1, 25)

        # Adding both toolboxs to the QOI_P main toolbox
        self.QOI_P_toolboxmain.addItem(self.QOI_P_toolbox1,
                                       "Select the Quantities of Interest values as per requirement:")
        self.QOI_P_toolboxmain.addItem(self.QOI_P_toolbox2, "Select the Parameters values as per requirement:")

        # Adding Products Tab to the GUI
        self.tabWidget2 = QTabWidget(self)
        self.tabWidget2.setGeometry(QRect(10, 600, 0.33 * width - 20, 400))
        self.prods = QWidget()
        self.prods.setEnabled(True)
        self.tabWidget2.addTab(self.prods, "Product Menu")
        font = QFont()
        font.setPointSize(10)
        self.tabWidget2.setFont(font)

        # Product Tab
        self.prods_toolboxmain = QToolBox(self.prods)
        prods_Grid_Width = 0.33 * width - 40
        self.prods_toolboxmain.setGeometry(QRect(10, 10, prods_Grid_Width, 100))
        self.prods_toolbox = QWidget()

        self.prods_Grid = QGridLayout(self.prods_toolbox)
        self.prods_Grid.setSpacing(10)
        self.prods_Grid.setSizeConstraint(QLayout.SetFixedSize)
        font.setBold(True)
        #
        # # Headings of the Product Menu
        # prods_Header1 = QLabel("Name", self.prods)
        # prods_Header1.setFont(font)
        # self.prods_Grid.addWidget(prods_Header1, 0, 0, 1, 1)
        # prods_Header2 = QLabel("Rename", self.prods)
        # prods_Header2.setFixedWidth(prods_Grid_Width * 0.15)
        # prods_Header2.setFont(font)
        # self.QOI_P_Grid2.addWidget(prods_Header2, 0, 1, 1, 1)
        # prods_Header3 = QLabel("Delete", self.prods)
        # prods_Header3.setMaximumWidth(prods_Grid_Width * 0.5)
        # prods_Header3.setFont(font)
        # self.QOI_P_Grid2.addWidget(prods_Header3, 0, 2, 1, 1)

        # Product Menu List
        num_pro = len(self.p)

        # self.prods_table = QListWidget(self.prods)
        # self.prods_table.horizontalHeader().setStretchLastSection(True)

        # self.prods_table.setRowCount(nb_row)
        # self.prods_table.setColumnCount(nb_col)
        # self.prods_table.setHorizontalHeaderLabels(['Products List'])
        # for row in range(nb_row):
        #     item = QListWidgetItem(str(self.ProdNames[row]))
        #     self.prods_table.setItemWidget(item, QRadioButton("Test"))
        # # self.prods_table.setEditTriggers(QTableWidget.NoEditTriggers)
        # self.prods_table.setGeometry(10, 10, 0.33 * width - 40, 350)

        # Testinggggggggg
        for i in range(0, num_pro):
            Product_element = QRadioButton(self.ProdNames[i], self)
            if i == 0:
                Product_element.setChecked(True)
            Product_element.toggled.connect(self.change_prod)
            self.prods_Grid.addWidget(Product_element, i + 1, 0, 1, 1)
            setattr(self.prods_Grid, str(self.ProdNames[i]), Product_element)

        # Testingggggg Endssssss

        # Adding DV_toolbox to toolboxmain
        self.prods_toolboxmain.addItem(self.prods_toolbox, "Select or ADD or Delete Products as per requirement:")

        self.show()

    def update_values(self):
        self.p[self.currentProdNum].sampleSize = self.sample_size_input.text()
        print(self.p[self.currentProdNum].sampleSize)
        # test = getattr(self.DV_Grid, "u1")
        # print(test.text())
        # test = getattr(self.QOI_P_Grid1, "color0")
        # print(test)
        # print(self.printingtest)
        # print(self.p[self.currentProdNum].y[1]["color"])
        # self.p.append(self.problem())
        # self.ProdNames.append("Product 2")
        # self.currentProdNum = 1

        # self.change_prod()

    def change_prod(self):
        for i in range(0, len(self.p)):
            Product_element = getattr(self.prods_Grid, str(self.ProdNames[i]))
            if Product_element.isChecked():
                self.currentProdNum = i

        # Changing Design Variable values
        for i in range(0, len(self.p[self.currentProdNum].x)):
            DV_dsl = getattr(self.DV_Grid, "dsl" + str(i))
            DV_dsl.setText(str(self.p[self.currentProdNum].x[i]["dsl"]))

            DV_l = getattr(self.DV_Grid, "l" + str(i))
            DV_l.setText(str(self.p[self.currentProdNum].x[i]["l"]))

            # Need to Add Ranger values later

            DV_u = getattr(self.DV_Grid, "u" + str(i))
            DV_u.setText(str(self.p[self.currentProdNum].x[i]["u"]))

            DV_dsu = getattr(self.DV_Grid, "dsu" + str(i))
            DV_dsu.setText(str(self.p[self.currentProdNum].x[i]["dsu"]))

        # print("Current Product = ", self.currentProdNum)
        # print("Current Product DSL =", self.p[self.currentProdNum].x[0]["dsl"])

        # Changing Quantities of Interest Values
        for i in range(0, len(self.p[self.currentProdNum].y)):
            QOI_P_visible = getattr(self.QOI_P_Grid1, "visible" + str(i))
            QOI_P_visible.setChecked(True)

            QOI_P_active = getattr(self.QOI_P_Grid1, "active" + str(i))
            if self.p[self.currentProdNum].y[i]["active"] == 1:
                QOI_P_active.setChecked(True)
            else:
                QOI_P_active.setChecked(False)

            QOI_P_l = getattr(self.QOI_P_Grid1, "l" + str(i))
            QOI_P_l.setText(str(self.p[self.currentProdNum].y[i]["l"]))

            QOI_P_u = getattr(self.QOI_P_Grid1, "u" + str(i))
            QOI_P_u.setText(str(self.p[self.currentProdNum].y[i]["u"]))

            [r, b, g] = self.p[self.currentProdNum].y[i]["color"]
            QOI_P_colorbtn = getattr(self.QOI_P_Grid1, "color" + str(i))
            QOI_P_colorbtn.setStyleSheet("background-color: #%02x%02x%02x" % (r, g, b))

        # Changing Parameters Values
        for i in range(0, len(self.p[self.currentProdNum].p)):
            QOI_P_value = getattr(self.QOI_P_Grid2, "value" + str(i))
            QOI_P_value.setText(str(self.p[self.currentProdNum].p[i]["value"]))

    def run_gui_main(self):
        print("Need to call SolutionSpace")

    def selectColor(self):
        '''
        Show color-picker dialog to select color.
        '''
        dlg = QColorDialog(self)
        dlg.exec()

        # if self._color:
        #     dlg.setCurrentColor(QColor(self._color))
        if dlg.exec():
            for i in range(0, len(self.p[self.currentProdNum].y)):
                QOI_color = getattr(self.QOI_P_Grid1, "color" + str(i))
                [r, g, b] = self.p[self.currentProdNum].y[i]["color"]
                text = "#%02x%02x%02x" % (r, g, b)
                if (QOI_color.text() == text):
                    QOI_color.setText(dlg.currentColor().name())
                    h = dlg.currentColor().name().lstrip("#")
                    (r, g, b) = tuple(int(h[k:k + 2], 16) for k in (0, 2, 4))
                    self.p[self.currentProdNum].y[i]["color"] = [r, g, b]
                    QOI_color.setStyleSheet("background-color: #%02x%02x%02x" % (r, g, b))


# Setting up same icon to show on the task bar
if sys.platform == "win32":  # Need to check this
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# app = QApplication(sys.argv)
# w2 = gui_main("S0002_x_Simple_Transmission")
# sys.exit(app.exec())
