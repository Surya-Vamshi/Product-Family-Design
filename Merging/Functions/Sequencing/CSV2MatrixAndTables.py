def CSV2MatrixAndTables(CSV, path):
    """
    Descirption : From csv file to 3 lines (variable name, variable type and
    variable color) + matrix of DSM

    Input variables :
    CSV : csv file with '.csv'
    path : folder where the csv file is saved

    Output variables :
    MatVar : List with variable name
    MatType : List with variable type
    MatColor : List with variable color
    Matrix : Matrix of the DSM
    """
    # Importing Modules
    import csv
    import numpy as np
    from pathlib import Path

    # Reading CSV Files
    with open(str(Path(path+'/'+CSV)), newline='') as f:
        reader = csv.reader(f)
        listAll = list(reader)

    # Assigning Values
    MatVar = listAll[0]
    MatType = listAll[1]
    MatColor = listAll[2]
    Matrix = listAll[3:]
    Matrix = np.array(Matrix)

    return MatVar, MatType, MatColor, Matrix
