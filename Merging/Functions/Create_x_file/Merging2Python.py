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

    VerifVar = OneVarIn2ndList(Input1, Intermediate3)
    # if in 1st CSV file Inputs are Intermediate variables of the final system. Then need to change position of both matrix by inverse them and the files
    if VerifVar == 1: #That is when VerifVar = 1


    Input3 = "Not yet done"
    Intermediate3 = "Not yet done"
    Output3 = "Not yet done"
    return Input3, Intermediate3, Output3
