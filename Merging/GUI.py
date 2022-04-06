from PySide6.QtWidgets import QApplication, QPushButton, QTableWidgetItem, \
    QDialog, QLabel, QLineEdit, QTableWidget
import sys
from PySide6.QtGui import QIcon

import os

os.chdir("../")
Folder_Main = os.getcwd()
Folder_Database = r"\Database"
files = os.listdir(Folder_Main + Folder_Database)
available_Models = []
for name in files:
    if name.startswith("M") and name.endswith(".csv"):
        available_Models.append(name)


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
        self.label2.setGeometry(20, 350, 360, 40)
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Simple_Transmission")
        self.name.setGeometry(20, 390, 360, 40)

        btn1 = QPushButton("Run", self)
        btn1.setGeometry(200, 440, 80, 40)
        btn1.clicked.connect(self.run_merge)

        btn2 = QPushButton("Quit", self)
        btn2.setGeometry(300, 440, 80, 40)
        btn2.clicked.connect(QApplication.instance().quit)

    def run_merge(self):
        list = self.table1.selectedItems()
        CODEs = []
        for item in list:
            CODEs.append(item.text())
        print(CODEs)
        system_name = self.name.text()
        system_name = "".join(x for x in system_name if x.isalnum())
        print(system_name)
        print("Calling Merging Function")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
