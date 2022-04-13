def Merging2CSV(CSV1, CSV2, MergedModel, Folder_Main, Folder_Temporary, Folder_Merging_Funtions,
                Folder_Merging_Sequencing, Folder_Merging_Create_x_file):
    """
    Description : Merging of 2 DSM saved  in 2 CSV file into a new CSV file (it is regrouping the different
    sub-algorithms which make this biggest part of the work)

    Input variables :
    CSV1 : name of the first csv file with '.csv'
    CSV2 : name of the second csv file with '.csv'
    FileName : Name of the new merged csv file without '.csv'
    Folder_Database : Folder with all modular models
    Folder_Merging_Funtions : Folder with all the merging algorithms
    Folder_Merging_Sequencing : Folder with all the Sequencing algorithms
    Folder_Merging_Create_x_file :Folder with all the Create_x_file algorithms

    Output variables :
    CSV3 : path of the merged CSV file with '.csv'
    """
    # Importing Modules
    from Functions.Sequencing.CSV2MatrixAndTables import CSV2MatrixAndTables
    from Functions.Sequencing.AdequacyOrdering import AdequacyOrdering
    # Code
    [PyVar1, PyType1, PyColor1, Mat1] = CSV2MatrixAndTables(CSV1, Folder_Main + Folder_Temporary)
    [PyVar2, PyType2, PyColor2, Mat2] = CSV2MatrixAndTables(CSV2, Folder_Main + Folder_Temporary)
    [PyVar2, PyType2, PyColor2, Mat2] = AdequacyOrdering(PyVar1, PyVar2, PyType2, PyColor2, Mat2)

    print(PyVar2)
    print(PyType2)
    print(PyColor2)
    print(Mat2)

    Pythonx = "Not yet done"
    return Pythonx
