def ReplaceTemporaryLineCode(OldTempoFile, ModelFile, ActualTempoFile, Folder_Main, Folder_Temporary, Folder_Merging):
    """
    Description: Inside the actual temporary file the function temporary file
    of previous temporary file need to replace what is inside (functions of
    models)

    Input variables :
    OldTempoFile : CSV file without '.csv' of the previous Temporary file
    ModelFile : CSV file without '.csv' of the added model
    ActualFile : CSV file without '.csv' of the actual temporary file
    Folder_Main : Main Folder containing all the code files
    Folder_Temporary : Folder with all the Temporary files
    Folder_Merging : Folder with all the merging algorithms

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
    ModelT = open(str(Path(Folder_Main + Folder_Temporary + "/" + ModelV)), "r").read()
    NewFile = open(str(Path(Folder_Main + Folder_Temporary + "/" + ActualV)), 'w+')

    FunctionDelimiter1 = re.search("def ", ActualT).start()
    FunctionDelimiter2 = re.search(':', ActualT[FunctionDelimiter1:]).end()
    FirstPart = ActualT[0:FunctionDelimiter1 + FunctionDelimiter2]


    NewFile.write(FirstPart)

    TemporarysearchList = re.search('(?s:.*)' + OldV[0:-3], OldT).end()

    EndOldT = OldT[TemporarysearchList:]

    # Writing imports from Old file to the New file
    TemporaryBeginImports = re.search(":", EndOldT).end()
    TemporaryFinishImports = re.search("# Code", EndOldT).start()
    NewFile.write(EndOldT[TemporaryBeginImports:TemporaryFinishImports])

    # Importing Model File
    NewFile.write('from Database.' + ModelV[0:-3])
    NewFile.write(' import ' + ModelV[0:-3] + '\n')

    # Main Code: Function calls
    NewFile.write('\t# Code')
    # Function calls in Old file
    TemporaryBeginList = [match.start() for match in re.finditer(r'\[', EndOldT)]
    TemporaryFinishList = [match.end() for match in re.finditer(r'\)', EndOldT)]

    N = len(TemporaryBeginList)
    for i in range(0, N):
        line = EndOldT[TemporaryBeginList[i]:TemporaryFinishList[i+1]]
        NewFile.write('\n\t' + line)

    # Function call from Model File
    Model_functionline_p1 = ""
    Model_functionline_p2 = ""
    for line in ModelT.splitlines():
        if line.startswith("    return"):
            Model_functionline_p1 = line[11:]
        if line.startswith("def"):
            Model_functionline_p2 = line[4:-1]
    NewFile.write('\n\t[' + Model_functionline_p1 + '] = ')
    NewFile.write(Model_functionline_p2)

    # Writing Return Statement
    FunctionDelimiter3 = re.search("return", ActualT).start()
    ReturnPart = ActualT[FunctionDelimiter3:]
    NewFile.write("\n\t" + ReturnPart)

    return ActualV
