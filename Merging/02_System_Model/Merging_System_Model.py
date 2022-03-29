"""
Create GUI to interact with User
The function should provide a user interface with two callbacks:
1. List of Modular Models which should be merged (M0001,...)
2. Name of the System model (which the algorithm will generate)

Number of sample point should be 300 by default.
"""
# GUI Interface will be used for these inputs
CODEs = ['M0001','M0002','M0003','M0004']
System_Name = 'Simple_Transmission'
SampleSize = 300 #Default
# IMPORT MODULES
#from PySide6.QtGui import QGuiApplication
#from PySide6.QtQml import QQmlApplicationEngine

import os
path = os.getcwd()
Folder_Main = os.path.dirname(path)

# User can change these directories location if needed.
Folder_Design_Problems = r"\Product-Family-Design\Optimization\Design_Problems"
Folder_Systems = r"\Product-Family-Design\Merging\01_Systems"
Folder_Database = r"\Product-Family-Design\Database"
Folder_Merging_Funtions = r"\Product-Family-Design\Merging\100_Functions"
Folder_Merging_Sequencing = r"\Product-Family-Design\Merging\100_Functions\01_Sequencing"
Folder_Merging_Create_x_file = r"\Product-Family-Design\Merging\100_Functions\02_Create_x_file"

# Do not touch

import sys
sys.path.append(str(Folder_Main+Folder_Merging_Funtions))
from System_XRay_From_Models import System_XRay_From_Models

CSVFinal,Pythonx = System_XRay_From_Models(CODEs,System_Name,SampleSize,Folder_Main,Folder_Design_Problems,Folder_Systems,Folder_Database,Folder_Merging_Funtions,Folder_Merging_Sequencing,Folder_Merging_Create_x_file)

print("CSV file after Merging is saved as "+CSVFinal)
print("Python file after Merging is saved as "+Pythonx)