def SimilarityInDSM(Var1, Var2):
    """
    Description : Give the position of variables that are present in Var 1
    and Var 2 and the one that are only in Var1 and the one that are only in
    Var2

    Input variables :
    Var1 : variables of first DSM
    Var2 : variables of second DSM

    Output Variables :
    PositionDb1, PositionDb2 : position of variables that are present in Var1 / Var2
    PositionUnik1, PositionUnik2 : position of variables that are only in Var1 / Var2
    """
    # Importing Modules
    from Functions.Sequencing.SimilaritiesInDSMFor2ndCell import SimilaritiesInDSMFor2ndCell

    # Code
    PositionDb1, PositionUnik1 = SimilaritiesInDSMFor2ndCell(Var2, Var1)  # Positions in Variable1
    PositionDb2, PositionUnik2 = SimilaritiesInDSMFor2ndCell(Var1, Var2)  # Positions in Variable2

    return PositionDb1, PositionUnik1, PositionDb2, PositionUnik2
