def AdequacyOrdering(MatVar1, MatVar2, MatType2, MatColor2, Mat2):
    """
    Descirption : Ordering 2nd matrix in adequacy with first matrix

    Input variables :
    MatVar1: List with variable name of 1st CSV
    MatVar2: List with variable name of 2nd CSV
    MatType2: List with variable type of 2nd CSV
    MatColor2: List with variable color of 2nd CSV
    Mat2 : Matrix of the dependency graph of 2nd CSV

    Output variables :
    MatVar2 : List with variable name
    MatType2 : List with variable type
    MatColor2 : List with variable color
    Mat2 : Matrix of the DSM
    """
    # Importing Modules
    import numpy as np

    from Functions.Sequencing.P1toP2Tables import P1toP2Tables
    from Functions.Sequencing.P1toP2Matrix import P1toP2Matrix

    # Code
    Mat2 = np.array(Mat2)
    N1 = len(MatVar1)
    N2 = len(MatVar2)
    Step2 = 0
    for i in range(N1 - 1, -1, -1):
        Letter1 = MatVar1[i]
        for j in range(N2 - Step2 - 1, -1, -1):
            Letter2 = MatVar2[j]
            if j == (N2 - Step2):
                if Letter1 == Letter2:
                    Step2 = Step2 + 1
            else:
                if Letter1 == Letter2:
                    MatVar2, MatType2, MatColor2 = P1toP2Tables(MatVar2, MatType2, MatColor2, j, N2 - Step2 - 1)
                    Mat2 = P1toP2Matrix(Mat2, j, N2 - Step2 - 1)
                    Step2 = Step2 + 1

    return MatVar2, MatType2, MatColor2, Mat2

