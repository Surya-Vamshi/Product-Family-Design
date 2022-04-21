def Merging2DSM(MatVar1, MatType1, MatColor1, Matrix1, MatVar2, MatType2, MatColor2, Matrix2):
    """
    Description : Merging 2DSM into a new DSM -> only the tables and matrices,
    the creation of the CSV file and rename file is done in another algorithm.

    Input variables :
    PyVar1,PyVar2 : variable name table of CSV file 1 and 2
    PyType1,PyType2 : variable type table of CSV file 1 and 2
    PyColor1,PyColor2 : variable color table of CSV file 1 and 2
    Matrix1,Matrix2 : DSM of CSV file 1 and 2

    Output variables :
    PyVar : variable name table of merged DSM
    PyType : variable type table of merged DSM
    PyColor : variable color table of merged DSM
    Matrix : DSM of merged DSM
    """
    # Importing Modules
    import numpy as np
    from Functions.Sequencing.SimilarityInDSM import SimilarityInDSM

    # Code
    NbVar1 = len(MatVar1)
    [PositionDouble1, PositionUnique1, PositionDouble2, PositionUnique2] = SimilarityInDSM(MatVar1, MatVar2)
    # Adding unique variables of 2nd DSM to the variables of 1st DSM
    MatVar = MatVar1 + [e for i, e in enumerate(MatVar2) if i in PositionUnique2]
    MatType = MatType1 + [e for i, e in enumerate(MatType2) if i in PositionUnique2]
    MatColor = MatColor1 + [e for i, e in enumerate(MatColor2) if i in PositionUnique2]

    NbVar = len(MatVar)
    # Start of merging the matrix
    Matrix = np.zeros((NbVar, NbVar))  # Creating the new matrix full of zeros
    # First Part
    # Copy first DSM into new DSM
    Matrix[PositionUnique1, 0:NbVar1] = Matrix1[PositionUnique1, 0:NbVar1]
    # Step 1.a. line of Variable which are only in matrix 1
    Matrix[0:NbVar1, PositionUnique1] = Matrix1[0:NbVar1, PositionUnique1]
    # Step 1.b. Column of Variable which are only in matrix 1
    # If input and output variables are in both DSM : take max -> 1 if there is a dependency in one of the 2 matrices
    Matrix[PositionDouble1, PositionDouble1] = max(int(Matrix1[PositionDouble1, PositionDouble1]),
                                                   int(Matrix2[PositionDouble2, PositionDouble2]))
    # Second Part
    Matrix[NbVar1: NbVar, NbVar1: NbVar] = Matrix2[PositionUnique2, PositionUnique2]
    # Third Part
    # Input variables are only in 2nd DSM and Output variables are in both
    Matrix[range(NbVar1, NbVar), PositionDouble1] = Matrix2[PositionUnique2, PositionDouble2]
    # Fourth Part
    # Output variables are only in 2nd DSM and Input variables are in both
    Matrix[PositionDouble1, range(NbVar1, NbVar)] = Matrix2[PositionDouble2, PositionUnique2]

    return MatVar, MatType, MatColor, Matrix
