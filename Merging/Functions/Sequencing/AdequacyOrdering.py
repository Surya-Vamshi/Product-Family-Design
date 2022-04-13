def AdequacyOrdering(PyVar1, PyVar2, PyType2, PyColor2, Mat2):
    """
    Descirption : Ordering 2nd matrix in adequacy with first matrix

    Input variables :
    PyVar1: List with variable name of 1st CSV
    PyVar2: List with variable name of 2nd CSV
    PyType2: List with variable type of 2nd CSV
    PyColor2: List with variable color of 2nd CSV
    Mat2 : Matrix of the dependency graph of 2nd CSV

    Output variables :
    PyVar2 : List with variable name
    PyType2 : List with variable type
    PyColor2 : List with variable color
    Mat2 : Matrix of the DSM
    """
    # Importing Modules
    import numpy as np

    from Functions.Sequencing.P1toP2Tables import P1toP2Tables
    from Functions.Sequencing.P1toP2Matrix import P1toP2Matrix

    # Code
    Mat2 = np.array(Mat2)
    N1 = len(PyVar1)
    N2 = len(PyVar2)
    Step2 = 0
    for i in range(N1 - 1, -1, -1):
        Letter1 = PyVar1[i]
        for j in range(N2 - Step2 - 1, -1, -1):
            Letter2 = PyVar2[j]
            if j == (N2 - Step2):
                if Letter1 == Letter2:
                    Step2 = Step2 + 1
            else:
                if Letter1 == Letter2:
                    PyVar2, PyType2, PyColor2 = P1toP2Tables(PyVar2, PyType2, PyColor2, j, N2 - Step2 - 1)
                    Mat2 = P1toP2Matrix(Mat2, j, N2 - Step2 - 1)
                    Step2 = Step2 + 1

    return PyVar2, PyType2, PyColor2, Mat2

