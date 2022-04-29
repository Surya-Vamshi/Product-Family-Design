def WriteVariableDescription(Text1, Text2, TextForIntermediate, Pythonfile, AllVariablesList, AnalyzedVariablesList,
                             VariableType, NextVariableType):
    """
    Description : Write in the Python file the description of the variables of
    the AnalyzedVariablesList (it will be the input, intermediate or output
    variables of the model)

    Input variables :
    Text1 : Python file of the first model
    Text2 : Python file of the second model
    TextForIntermediate : use for the intermediate variables
    Pythonfile : Name of the new
    AllVariablesList : list of all variables of the model
    AnalyzedVariablesList : list of variables that are of the Type
    VariableType : Type of variables group (input,intermediate or output variables)
    NextVariableType : Type of the next variables group (input,intermediate or output variables)

    The 2 last variables -> we use this to help the algorithm to see the beginning
    and the end of the text to analyze -> only the input/intermediate/output variables

    Output Variables :
    Text : the text that is written in the Python file during the algorithm
    """
    # Importing Modules
    import re  # For regular expression operations

    # Code
    Text = "Nothing"
    Type1 = VariableType + ":"  # beginning of the type of variables (input,intermediate or output variables)
    Type2 = NextVariableType + ":"  # end of the type of variables (input,intermediate or output variables)
    Pythonfile.write('\n\n' + Type1)
    Text1_p1 = re.search(Type1, Text1).end()  # take the position in the text1 of the word Type1
    Text1_p2 = re.search(Type2, Text1).start()  # take the position in the text1 of the word Type2
    Text1_2 = Text1[Text1_p1:Text1_p2]  # take only the text between the 2 limits (Text1_p1 and Text1_p2)
    Text2_p1 = re.search(Type1, Text2).end()
    Text2_p2 = re.search(Type2, Text2).start()
    Text2_2 = Text2[Text2_p1:Text2_p2]
    Text = Text1_2 + Text2_2 + TextForIntermediate
    # Text = Merging the texts of the 2 input models with the variable's description
    # Intermediate of total system are : the intermediate of 1 and 2 but also
    # the inputs that become intermediate when merging
    N = len(AnalyzedVariablesList)
    if N > 0:
        for i in range(0, N):
            Variable = AnalyzedVariablesList[i]
            VariableT = Variable + " = "  # variable (+ ' =') to search in the Text
            if Variable in AllVariablesList:  # If the variable is listed in all variables list, write the
                # description in the new Pythonfile
                Text_p1 = re.search(VariableT, Text).start()
                Text_p1 = Text_p1
                Text_p2 = re.search(']', Text[Text_p1:]).start()
                Pythonfile.write('\n\t' + Text[Text_p1:Text_p1 + Text_p2 + 1])

    return Text
