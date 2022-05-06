def TypeOfVariables(MatVar, Matrix):
    """
    Description : Give the type of variable of the variables of the DSM. The
    type can be input, intermediate or output variable

    Input Variables :
    MatVar : list of variable of the DSM
    Matrix : matrix of the DSM (order respected of course)

    Output Variables :
    Input : list of variable that are input variables
    Intermediate : list of variable that are intermediate variables
    Output : list of variable that are output variables
    """
    # Importing Modules
    import numpy as np

    Input = []
    Intermediate = []
    Output = []
    N = len(MatVar)
    Matrix = Matrix.astype('float')
    Sums1 = np.sum(Matrix, axis=0)
    Sums2 = np.sum(Matrix, axis=1)

    for i in range(0, N):
        if Sums1[i] == 0:
            Input.append(MatVar[i])
        if Sums2[i] == 0:
            Output.append(MatVar[i])
        if Sums1[i] != 0 and Sums2[i] != 0:
            Intermediate.append(MatVar[i])

    return Input, Intermediate, Output
