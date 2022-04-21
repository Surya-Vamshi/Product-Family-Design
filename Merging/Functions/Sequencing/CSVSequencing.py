def CSVSequencing(CSV, Suffix, Folder_Main, Folder_Temporary, Folder_Merging_Funtions,
                  Folder_Merging_Sequencing, Folder_Merging_Create_x_file):
    """
    Description : Reorganize a CSV file

    Input variables :
    CSV : csv file name with '.csv'
    Suffix : name of the new file is the name of the old file + suffix or if suffix empty replace file
    Folder_Database : Position of the csv file
    Folder_Merging_Algorithms : Folder with all the algorithms

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
