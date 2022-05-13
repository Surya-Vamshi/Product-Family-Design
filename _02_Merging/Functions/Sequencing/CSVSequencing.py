def CSVSequencing(CSV, Suffix, Folder_Main, Folder_Temporary, Folder_Merging):
    """
    Description : Reorganize a CSV file

    Input variables :
    CSV : csv file name with '.csv'
    Suffix : name of the new file is the name of the old file + suffix or if suffix empty replace file
    Folder_Main : Main Folder containing all the code files
    Folder_Temporary : Folder with all the Temporary files
    Folder_Merging : Folder with all the merging algorithms

    Output variables :
    NewFile : reordered csv file name with '.csv'
    """
    # Importing Modules
    from Functions.Sequencing.CSV2MatrixAndTables import CSV2MatrixAndTables
    from Functions.Sequencing.DSMSequencing import DSMSequencing
    from Functions.Sequencing.WritingList2CSV import WritingList2CSV
    from Functions.Sequencing.NameOfNewCSVFile import NameOfNewCSVFile

    # Code
    [MatVar, MatType, MatColor, Mat] = CSV2MatrixAndTables(CSV, Folder_Main + Folder_Temporary)
    [MatVar, MatType, MatColor, Mat] = DSMSequencing(MatVar, MatType, MatColor, Mat)
    NewFile = NameOfNewCSVFile(CSV, Suffix)
    NewFile = Folder_Main + Folder_Temporary + "\\" + NewFile
    WritingList2CSV(MatVar, MatType, MatColor, Mat, NewFile)
    return NewFile
