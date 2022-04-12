def P1toP2Matrix(OldMat, P1, P2):
    """
    Description : Reorder matrix when change variable position from Position 1
    to position 2 (P1<P2 always).
    Explanation in Nicky Rostan Master Thesis
    This algorithm is linked with P1toP2Tables.py

    Input variables :
    OldMat : the matrix in question
    P1 : Initial position of the variable to move
    P2 : Final position of the variable to move

    Output variables :
    NewMat : The matrix after moving a variable position.
    """
    N = len(OldMat[0])
    NewMat = [[0] * N] * N
    if P1 != 0 and P2 != N - 1:
        NewMat[P2 + 1: N - 1][0: P1 - 1] = OldMat[P2 + 1: N - 1][0: P1 - 1]  # 2
        NewMat[0: P1 - 1][P2 + 1: N - 1] = OldMat[0: P1 - 1][P2 + 1: N - 1]  # 3

    if P1 != 0:
        NewMat[0: P1 - 1][0: P1 - 1] = OldMat[0: P1 - 1][0: P1 - 1]  # 1
        NewMat[0: P1 - 1][P1: P2 - 1] = OldMat[0: P1 - 1][P1 + 1: P2]  # 5
        NewMat[0: P1 - 1][P2] = OldMat[0: P1 - 1][P1]  # 6
        NewMat[P1: P2 - 1][0: P1 - 1] = OldMat[P1 + 1: P2][0: P1 - 1]  # 9
        NewMat[P2][0: P1 - 1] = OldMat[P1][0: P1 - 1]  # 11

    if P2 != N-1:
        NewMat[P2 + 1: N - 1][P2 + 1: N - 1] = OldMat[P2 + 1: N - 1][ P2 + 1: N - 1]  # 4
        NewMat[P2 + 1: N - 1][P1: P2 - 1] = OldMat[P2 + 1: N - 1][P1 + 1: P2]  # 7
        NewMat[P2 + 1: N - 1][P2] = OldMat[P2 + 1: N - 1][P1]  # 8
        NewMat[P1: P2 - 1][P2 + 1: N - 1] = OldMat[P1 + 1: P2][P2 + 1: N - 1]  # 10
        NewMat[P2][P2 + 1: N - 1] = OldMat[P1][P2 + 1: N - 1]  # 12

    NewMat[P1: P2 - 1][P2] = OldMat[P1 + 1: P2][P1]  # 13
    NewMat[P1: P2 - 1][P1: P2 - 1] = OldMat[P1 + 1: P2][P1 + 1: P2]  # 14
    NewMat[P2][P1: P2 - 1] = OldMat[P1][P1 + 1: P2]  # 15
    NewMat[P2][P2] = OldMat[P1][P1]  # 16

    return NewMat
