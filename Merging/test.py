from PySide6.QtWidgets import QApplication, QPushButton, QTableWidgetItem, \
    QDialog, QLabel, QLineEdit, QTableWidget
import sys
from PySide6.QtGui import QIcon

import os




class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        # window title, icon and geometry
        self.setGeometry(500, 200, 400, 500)
        self.setFixedSize(400, 500)
        self.setWindowTitle("Merging System Model")
        self.setWindowIcon(QIcon('icon.png'))





app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
