def Merging2DSM(PyVar1,PyType1,PyColor1,Matrix1,PyVar2,PyType2,PyColor2,Matrix2):
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
    from Functions.Sequencing.SimilarityInDSM import SimilarityInDSM
    from Functions.Sequencing.AdequacyOrdering import AdequacyOrdering

    # Code
    NbVar1 = len(PyVar1)


    return