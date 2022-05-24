def CreatxFile(System_Name_CSV, SampleSize, Folder_Main, Folder_Database, Folder_Merging, Folder_Design_Problems,
                         Folder_Systems):
    """
    Description :
    Creat the file for the X ray tool of the Model and save it in the XFile

    Input variables :
    Model : Name of the CSV file without '.csv' at the end
    SampleSize : Number of samples
    Folder_Systems : Folder with CSV and Matlab files of the systems
    Folder_Design_Problems : Folder with the X_ray tool file of the systems
    Folder_Database : Folder with all modular models
    Folder_Merging_Algorithms : Folder with all the algorithms

    Output variables :
    Matlabx : Name of the final Matlab file for the XRay tool
    """
    # Importing Modules
    import re
    from pathlib import Path
    from Functions.Sequencing.CSV2MatrixAndTables import CSV2MatrixAndTables
    from Functions.Create_x_file.TypeOfVariables import TypeOfVariables
    from Functions.Create_x_file.FromType1toType2 import FromType1toType2

    # Code
    [MatVar, MatType, MatColor, Matrix] = CSV2MatrixAndTables(System_Name_CSV, Folder_Main + Folder_Systems)
    [Input, x, Output] = TypeOfVariables(MatVar, Matrix)
    NInput = len(Input)
    # NIntermediate = len(Intermediate)
    NOutput = len(Output)
    Pythonf = FromType1toType2(System_Name_CSV, '.csv', '.py', 'f')  # FileName
    Pythonx = FromType1toType2(System_Name_CSV, '.csv', '.py', 'x')  # FileName
    Pythons = FromType1toType2(System_Name_CSV, '.csv', '.py', 's')  # FileName
    Text = open(str(Path(Folder_Main + Folder_Systems + "/" + Pythonf)), "r").read()
    PythonWriter = open(str(Path(Folder_Main + Folder_Systems + "/" + Pythonx)), 'w+')
    # Preparation for the diagram code lines
    NDiagram = round(NOutput / 2)
    DiagramList = "["
    for i in range(1, NDiagram + 1):
        DiagramList = DiagramList + str(i*2-1) + " " + str(i*2)
    DiagramList = DiagramList + "]"

    # Beginning
    PythonWriter.write("# " + Pythonx + "\n\n\n")
    PythonWriter.write("# Code:\n")
    PythonWriter.write("class " + Pythonx[:-3] + ":")
    PythonWriter.write("\n\tdef __init__(self):")
    PythonWriter.write("\n\t\t# --------------------------------------------------")
    PythonWriter.write("\n\t\t#            Definitions of variables")
    PythonWriter.write("\n\t\t# --------------------------------------------------")
    PythonWriter.write("\n\t\tself.x = {}  # Design variables")
    PythonWriter.write("\n\t\tself.y = {}  # Quantities of interest")
    PythonWriter.write("\n\t\tself.p = {}")
    PythonWriter.write("\n\t\tself.index = {}")
    PythonWriter.write("\n\t\tself.samples = {}")
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\t# --------------------------------------------------")
    PythonWriter.write("\n\t\t#            Input variables")
    PythonWriter.write("\n\t\t# --------------------------------------------------")
    PythonWriter.write("\n\t\tself.sampleSize = 0  # Number of samples")
    PythonWriter.write("\n\t\tself.diagram = []  # Diagram list")
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\tself.m = 0  # Number of quantities of interest")
    PythonWriter.write("\n\t\tself.d = 0  # Number of design variables")
    PythonWriter.write("\n\t\tself.np = 0  # Number of parameters")
    PythonWriter.write("\n\t\tself.k = 0  # necessary for plot_m_x")
    PythonWriter.write("\n\t\tself.b = 0  # necessary for writeInputOutput")
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\tself.good_design_color = 'green'  # Color of good designs")
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\t# Line definition for solution spaces")
    PythonWriter.write("\n\t\tself.solutionspace_line_color = 'black'")
    PythonWriter.write("\n\t\tself.solutionspace_line_width = 2")
    PythonWriter.write("\n\t\tself.solutionspace_line_type = '--'")
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\tself.legend = ''  # Legend text")
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\tself.save_as = '" + Pythons + "'  # Filename of saved file")
    PythonWriter.write("\n\t\t")

    # Methods







    PythonWriter.close()
    Pythonx = "Not yet done"

    return Pythonx