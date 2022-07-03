def ReorderLines(CSVFileName, FunctionInputVariables, IntermediateVariables, OutputVariables, Folder_Main,
                 Folder_Temporary, Folder_Merging):
    """
    Description : Put the models functions inside the global system Python file in the good order

    Input variables :
    CSVFileName : Name of the global system csv file without '.csv'
    FunctionInputVariables : list of the input variables of the global system
    Folder_Main : Main Folder containing all the code files
    Folder_Temporary : Folder with all the Temporary files
    Folder_Merging : Folder with all the merging algorithms

    Output variables : output is useless in our algorithm. Can be changed
    M : not assigned and useless
    """
    # Importing Modules
    import re
    from pathlib import Path
    from Functions.Sequencing.CSV2MatrixAndTables import CSV2MatrixAndTables
    from Functions.Create_x_file.TypeOfVariables import TypeOfVariables
    from Functions.Create_x_file.FromType1toType2 import FromType1toType2

    # Code
    FileV0 = CSVFileName + ".csv"
    FileV = FromType1toType2(FileV0, ".csv", ".py", "f")
    FileT = open(str(Path(Folder_Main + Folder_Temporary + "/" + FileV)), "r").read()
    NewFile = open(str(Path(Folder_Main + Folder_Temporary + "/" + FileV)), 'w+')

    Delimiter1 = re.search('(?s:.*)' + FileV[0:-3], FileT).end()
    Delimiter2 = re.search("Code", FileT[Delimiter1:]).end()
    FirstPart = FileT[0:Delimiter1 + Delimiter2]
    SecondPart = FileT[Delimiter1 + Delimiter2:]

    NewFile.write(FirstPart)

    DelimiterList1 = [match.start() for match in re.finditer(r'\[', SecondPart)]
    DelimiterList2 = [match.end() for match in re.finditer(r'\)', SecondPart)]

    Nline = len(DelimiterList2)
    LineList = [[""] * Nline for i in range(3)]
    for i in range(0, Nline):
        LineT = SecondPart[DelimiterList1[i]:DelimiterList2[i]]
        LineList[0][i] = LineT

        De1 = re.search("= ", LineT).end()
        De2 = re.search(r'\(', LineT).start()
        FunctionName = LineT[De1:De2]

        PythonName = FunctionName + ".py"
        CSVName = FromType1toType2(PythonName, '.py', '.csv', 'a')
        [MatVar, x, y, Mat] = CSV2MatrixAndTables(CSVName, Folder_Main + Folder_Temporary)
        [Input, x, Output] = TypeOfVariables(MatVar, Mat)
        LineList[1][i] = Input
        LineList[2][i] = Output
    # InputAndIntermediateVariables = list of all input variables and in the while loop we will add to this variable the
    # output variables of each function that are intermediate variables of the global system.
    InputAndIntermediateVariables = FunctionInputVariables

    h = 0
    while h < Nline - 1:
        i = 0
        while i < Nline - h:
            ListInputi = LineList[1][i]
            Ni = len(ListInputi)
            Autorize = 0
            for j in range(0, Ni):
                # looking if the Input-variable taken is already existing in the FunctionInputVariables
                if any(x in ListInputi[j] for x in InputAndIntermediateVariables):
                    Autorize = Autorize + 1

            # If all Input-variables of function are existing in the FunctionInputVariables than we have this equality
            if Autorize == Ni:
                NewFile.write("\n\t" + LineList[0][i])
                InputAndIntermediateVariables = InputAndIntermediateVariables + LineList[2][i]
                [j.pop(i) for j in LineList]
                h = h + 1
                # Need this to ignore the last line to copy (last line to copy will be done outside the while loop)
                if Nline - h == 1:
                    i = i + 1

            else:
                i = i + 1

    NewFile.write("\n\t" + LineList[0][0])

    Delimiter3 = re.search("return", SecondPart).start()
    ReturnPart = SecondPart[Delimiter3:]
    NewFile.write("\n\t" + ReturnPart)

    NewFile.close()

    return None
