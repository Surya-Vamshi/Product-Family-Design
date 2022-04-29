def Merging2Python(Model1, Model2, Model3, Folder_Main, Folder_Temporary, Folder_Merging_Funtions,
                   Folder_Merging_Sequencing, Folder_Merging_Create_x_file):
    """
    Description : Merging 2 Python file of 2 models into a merged file (no ordering system)

    Input variables :
    Model1 : CSV file of first model without '.csv'
    Model2 : CSV file of second model without '.csv'
    Model3 : CSV file of merged model without '.csv'

    Output variables :
    Input3 : list of input variables of the merged model
    Intermediate3 : list of intermediate variables of the merged model
    Output3 : list of output variables of the merged model
    """
    # Importing Modules
    from Functions.Sequencing.CSV2MatrixAndTables import CSV2MatrixAndTables
    from Functions.Create_x_file.TypeOfVariables import TypeOfVariables
    from Functions.Create_x_file.OneVarIn2ndList import OneVarIn2ndList
    from Functions.Create_x_file.FromType1toType2 import FromType1toType2
    from Functions.Create_x_file.VariablesOfList2inList1orNot import VariablesOfList2inList1orNot
    from Functions.Create_x_file.WriteVariableDescription import WriteVariableDescription

    # Code
    CSV1 = Model1 + ".csv"
    CSV2 = Model2 + ".csv"
    CSV3 = Model3 + ".csv"
    # 2 Functions to Merge
    [MatVar1, MatType1, MatColor1, Matrix1] = CSV2MatrixAndTables(CSV1, Folder_Main + Folder_Temporary)
    [MatVar2, MatType2, MatColor2, Matrix2] = CSV2MatrixAndTables(CSV2, Folder_Main + Folder_Temporary)
    [MatVar3, MatType3, MatColor3, Matrix3] = CSV2MatrixAndTables(CSV3, Folder_Main + Folder_Temporary)
    # Input, Intermediates, Outputs
    [Input1, Intermediate1, Output1] = TypeOfVariables(MatVar1, Matrix1)
    [Input3, Intermediate3, Output3] = TypeOfVariables(MatVar3, Matrix3)

    # Should remove code from here to
    Input1 = ['T_in', 'n_in', 'i']
    Input3 = ['i_1', 'i_2', 'n_in', 'T_in']
    Intermediate3 = ['i']
    Output3 = ['T_out', 'n_out']
    # Till here

    VerifVar = OneVarIn2ndList(Input1, Intermediate3)

    # if in 1st CSV file Inputs are Intermediate variables of the final system. Then need to change position of both
    # matrix by inverse them and the files
    if VerifVar == 1:  # That is when VerifVar = 1
        MatVarA = MatVar2
        MatVar2 = MatVar1
        MatVar1 = MatVarA
        CSVA = CSV2
        CSV2 = CSV1
        CSV1 = CSVA
    # Now File1/CSV1 is first!
    # Creating.py file name from .csv
    Python1 = FromType1toType2(CSV1, '.csv', '.py', 'f')  # FileName
    Python2 = FromType1toType2(CSV2, '.csv', '.py', 'f')  # FileName
    # TXT3 = FromType1toType2(CSV3, '.csv', '.txt', 'f'); # FileName
    Python3 = FromType1toType2(CSV3, '.csv', '.py', 'f')
    Text1 = open(Folder_Main + Folder_Temporary + "\\" + Python1, "r").read()
    Text2 = open(Folder_Main + Folder_Temporary + "\\" + Python2, "r").read()
    Python3Writer = open(Folder_Main + Folder_Temporary + "\\" + Python3, 'w+')

    # START OF WRITING THE NEW FILE
    Python3Writer.write('"""\n')  # Commenting
    Python3Writer.write(Python3)  # Title
    Python3Writer.write('\n\nDescription:')  # Description

    [x, UnikInMatVar2] = VariablesOfList2inList1orNot(MatVar1, MatVar2)
    VariableList = MatVar1 + UnikInMatVar2

    # Input
    Text_input = WriteVariableDescription(Text1, Text2, '', Python3Writer, VariableList, Input3, 'Input',
                                          'Intermediate')
    # Intermediate
    WriteVariableDescription(Text1, Text2, Text_input, Python3Writer, VariableList, Intermediate3, 'Intermediate',
                             'Output')
    # Output
    WriteVariableDescription(Text1, Text2, '', Python3Writer, VariableList, Output3, 'Output', 'Example')

    # Example
    Python3Writer.write('\n\nExample:\n')
    # Formula
    Python3Writer.write('\nFormula:\n\n')
    # Code
    Python3Writer.write('"""\n#  Code:\n')

    # Import line
    Python3Writer.write('\nimport numpy as np\n\n')
    # Function line
    Python3Writer.write('\ndef ')
    Python3Writer.write(Python3[0:-3] + '(')

    Input3 = ['i_1', 'i_2', 'n_in', 'T_in']  # Should be removed
    Output3 = ['T_out', 'n_out']  # Should be removed
    for i in Input3:
        Python3Writer.write(i)
        if i == Input3[-1]:
            Python3Writer.write('):\n')
        else:
            Python3Writer.write(', ')

    # Need to import modules to run the code
    Python3Writer.write('\tfrom Database.' + Python1[0:-3])
    Python3Writer.write(' import ' + Python1[0:-3] + '\n')
    Python3Writer.write('\tfrom Database.' + Python2[0:-3])
    Python3Writer.write(' import ' + Python2[0:-3] + '\n')

    # Functions and Main part
    Text1_functionline_p1 = ""
    Text1_functionline_p2 = ""
    Text2_functionline_p1 = ""
    Text2_functionline_p2 = ""
    for line in Text1.splitlines():
        if line.startswith("    return"):
            Text1_functionline_p1 = line[11:]
        if line.startswith("def"):
            Text1_functionline_p2 = line[4:-1]
    for line in Text2.splitlines():
        if line.startswith("    return"):
            Text2_functionline_p1 = line[11:]
        if line.startswith("def"):
            Text2_functionline_p2 = line[4:-1]
    Python3Writer.write('\t# Code\n')
    Python3Writer.write('\t[' + Text1_functionline_p1 + '] = ')
    Python3Writer.write(Text1_functionline_p2)
    Python3Writer.write('\n\t[' + Text2_functionline_p1 + '] = ')
    Python3Writer.write(Text2_functionline_p2)

    # Return Statement along with output variables
    Python3Writer.write('\n\treturn ')
    for i in Output3:
        Python3Writer.write(i)
        if i == Output3[-1]:
            Python3Writer.write('\n')
        else:
            Python3Writer.write(', ')

    return Input3, Intermediate3, Output3
