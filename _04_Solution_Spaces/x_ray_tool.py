"""
Create GUI to interact with User
The function should provide a user interface with two callbacks:
1. List of X files which are already merged (S0001,...)

"""
# Importing Modules
import os
import sys
import shutil
import string
import ctypes
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtWidgets import QApplication, QPushButton, QTableWidgetItem, \
    QDialog, QLabel, QLineEdit, QTableWidget

from _100_design_space_projection.gui_main import *

# User can change these directories' location if needed.
Folder_Design_Problems = str(Path("../_03_Design_Problems"))

# Do not touch
# Getting available models from database
files = os.listdir(Folder_Design_Problems)
entries = []
for name in files:
    if name.startswith("S") and name.endswith(".py"):
        entries.append(name[:-3])
entries.sort()


class DesignProblems(QDialog):
    def __init__(self):
        super().__init__()

        # window title, icon and geometry
        self.setGeometry(500, 200, 400, 400)
        centerPoint = QGuiApplication.primaryScreen().availableGeometry().center()
        qtRectangle = self.frameGeometry()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setFixedSize(400, 400)
        self.setWindowTitle("Choose Design Problem")
        self.setWindowIcon(QIcon(str(Path('../icon.png'))))

        models = entries

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
        self.table1.setHorizontalHeaderLabels(['Select a Design Problem'])
        for row in range(nb_row):
            for col in range(nb_col):
                item = QTableWidgetItem(str(data[row][col]))
                self.table1.setItem(row, col, item)
        self.table1.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table1.setGeometry(20, 20, 360, 250)

        self.error1 = QLabel(self)
        self.error2 = QLabel(self)

        btn1 = QPushButton("Run", self)
        btn1.setGeometry(200, 340, 80, 40)
        btn1.clicked.connect(self.call_user_interface)

        btn2 = QPushButton("Quit", self)
        btn2.setGeometry(300, 340, 80, 40)
        btn2.clicked.connect(QApplication.instance().quit)

    def call_user_interface(self):
        selected_list = self.table1.selectedItems()
        Problem = []
        for item in selected_list:
            Problem.append(item.text())
        num = len(Problem)

        if not Problem:
            if not Problem:
                self.error1.setText("Please a Select Model")
                self.error1.setGeometry(20, 280, 360, 40)
                self.error1.setStyleSheet("border-radius: 5px; background-color: #D92000")
                self.error1.setAlignment(Qt.AlignCenter)
                self.error1.setHidden(False)
            else:
                self.error1.setHidden(True)
        elif num != 1:
            self.error1.setText("Please Select only One Model")
            self.error1.setGeometry(20, 280, 360, 40)
            self.error1.setStyleSheet("border-radius: 5px; background-color: #D92000")
            self.error1.setAlignment(Qt.AlignCenter)
            self.error1.setHidden(False)
        else:
            self.error1.setHidden(True)

            # os.mkdir(str(Path("_100_design_space_projection/temp")))
            # shutil.copyfile(str(Path(".." + Folder_Design_Problems + "/" + Problem[0] + ".py")),
            #                 str(Path("_100_design_space_projection/temp" + "/" + Problem[0] + ".py")))
            self.w2 = gui_main(Problem[0])
            # shutil.rmtree("_100_design_space_projection/temp")

            print("Done")


# Setting up same icon to show on the task bar
if sys.platform == "win32":  # Need to check this
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app = QApplication(sys.argv)
w1 = DesignProblems()
w1.show()
sys.exit(app.exec())
