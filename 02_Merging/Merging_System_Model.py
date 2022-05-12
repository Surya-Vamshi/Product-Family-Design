"""
Create GUI to interact with User
The function should provide a user interface with two callbacks:
1. List of Modular Models which should be merged (M0001,...)
2. Name of the System model (which the algorithm will generate)

Number of sample point should be 300 by default.
"""

# Importing Modules
from PySide6.QtWidgets import QApplication, QPushButton, QTableWidgetItem, \
    QDialog, QLabel, QLineEdit, QTableWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
import sys
import os
import string
from pathlib import Path

from Functions.System_XRay_From_Models import System_XRay_From_Models

# User can change these directories' location if needed.
Folder_Design_Problems = str(Path("/03_Design_Problems"))
Folder_Systems = str(Path("/02_Merging/Systems"))
Folder_Database = str(Path("/01_Database"))
Folder_Merging = str(Path("/02_Merging"))

SampleSize = 300  # Default

# Do not touch
# Getting available models from database
os.chdir("../")
Folder_Main = str(Path(os.getcwd()))
files = os.listdir(Folder_Main + Folder_Database)
available_Models = []
for name in files:
    if name.startswith("M") and name.endswith(".csv"):
        available_Models.append(name[:-4])
available_Models.sort()

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        # window title, icon and geometry
        self.setGeometry(500, 200, 400, 500)
        self.setFixedSize(400, 500)
        self.setWindowTitle("Merging System Model")
        self.setWindowIcon(QIcon('icon.png'))

        models = available_Models

        nb_row = len(models)
        nb_col = 1

        data = [[] for i in range(nb_row)]
        for i, model in enumerate(models):
            for j in range(nb_col):
                data[i].append(model)

        self.table1 = QTableWidget(self)
        self.table1.horizontalHeader().setStretchLastSection(True)

        self.table1.setRowCount(nb_row)
        self.table1.setColumnCount(nb_col)
        self.table1.setHorizontalHeaderLabels(['List of Modular Models available in Database'])
        for row in range(nb_row):
            for col in range(nb_col):
                item = QTableWidgetItem(str(data[row][col]))
                self.table1.setItem(row, col, item)
        self.table1.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table1.setGeometry(20, 20, 360, 300)

        self.label2 = QLabel(self)
        self.label2.setText("Enter the name of the System model:")
        self.label2.setGeometry(20, 310, 360, 40)
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Simple_Transmission")
        self.name.setGeometry(20, 350, 360, 40)

        self.error1 = QLabel(self)
        self.error2 = QLabel(self)

        btn1 = QPushButton("Run", self)
        btn1.setGeometry(200, 440, 80, 40)
        btn1.clicked.connect(self.run_merge)

        btn2 = QPushButton("Quit", self)
        btn2.setGeometry(300, 440, 80, 40)
        btn2.clicked.connect(QApplication.instance().quit)

    def run_merge(self):
        selected_list = self.table1.selectedItems()
        CODEs = []
        for item in selected_list:
            CODEs.append(item.text()[:5])
        System_Name = self.name.text()
        valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
        System_Name = "".join(x for x in System_Name if x in valid_chars)

        if not CODEs or not System_Name:
            if not CODEs:
                self.error1.setText("Please Select Models")
                self.error1.setGeometry(20, 400, 175, 30)
                self.error1.setStyleSheet("border-radius: 5px; background-color: #D92000")
                self.error1.setAlignment(Qt.AlignCenter)
            else:
                self.error1.setHidden(True)
            if not System_Name:
                self.error2.setText("Please Enter a System Name")
                self.error2.setGeometry(205, 400, 175, 30)
                self.error2.setStyleSheet("border-radius: 5px; background-color: #D92000")
                self.error2.setAlignment(Qt.AlignCenter)
            else:
                self.error2.setHidden(True)
        else:
            self.error1.setHidden(True)
            self.error2.setHidden(True)
            CSVFinal, Pythonx = System_XRay_From_Models(CODEs, System_Name, SampleSize, Folder_Main, Folder_Database,
                                                        Folder_Merging, Folder_Design_Problems, Folder_Systems)
            print("CSV file after Merging is saved as " + CSVFinal)
            print("Python file after Merging is saved as " + Pythonx)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())

