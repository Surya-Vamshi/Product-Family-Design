def CSV2MatrixAndTables(CSV, Path):
    """
    Descirption : From csv file to 3 lines (variable name, variable type and
    variable color) + matrix of DSM

    Input variables :
    CSV : csv file with '.csv'
    Path : folder where the csv file is saved

    Output variables :
    PyVar : List with variable name
    PyType : List with variable type
    PyColor : List with variable color
    Matrix : Matrix of the DSM
    """
    # Importing Modules
    import csv

    # Reading CSV Files
    with open(Path+'\\'+CSV, newline='') as f:
        reader = csv.reader(f)
        listAll = list(reader)

    # Assigning Values
    PyVar = listAll[0]
    PyType = listAll[1]
    PyColor = listAll[2]
    Matrix = listAll[3:]
    print(Matrix)

    return PyVar, PyType, PyColor, Matrix
