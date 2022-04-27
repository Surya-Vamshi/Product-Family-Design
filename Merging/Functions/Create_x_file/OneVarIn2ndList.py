def OneVarIn2ndList(List1, List2):
    """
    Description : Check if there is at least 1 variable of first list in the
    second list.

    Input variables :
    List1 : list of variables to check
    List2 : list of variables to see if it is inside

    Output variables :
    VerifVar : Is equal to 1 if there is at least 1 variable of first list in
    the second list. else equal to 0
    """
    VerifVar = 0
    N = len(List1)
    flag = 0
    for i in range(0, N):
        if List1[i] in List2:  # Look if the variable is equal to one of the variable of the second list
            flag = 1  # if the variable is present in second list, flag is equal to 1
    if flag == 1:  # the variable is present in second list
        VerifVar = 1
    return VerifVar
