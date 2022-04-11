def importTester(CODEs, System_Name, SampleSize, Folder_Main, Folder_Design_Problems,
                                            Folder_Systems, Folder_Database, Folder_Merging_Funtions,
                                            Folder_Merging_Sequencing, Folder_Merging_Create_x_file):
    from Functions.System_XRay_From_Models import System_XRay_From_Models

    CSVFinal, Pythonx = System_XRay_From_Models(CODEs, System_Name, SampleSize, Folder_Main, Folder_Design_Problems,
                                                Folder_Systems, Folder_Database, Folder_Merging_Funtions,
                                                Folder_Merging_Sequencing, Folder_Merging_Create_x_file)

    print("CSV file after Merging is saved as " + CSVFinal)
    print("Python file after Merging is saved as " + Pythonx)
    return None
