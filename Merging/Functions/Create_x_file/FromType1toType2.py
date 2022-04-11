def FromType1toType2(NameWithType1, Type1, Type2, Prefix2):
    """
    Description : Create the name of a file with the help of the name of
    another file type with the same file name (_a_.csv, _f_.m, etc)

    Input variables :
    NameWithType1 : the name of the file with the initial Type1
    Type1 : the type of file it come from
    Type2 : the type of file you want
    Prefix2 : depending on the type you want you need to add the '_a_' or '_f_' etc in front (after MXXXX)

    Output variables :
    NameType2 : name of file with the final type2
    """

    N = len(Type1)
    Prefix1 = NameWithType1[0:5]
    NameModel = NameWithType1[8:-N]
    NameWithType2 = Prefix1 + "_" + Prefix2 + "_" + NameModel + Type2

    return NameWithType2
