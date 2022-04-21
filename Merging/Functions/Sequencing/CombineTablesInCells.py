def CombineTablesInCells(MatVar, MatType, MatColor, Matrix):
    """
    Descirption : Combine the table of variable, type, color and the matrix
    into a big cell

    Input variables :
    MatVar : 1: table with variable name
    MatType : 1: table with variable type
    MatColor : 1: table with variable color
    Matrix : Matrix of the DSM

    Output variables :
    FinalCell : The Combined Cell with variables,type,Color and matrix
    """
    # Importing Modules
    import numpy as np

    # Assigning Values
    FinalCell = []
    FinalCell[0] = MatVar
    FinalCell[1] = MatType
    FinalCell[2] = MatColor
    Matrix = Matrix.tolist()
    #FinalCell[3] = Matrix
    print(FinalCell)

    return FinalCell
