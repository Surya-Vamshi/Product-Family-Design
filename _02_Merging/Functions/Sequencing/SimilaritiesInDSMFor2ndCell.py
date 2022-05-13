def SimilaritiesInDSMFor2ndCell(Var1, Var2):  # Positions in Cell2
    """"
    Description : Give the position in Var2 of variables that are present in Var 1
    and Var 2 and the one that are only in Var2

    Input variables :
    Var1 : Variables of first DSM
    Var2 : Variables of second DSM

    Output Variables :
    PositionDb : position of variables that are present in Var1 and Var2
    PositionUnik : position of variables that are only in Var 2
    """
    # Code
    VarDb = []
    VarUnik = []
    for i in range(0, len(Var2)):
        Detector = 0
        for j in range(0, len(Var1)):
            if Var2[i] == Var1[j]:
                VarDb.append(i)
                Detector = 1

        if Detector == 0:
            VarUnik.append(i)

    PositionDb = VarDb  # Positions in Cell2
    PositionUnik = VarUnik  # Positions in Cell2

    return PositionDb, PositionUnik
