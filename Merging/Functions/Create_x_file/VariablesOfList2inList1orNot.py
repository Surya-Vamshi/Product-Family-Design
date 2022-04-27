def VariablesOfList2inList1orNot(List1, List2):
    """
    Description : Give the variable of list 2 that are in list 1 and the
    variable of list 2 that aren't in list 1 in 2 different lists

    Input variables :
    List1 : First List
    List2 : Second List

    Output variables :
    InList1 : List of variable of list2 that are in list 1
    NotInList1 : List of variable of list2 that aren't in list 1
    """
    InList1 = []
    NotInList1 = []
    N = len(List2)
    for i in range(0, N):
        if List2[i] in List1:  # analyze if variable is in list 1 or not
            InList1.append(List2[i])
        else:  # If this is verified then variable is not in list 1
            NotInList1.append(List2[i])
    return InList1, NotInList1
