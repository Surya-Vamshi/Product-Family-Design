def NameOfNewFileMerge(File1, File2, UserNewFileName, Type):
    """
    Descirption : Name of the file after merging 2 files. The user will probably always give the name of the new file.
    If not the case, then the new file will just use the name of the 2 used files.
    Any type of file is accepted : CSV, Matlab, PPX, etc

    Input variables :
    File1, File2 : name of the 2 used files with the suffix '.csv', '.m', etc
    UserNewFileName : name of the file if user give one without the suffix '.csv', '.m', etc. User can let it empty : ''
    Type : type of file '.csv', '.m', etc

    Output variables :
    NewFilepath : path of the new file
    NewFileName : name of the file with the suffix '.csv', '.m', etc
    """
    N = len(Type)
    FileName1 = File1[:-N]
    FileName2 = File2[:-N]
    if UserNewFileName == "":
        NewFileName = FileName1 + "+" + FileName2 + Type
    else:
        NewFileName = UserNewFileName + Type
    return NewFileName
