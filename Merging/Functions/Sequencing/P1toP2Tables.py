def P1toP2Tables(OldVar, OldType, OldColor, P1, P2):
    """
    Description : Reorder the variable name table + variable type table + variable color table when change variable
    position from Position 1 to position 2 (P1<P2 always).
    This algorithm is linked with P1toP2Matrix.py

    Input variables :
    OldVar : List of variable names
    OldType : List of variable type
    OldColor : List of variable color
    P1 : Initial position of variable
    P2 : Final position of variable

    Output variables :
    NewVar : new List of variable names after ordering
    NewType : new List of variable type after ordering
    NewColor : new List of variable color after ordering
    """

    # Variables
    N = len(OldVar)
    NewVar = OldVar[:]
    NewType = OldType[:]
    NewColor = OldColor[:]

    # First part : variable in P1 go to position P2
    NewVar[P2] = OldVar[P1]  # 1 for variable name
    NewType[P2] = OldType[P1]  # 1 for variable type
    NewColor[P2] = OldColor[P1]  # 1 for variable color

    # Second part : variables before P1 don't move
    if P1 != 0:
        NewVar[0:P1] = OldVar[0:P1]  # 2 for variable name
        NewType[0:P1] = OldType[0:P1]  # 2 for variable type
        NewColor[0:P1] = OldColor[0:P1]  # 2 for variable color

    # Third part : variables after P2 don't move
    if P2 != N-1:
        NewVar[P2 + 1:N] = OldVar[P2 + 1:N]  # 3 for variable name
        NewType[P2 + 1:N] = OldType[P2 + 1:N]  # 3 for variable type
        NewColor[P2 + 1:N] = OldColor[P2 + 1:N]  # 3 for variable color

    # Last part : variable between P1 and P2 move one position on the left
    NewVar[P1:P2] = OldVar[P1 + 1:P2 + 1]  # 4 for variable name
    NewType[P1:P2] = OldType[P1 + 1:P2 + 1]  # 4 for variable type
    NewColor[P1:P2] = OldColor[P1 + 1:P2 + 1]  # 4 for variable color

    return NewVar, NewType, NewColor
