def Merging2CSV(CSV1, CSV2, FileName, Folder_Main, Folder_Temporary, Folder_Merging):
    """
    Description : Merging of 2 DSM saved  in 2 CSV file into a new CSV file (it is regrouping the different
    sub-algorithms which make this biggest part of the work)

    Input variables :
    CSV1 : name of the first csv file with '.csv'
    CSV2 : name of the second csv file with '.csv'
    FileName : Name of the new merged csv file without '.csv'
    Folder_Main : Main Folder containing all the code files
    Folder_Temporary : Folder with all the Temporary files
    Folder_Merging : Folder with all the merging algorithms

    Output variables :
    CSV3 : path of the merged CSV file with '.csv'
    """
    # Importing Modules
    from pathlib import Path
    from Functions.Sequencing.CSV2MatrixAndTables import CSV2MatrixAndTables
    from Functions.Sequencing.AdequacyOrdering import AdequacyOrdering
    from Functions.Sequencing.Merging2DSM import Merging2DSM
    from Functions.Sequencing.DSMSequencing import DSMSequencing
    from Functions.Sequencing.WritingList2CSV import WritingList2CSV
    from Functions.Sequencing.NameOfNewFileMerge import NameOfNewFileMerge

    # Code
    [MatVar1, MatType1, MatColor1, Mat1] = CSV2MatrixAndTables(CSV1, Folder_Main + Folder_Temporary)
    [MatVar2, MatType2, MatColor2, Mat2] = CSV2MatrixAndTables(CSV2, Folder_Main + Folder_Temporary)
    [MatVar2, MatType2, MatColor2, Mat2] = AdequacyOrdering(MatVar1, MatVar2, MatType2, MatColor2, Mat2)
    [MatVar, MatType, MatColor, Mat] = Merging2DSM(MatVar1, MatType1, MatColor1, Mat1, MatVar2, MatType2, MatColor2,
                                                   Mat2)
    [MatVar, MatType, MatColor, Mat] = DSMSequencing(MatVar, MatType, MatColor, Mat)
    CSV3 = NameOfNewFileMerge(CSV1, CSV2, FileName, '.csv')
    Fullpath = str(Path(Folder_Main + Folder_Temporary + "/" + CSV3))
    WritingList2CSV(MatVar, MatType, MatColor, Mat, Fullpath)

    return CSV3
