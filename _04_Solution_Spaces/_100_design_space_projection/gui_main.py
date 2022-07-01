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
    QStatusBar, QTabWidget, QWidget, QGridLayout, QSlider, QScrollArea, QLayout, QToolBox, QCheckBox, QColorDialog, \
    QRadioButton, QListWidget, QListWidgetItem, QInputDialog


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
        self.p.append(self.problem())
        self.ProdNames.append("Product 2")
        self.p.append(self.problem())
        self.ProdNames.append("Product 3")

        self.p[1].x[0]["dsl"] = 500
        self.p[1].x[1]["u"] = 2000
        print("Product 1: ", self.p[0].x[0]["dsl"])
        print("Product 2: ", self.p[1].x[0]["dsl"])
        print("Product 3: ", self.p[2].x[0]["dsl"])
        ## End

        # window title, icon and geometry
        screensize = QGuiApplication.primaryScreen().availableSize()
        width = screensize.width()
        height = screensize.height() - 40
        font = QFont()
        font.setPointSize(10)
        self.setGeometry(500, 200, 0.33 * width, height)
        self.setFixedSize(0.33 * width, height)
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

        # Error Message
        self.Error = QLabel(self)
        self.Error.setText("Error")
        self.Error.setGeometry(10, 10, width*0.33 - 300, 60)
        self.Error.setStyleSheet("font-size: 18px; border-radius: 5px; background-color: #D92000")
        self.Error.setAlignment(Qt.AlignCenter)
        self.Error.setHidden(True)

        # Refresh Tab Window call
        self.init_product_data()

        print("GUI is called " + str(problem))
        print("D = ", self.p[self.currentProdNum].d)
        print("M = ", self.p[self.currentProdNum].m)
        print("NP = ", self.p[self.currentProdNum].np)

        self.show()

    def init_product_data(self):
        screensize = QGuiApplication.primaryScreen().availableSize()
        height = screensize.height()
        width = screensize.width()
        # Sample Size input update
        self.sample_size_input.setText(str(self.p[self.currentProdNum].sampleSize))

        # Main Tab Windows
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(QRect(10, 100, 0.33 * width - 20, (height-100)*0.6))
        self.DV = QWidget()
        self.DV.setEnabled(True)
        self.tabWidget.addTab(self.DV, "Design Variables and Parameters")
        self.QOI = QWidget()
        self.tabWidget.addTab(self.QOI, "Quantities of Interest")
        font = QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)

        # Design Variables and Parameters Tab
        self.DV_toolboxmain = QToolBox(self.DV)
        DV_Grid_Width = 0.33 * width - 40
        self.DV_toolboxmain.setGeometry(QRect(10, 10, DV_Grid_Width, (height-100)*0.6 - 50))
        self.DV_toolbox = QWidget()
        self.Para_toolbox = QWidget()

        self.DV_Grid = QGridLayout(self.DV_toolbox)
        self.DV_Grid.setSpacing(10)
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

        # Setting dimensions for the Design Variable table
        for i in range(0, x_size):
            self.DV_Grid.setRowMinimumHeight(2 * i + 1, 25)
            self.DV_Grid.setRowMinimumHeight(2 * i + 2, 25)

        # Creating Parameters Tab2
        self.Para_Grid = QGridLayout(self.Para_toolbox)
        self.Para_Grid.setSpacing(10)
        self.Para_Grid.setSizeConstraint(QLayout.SetFixedSize)
        font.setBold(True)

        # Headings of the Design variable inputs
        Para_Header1 = QLabel("Name", self.DV)
        Para_Header1.setFixedWidth(DV_Grid_Width * 0.35)
        Para_Header1.setFont(font)
        self.Para_Grid.addWidget(Para_Header1, 0, 0, 1, 1)
        Para_Header2 = QLabel("Unit", self.DV)
        Para_Header2.setFixedWidth(DV_Grid_Width * 0.15)
        Para_Header2.setFont(font)
        self.Para_Grid.addWidget(Para_Header2, 0, 1, 1, 1)
        Para_Header3 = QLabel("Value", self.DV)
        Para_Header3.setMaximumWidth(DV_Grid_Width * 0.5)
        Para_Header3.setFont(font)
        self.Para_Grid.addWidget(Para_Header3, 0, 2, 1, 1)

        # Generating a table with Parameters as per X-ray file
        para_size = len(self.p[self.currentProdNum].p)

        for i in range(0, para_size):
            Para_name = QLabel(self.p[self.currentProdNum].p[i]["name"])
            Para_name.setFixedWidth(DV_Grid_Width * 0.35)
            self.Para_Grid.addWidget(Para_name, i + 1, 0, 1, 1)
            setattr(self.Para_Grid, self.p[self.currentProdNum].p[i]["name"], Para_name)

        for i in range(0, para_size):
            Para_unit = QLabel(self.p[self.currentProdNum].p[i]["unit"])
            Para_unit.setFixedWidth(DV_Grid_Width * 0.15)
            self.Para_Grid.addWidget(Para_unit, i + 1, 1, 1, 1)
            setattr(self.Para_Grid, "unit" + str(i), Para_unit)

        for i in range(0, para_size):
            Para_value = QLineEdit(str(self.p[self.currentProdNum].p[i]["value"]))
            Para_value.setMaximumWidth(DV_Grid_Width * 0.5)
            self.Para_Grid.addWidget(Para_value, i + 1, 2, 1, 1)
            setattr(self.Para_Grid, "value" + str(i), Para_value)

        # Setting dimensions for the Parameters table
        for i in range(0, para_size):
            self.Para_Grid.setRowMinimumHeight(i + 1, 25)

        # Adding both toolboxs to toolboxmain
        self.DV_toolboxmain.addItem(self.DV_toolbox, "Select the Design Variable values as per requirement:")
        self.DV_toolboxmain.addItem(self.Para_toolbox, "Select the Parameters values as per requirement:")

        # Quantities of Interest Tab
        self.QOI_toolboxmain = QToolBox(self.QOI)
        QOI_Grid_Width = 0.33 * width - 40
        self.QOI_toolboxmain.setGeometry(QRect(10, 10, QOI_Grid_Width, (height-100)*0.6 - 50))
        self.QOI_toolbox1 = QWidget()

        # Creating Quantities of Interest Tab1
        self.QOI_Grid1 = QGridLayout(self.QOI_toolbox1)
        self.QOI_Grid1.setSpacing(10)
        self.QOI_Grid1.setSizeConstraint(QLayout.SetFixedSize)
        font.setBold(True)

        # Headings of the Design variable inputs
        QOI_Header1 = QLabel("Visible", self.QOI)
        QOI_Header1.setFont(font)
        self.QOI_Grid1.addWidget(QOI_Header1, 0, 0, 1, 1)
        QOI_Header2 = QLabel("Active", self.QOI)
        QOI_Header2.setFont(font)
        self.QOI_Grid1.addWidget(QOI_Header2, 0, 1, 1, 1)
        QOI_Header3 = QLabel("Name", self.QOI)
        QOI_Header3.setFont(font)
        self.QOI_Grid1.addWidget(QOI_Header3, 0, 2, 1, 1)
        QOI_Header4 = QLabel("Unit", self.QOI)
        QOI_Header4.setFont(font)
        self.QOI_Grid1.addWidget(QOI_Header4, 0, 3, 1, 1)
        QOI_Header5 = QLabel("Lower Limit", self.QOI)
        QOI_Header5.setAlignment(Qt.AlignCenter)
        QOI_Header5.setFont(font)
        self.QOI_Grid1.addWidget(QOI_Header5, 0, 4, 1, 1)
        QOI_Header6 = QLabel("Upper Limit", self.QOI)
        QOI_Header6.setAlignment(Qt.AlignCenter)
        QOI_Header6.setFont(font)
        self.QOI_Grid1.addWidget(QOI_Header6, 0, 5, 1, 1)
        QOI_Header7 = QLabel("Select Color", self.QOI)
        QOI_Header7.setAlignment(Qt.AlignCenter)
        QOI_Header7.setFont(font)
        self.QOI_Grid1.addWidget(QOI_Header7, 0, 6, 1, 1)

        # Generating a table with Quantities of Interest as per X-ray file
        y_size = len(self.p[self.currentProdNum].y)

        for i in range(0, y_size):
            QOI_visible = QCheckBox()
            QOI_visible.setChecked(True)
            self.QOI_Grid1.addWidget(QOI_visible, i + 1, 0, 1, 1)
            setattr(self.QOI_Grid1, "visible" + str(i), QOI_visible)

        for i in range(0, y_size):
            QOI_active = QCheckBox()
            if self.p[self.currentProdNum].y[i]["active"] == 1:
                QOI_active.setChecked(True)
            self.QOI_Grid1.addWidget(QOI_active, i + 1, 1, 1, 1)
            setattr(self.QOI_Grid1, "active" + str(i), QOI_active)

        for i in range(0, y_size):
            QOI_name = QLabel(self.p[self.currentProdNum].y[i]["name"])
            QOI_name.setFixedWidth(QOI_Grid_Width * 0.175)
            self.QOI_Grid1.addWidget(QOI_name, i + 1, 2, 1, 1)
            setattr(self.QOI_Grid1, self.p[self.currentProdNum].y[i]["name"], QOI_name)

        for i in range(0, y_size):
            QOI_unit = QLabel(self.p[self.currentProdNum].y[i]["unit"])
            QOI_unit.setFixedWidth(QOI_Grid_Width * 0.075)
            self.QOI_Grid1.addWidget(QOI_unit, i + 1, 3, 1, 1)
            setattr(self.QOI_Grid1, "unit" + str(i), QOI_unit)

        for i in range(0, y_size):
            QOI_l = QLineEdit(str(self.p[self.currentProdNum].y[i]["l"]))
            QOI_l.setMaximumWidth(QOI_Grid_Width * 0.15)
            self.QOI_Grid1.addWidget(QOI_l, i + 1, 4, 1, 1)
            setattr(self.QOI_Grid1, "l" + str(i), QOI_l)

        for i in range(0, y_size):
            QOI_u = QLineEdit(str(self.p[self.currentProdNum].y[i]["u"]))
            QOI_u.setMaximumWidth(QOI_Grid_Width * 0.15)
            self.QOI_Grid1.addWidget(QOI_u, i + 1, 5, 1, 1)
            setattr(self.QOI_Grid1, "u" + str(i), QOI_u)

        for i in range(0, y_size):
            [r, b, g] = self.p[self.currentProdNum].y[i]["color"]
            text = "#%02x%02x%02x" % (r, g, b)
            QOI_colorbtn = QPushButton(text)
            QOI_colorbtn.setStyleSheet("background-color: #%02x%02x%02x" % (r, g, b))
            QOI_colorbtn.clicked.connect(self.selectColor)
            self.QOI_Grid1.addWidget(QOI_colorbtn, i + 1, 6, 1, 1)
            setattr(self.QOI_Grid1, "color" + str(i), QOI_colorbtn)

        # Setting dimensions for the Quantities of Interest table
        for i in range(0, y_size):
            self.QOI_Grid1.setRowMinimumHeight(i + 1, 25)

        # Adding toolbox to the QOI main toolbox
        self.QOI_toolboxmain.addItem(self.QOI_toolbox1,
                                       "Select the Quantities of Interest values as per requirement:")

        # Adding Products Tab to the GUI
        self.tabWidget2 = QTabWidget(self)
        self.tabWidget2.setGeometry(QRect(10, (height-100)*0.6 + 120, 0.33 * width - 20, (height-100)*0.3))
        self.prods = QWidget()
        self.prods.setEnabled(True)
        self.tabWidget2.addTab(self.prods, "Product Menu")
        font = QFont()
        font.setPointSize(10)
        self.tabWidget2.setFont(font)

        # Product Tab
        self.prods_toolboxmain = QToolBox(self.prods)
        prods_Grid_Width = 0.33 * width - 40
        self.prods_toolboxmain.setGeometry(QRect(10, 10, prods_Grid_Width, (height-100)*0.3 - 100))
        self.prods_toolbox = QWidget()

        self.prods_Grid = QGridLayout(self.prods_toolbox)
        self.prods_Grid.setSpacing(10)
        self.prods_Grid.setSizeConstraint(QLayout.SetFixedSize)
        font.setBold(True)

        # Product Menu List
        num_pro = len(self.p)

        for i in range(0, num_pro):
            Product_element = QRadioButton(self.ProdNames[i], self)
            if i == 0:
                Product_element.setChecked(True)
            Product_element.toggled.connect(self.change_prod)
            self.prods_Grid.addWidget(Product_element, i + 1, 0, 1, 1)
            setattr(self.prods_Grid, str(self.ProdNames[i]), Product_element)

        # Adding DV_toolbox to toolboxmain
        self.prods_toolboxmain.addItem(self.prods_toolbox, "Select or ADD or Delete Products as per requirement:")

        # Product Family Call button
        self.product_family_button = QPushButton("Product Family", self.prods)
        self.product_family_button.setGeometry(20, (height-100)*0.3 - 80, prods_Grid_Width * 0.3, 40)
        self.product_family_button.clicked.connect(self.run_product_family)

        # Pushbuttons to manipulate products
        self.add_btn = QPushButton("Add", self.prods)
        self.add_btn.setGeometry(prods_Grid_Width * 0.4 - 20, (height-100)*0.3 - 80, prods_Grid_Width * 0.2, 40)
        self.add_btn.clicked.connect(self.add_product)
        self.rename_btn = QPushButton("Rename", self.prods)
        self.rename_btn.setGeometry(prods_Grid_Width * 0.6 - 10, (height-100)*0.3 - 80, prods_Grid_Width * 0.2, 40)
        self.rename_btn.clicked.connect(self.rename_product)
        self.delete_btn = QPushButton("Delete", self.prods)
        self.delete_btn.setGeometry(prods_Grid_Width * 0.8, (height-100)*0.3 - 80, prods_Grid_Width * 0.2, 40)
        self.delete_btn.clicked.connect(self.delete_product)

        self.show()

    def update_values(self):
        self.p[self.currentProdNum].sampleSize = self.sample_size_input.text()
        # Updating the Design Variable values from the GUI to the current product details
        for i in range(0, len(self.p[self.currentProdNum].x)):
            DV_dsl = getattr(self.DV_Grid, "dsl" + str(i))
            self.p[self.currentProdNum].x[i]["dsl"] = DV_dsl.text()

            DV_l = getattr(self.DV_Grid, "l" + str(i))
            self.p[self.currentProdNum].x[i]["l"] = DV_l.text()

            # Need to Add Ranger values later

            DV_u = getattr(self.DV_Grid, "u" + str(i))
            self.p[self.currentProdNum].x[i]["u"] = DV_u.text()

            DV_dsu = getattr(self.DV_Grid, "dsu" + str(i))
            self.p[self.currentProdNum].x[i]["dsu"] = DV_dsu.text()

        # Updating the Quantities of Interest Values from the GUI to the current product details
        for i in range(0, len(self.p[self.currentProdNum].y)):
            QOI_visible = getattr(self.QOI_Grid1, "visible" + str(i))
            self.p[self.currentProdNum].y[i]["visible"] = QOI_visible.checkState()

            QOI_active = getattr(self.QOI_Grid1, "active" + str(i))
            self.p[self.currentProdNum].y[i]["active"] = QOI_active.checkState()

            QOI_l = getattr(self.QOI_Grid1, "l" + str(i))
            self.p[self.currentProdNum].y[i]["l"] = QOI_l.text()

            QOI_u = getattr(self.QOI_Grid1, "u" + str(i))
            self.p[self.currentProdNum].y[i]["u"] = QOI_u.text()

            QOI_colorbtn = getattr(self.QOI_Grid1, "color" + str(i))
            h = QOI_colorbtn.text().lstrip("#")
            (r, g, b) = tuple(int(h[k:k + 2], 16) for k in (0, 2, 4))
            self.p[self.currentProdNum].y[i]["color"] = [r, g, b]

        # Updating the Parameters Values from the GUI to the current product details
        for i in range(0, len(self.p[self.currentProdNum].p)):
            QOI_value = getattr(self.Para_Grid, "value" + str(i))
            QOI_value.setText(str(self.p[self.currentProdNum].p[i]["value"]))

    def change_prod(self):
        for i in range(0, len(self.p)):
            Product_element = getattr(self.prods_Grid, str(self.ProdNames[i]))
            if Product_element.isChecked():
                self.currentProdNum = i

        print("Current Product = " + self.ProdNames[self.currentProdNum])

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

        # Changing Quantities of Interest Values
        for i in range(0, len(self.p[self.currentProdNum].y)):
            QOI_visible = getattr(self.QOI_Grid1, "visible" + str(i))
            QOI_visible.setChecked(True)

            QOI_active = getattr(self.QOI_Grid1, "active" + str(i))
            if self.p[self.currentProdNum].y[i]["active"] == 1:
                QOI_active.setChecked(True)
            else:
                QOI_active.setChecked(False)

            QOI_l = getattr(self.QOI_Grid1, "l" + str(i))
            QOI_l.setText(str(self.p[self.currentProdNum].y[i]["l"]))

            QOI_u = getattr(self.QOI_Grid1, "u" + str(i))
            QOI_u.setText(str(self.p[self.currentProdNum].y[i]["u"]))

            [r, b, g] = self.p[self.currentProdNum].y[i]["color"]
            QOI_colorbtn = getattr(self.QOI_Grid1, "color" + str(i))
            QOI_colorbtn.setStyleSheet("background-color: #%02x%02x%02x" % (r, g, b))

        # Changing Parameters Values
        for i in range(0, len(self.p[self.currentProdNum].p)):
            QOI_value = getattr(self.Para_Grid, "value" + str(i))
            QOI_value.setText(str(self.p[self.currentProdNum].p[i]["value"]))

    def add_product(self):
        name, ok = QInputDialog.getText(self, 'Add a new Product', 'Enter the name of the new Product:')
        if ok:
            if name in self.ProdNames:
                self.Error.setText("Product already exists")
                self.Error.setHidden(False)
            else:
                self.Error.setHidden(True)
                self.ProdNames.append(name)
                self.p.append(self.problem())
                Product_element = QRadioButton(self.ProdNames[len(self.p) - 1], self)
                Product_element.toggled.connect(self.change_prod)
                self.prods_Grid.addWidget(Product_element, self.prods_Grid.rowCount() + 1, 0, 1, 1)
                setattr(self.prods_Grid, str(self.ProdNames[len(self.p) - 1]), Product_element)

    def rename_product(self):
        item, ok = QInputDialog.getItem(self, "Rename a Product", "Please select a product to rename:", self.ProdNames,
                                        0, False)
        if ok:
            name, ok = QInputDialog.getText(self, 'Rename a Product', 'Enter the new name of the selected Product:')
            if ok:
                if name in self.ProdNames:
                    self.Error.setText("Product already exists")
                    self.Error.setHidden(False)
                else:
                    self.Error.setHidden(True)
                    rename_index = self.ProdNames.index(item)
                    setattr(self.prods_Grid, str(name), getattr(self.prods_Grid, str(self.ProdNames[rename_index])))
                    delattr(self.prods_Grid, str(self.ProdNames[rename_index]))
                    Product_element = getattr(self.prods_Grid, str(name))
                    Product_element.setText(str(name))
                    self.ProdNames[rename_index] = name

    def delete_product(self):
        if not self.ProdNames:
            self.Error.setText("No Products are left to delete")
            self.Error.setHidden(False)
        else:
            self.Error.setHidden(True)
            item, ok = QInputDialog.getItem(self, "Delete a Product", "Please select a product to Delete:",
                                            self.ProdNames, 0, False)
            if ok:
                delete_index = self.ProdNames.index(item)
                Product_element = getattr(self.prods_Grid, str(self.ProdNames[delete_index]))
                Product_element.setHidden(True)
                self.prods_Grid.removeWidget(Product_element)
                self.ProdNames.pop(delete_index)
                self.p.pop(delete_index)
                Product_element = getattr(self.prods_Grid, str(self.ProdNames[self.currentProdNum]))
                Product_element.setChecked(True)

    def run_gui_main(self):
        print("Need to call SolutionSpace")

    def run_product_family(self):
        item, ok = QInputDialog.getItem(self, "Select Products", "Please select products to create a family:",
                                        self.ProdNames, 0, True)
        print("Need to call Product Family")

    def selectColor(self):
        """
        Show color-picker dialog to select color.
        """
        dlg = QColorDialog(self)
        dlg.exec()

        # if self._color:
        #     dlg.setCurrentColor(QColor(self._color))
        if dlg.exec():
            for i in range(0, len(self.p[self.currentProdNum].y)):
                QOI_color = getattr(self.QOI_Grid1, "color" + str(i))
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

app = QApplication(sys.argv)
w2 = gui_main("S0002_x_Simple_Transmission")
sys.exit(app.exec())