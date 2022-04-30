def ReplaceTemporaryLineCode(OldTempoFile, ModelFile, ActualTempoFile, Folder_Main, Folder_Temporary,
                             Folder_Merging_Functions, Folder_Merging_Sequencing, Folder_Merging_Create_x_file):
    """
    Description: Inside the actual temporary file the function temporary file
    of previous temporary file need to replace what is inside (functions of
    models)

    Input variables :
    OldTempoFile : CSV file without '.csv' of the previous Temporary file
    ModelFile : CSV file without '.csv' of the added model
    ActualFile : CSV file without '.csv' of the actual temporary file
    Folder_Database : Position of the csv file
    Folder_Merging_Algorithms : Folder with all the algorithms

    Output variables : output is useless in our algorithm. Can be changed
    ActualV : ActualFile with '.csv'
    """
    # Importing Modules
    import re
    from pathlib import Path
    from Functions.Create_x_file.FromType1toType2 import FromType1toType2

    # Code
    OldV = OldTempoFile + ".csv"
    ActualV = ActualTempoFile + ".csv"
    ModelV = ModelFile + ".csv"
    OldV = FromType1toType2(OldV, '.csv', '.py', 'f')
    ActualV = FromType1toType2(ActualV, '.csv', '.py', 'f')
    ModelV = FromType1toType2(ModelV, '.csv', '.py', 'f')
    OldT = open(str(Path(Folder_Main + Folder_Temporary + "/" + OldV)), "r").read()
    ActualT = open(str(Path(Folder_Main + Folder_Temporary + "/" + ActualV)), "r").read()
    NewFile = open(str(Path(Folder_Main + Folder_Temporary + "/" + ActualV)), 'w+')

    FunctionDelimiter1 = re.search("def ", ActualT).start()
    FunctionDelimiter2 = re.search(':', ActualT[FunctionDelimiter1:]).end()
    FirstPart = ActualT[0:FunctionDelimiter1 + FunctionDelimiter2]
    SecondPart = ActualT[FunctionDelimiter1 + FunctionDelimiter2:]

    NewFile.write(FirstPart)

    TemporarysearchList = re.search('(?s:.*)' + OldV[0:-3], OldT).end()

    EndOldT = OldT[TemporarysearchList:]

    TemporaryBeginImports = re.search(":", EndOldT).end()
    TemporaryFinishImports = re.search("# Code", EndOldT).end()
    NewFile.write(EndOldT[TemporaryBeginImports:TemporaryFinishImports])

    TemporaryBeginList = [match.start() for match in re.finditer(r'\[', EndOldT)]
    TemporaryFinishList = [match.end() for match in re.finditer(r'\)', EndOldT)]
    # Need to add one extra import before going to code

    N = len(TemporaryBeginList)
    for i in range(0, N):
        line = EndOldT[TemporaryBeginList[i]:TemporaryFinishList[i+1]]
        NewFile.write('\n\t' + line)
    # Need to add second code as well
    # Need to make sure to keep return

    ActualV = 0
    return ActualV
