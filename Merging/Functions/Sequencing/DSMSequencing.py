def DSMSequencing(MatVar, MatType, MatColor, Matrix):
    """
    Description : Sequencing of a DSM (inputs are the matrix + the 3 Lists
    with name, type and color of variable)

    Input variables :
    Matrix : Matrix of the dependency graph
    MatVar : 1: List with variable name
    MatType : 1: List with variable type
    MatColor : 1: List with variable color

    Output variables :
    Matrix : Matrix of the dependency graph
    MatVar : 1: List with variable name
    MatType : 1: List with variable type
    MatColor : 1: List with variable color
    """
    # Importing Modules
    import numpy as np
    from Functions.Sequencing.P1toP2Tables import P1toP2Tables
    from Functions.Sequencing.P1toP2Matrix import P1toP2Matrix

    # Code
    StepCounting = 0
    # StepCounting is counting the number of line that are respecting the rule underdiagonal is full of zero starting
    # from the end of the matrix
    NbOfVar = len(MatVar)
    while StepCounting < NbOfVar:

        Step = StepCounting  # When a line is correct, we interest ourself with the matrix of smaller dimension (NbOfVar-Step)
        for i in reversed(range(0, NbOfVar - Step)):  # Always starting from the last line end go up
            LineAnalyzed = Matrix[i, 0:NbOfVar - Step]
            SumZeros = LineAnalyzed.sum(axis=0)
            if np.all((SumZeros == 0)):  # If full of 0 : line respect rule : add 1 to the variable StepCounting after the following if
                if i < NbOfVar - StepCounting:  # this is verified when at least one line before has a 1. So this line is put at the end of the small matrix end all other line are pushed 1 line at the top
                    [MatVar, MatType, MatColor] = P1toP2Tables(MatVar, MatType, MatColor, i, NbOfVar - Step - 1)  # Move the line to the last line of the small matrix, lines between P1 and P2 are pushed 1 line at the top
                    Matrix = P1toP2Matrix(Matrix, i, NbOfVar - Step - 1)
                StepCounting = StepCounting + 1

    return MatVar, MatType, MatColor, Matrix
