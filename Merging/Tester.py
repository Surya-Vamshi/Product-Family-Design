"""
This File is to test the code at development stage.
It will be removed once the Merging Codes are Completed.
"""

# GUI Interface will be used for these inputs
CODEs = ['M0001', 'M0002', 'M0003', 'M0004']
System_Name = 'Simple_Transmission'
SampleSize = 300  # Default

# IMPORT MODULES
from Functions.System_XRay_From_Models import System_XRay_From_Models
import os
os.chdir("../")
Folder_Main = os.getcwd()

# User can change these directories location if needed.
Folder_Design_Problems = r"\Optimization\Design_Problems"
Folder_Systems = r"\Merging\Systems"
Folder_Database = r"\Database"
Folder_Merging_Funtions = r"\Merging\Functions"
Folder_Merging_Sequencing = r"\Merging\Functions\Sequencing"
Folder_Merging_Create_x_file = r"\Merging\Functions\Create_x_file"

# Do not touch


CSVFinal, Pythonx = System_XRay_From_Models(CODEs, System_Name, SampleSize, Folder_Main, Folder_Design_Problems,
                                            Folder_Systems, Folder_Database, Folder_Merging_Funtions,
                                            Folder_Merging_Sequencing, Folder_Merging_Create_x_file)

print("CSV file after Merging is saved as " + CSVFinal)
print("Python file after Merging is saved as " + Pythonx)
