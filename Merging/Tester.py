"""
This File is to test the code at development stage.
It will be removed once the Merging Codes are Completed.
"""

# GUI Interface will be used for these inputs
import pathlib

CODEs = ['M0001', 'M0002', 'M0003', 'M0004']
System_Name = 'Simple_Transmission'
SampleSize = 300  # Default

# IMPORT MODULES
# from Functions.System_XRay_From_Models import System_XRay_From_Models
import os
from pathlib import Path

os.chdir("../")
Folder_Main = str(Path(os.getcwd()))

# User can change these directories' location if needed.
Folder_Design_Problems = str(Path("/Optimization/Design_Problems"))
Folder_Systems = str(Path("/Merging/Systems"))
Folder_Database = str(Path("/Database"))
Folder_Merging_Functions = str(Path("/Merging/Functions"))
Folder_Merging_Sequencing = str(Path("/Merging/Functions/Sequencing"))
Folder_Merging_Create_x_file = str(Path("/Merging/Functions/Create_x_file"))

# Do not touch
from System_Model.importTester import importTester

importTester(CODEs, System_Name, SampleSize, Folder_Main, Folder_Design_Problems,
             Folder_Systems, Folder_Database, Folder_Merging_Functions,
             Folder_Merging_Sequencing, Folder_Merging_Create_x_file)
