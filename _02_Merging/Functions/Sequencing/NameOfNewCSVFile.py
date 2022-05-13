def NameOfNewCSVFile(OldFile, Suffix):
    """
    Description : Naming of the new CSV file by adding a suffix (used for sequencing a simple CSV file

    Input variables :
    OldFile : the csv file
    Suffix : name of the new file by adding a suffix (if empty = replace file)

    Output variables :
    NewFileName : new csv file name with '.csv'
    """
    FileName = OldFile[:-4]

    if Suffix == "":
        NewFileName = FileName + ".csv"
    else:
        NewFileName = FileName + Suffix + ".csv"
    return NewFileName
