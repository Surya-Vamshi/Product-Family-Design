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
    import shutil
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
        DiagramList = DiagramList + str(i*2-1) + ", " + str(i*2)
    DiagramList = DiagramList + "]"

    # Beginning
    PythonWriter.write("# " + Pythonx + "\n\n\n")
    PythonWriter.write("# Code:\n")
    PythonWriter.write("class " + Pythonx[:-3] + ":")
    PythonWriter.write("\n\t")
    PythonWriter.write("\n\t# --------------------------------------------------")
    PythonWriter.write("\n\t#            Definitions of variables")
    PythonWriter.write("\n\t# --------------------------------------------------")
    PythonWriter.write("\n\tx = [{}")
    for i in range(0, len(Input)-1):
        PythonWriter.write(", {}")
    PythonWriter.write("]  # Design variables")
    PythonWriter.write("\n\ty = [{}")
    for i in range(0, len(Output)-1):
        PythonWriter.write(", {}")
    PythonWriter.write("]  # Quantities of interest")
    PythonWriter.write("\n\tp = []")
    PythonWriter.write("\n\tindex = {}")
    PythonWriter.write('\n\tsamples = {"marker": {}}')
    PythonWriter.write("\n\t")
    PythonWriter.write("\n\t# --------------------------------------------------")
    PythonWriter.write("\n\t#            Input variables")
    PythonWriter.write("\n\t# --------------------------------------------------")
    PythonWriter.write("\n\tsampleSize = 0  # Number of samples")
    PythonWriter.write("\n\tdiagram = []  # Diagram list")
    PythonWriter.write("\n\t")
    PythonWriter.write("\n\tm = 0  # Number of quantities of interest")
    PythonWriter.write("\n\td = 0  # Number of design variables")
    PythonWriter.write("\n\tnp = 0  # Number of parameters")
    PythonWriter.write("\n\tk = 0  # necessary for plot_m_x")
    PythonWriter.write("\n\tb = 0  # necessary for writeInputOutput")
    PythonWriter.write("\n\t")
    PythonWriter.write("\n\tgood_design_color = 'green'  # Color of good designs")
    PythonWriter.write("\n\t")
    PythonWriter.write("\n\t# Line definition for solution spaces")
    PythonWriter.write("\n\tsolutionspace_line_color = 'black'")
    PythonWriter.write("\n\tsolutionspace_line_width = 2")
    PythonWriter.write("\n\tsolutionspace_line_type = '--'")
    PythonWriter.write("\n\t")
    PythonWriter.write("\n\tlegend = ''  # Legend text")
    PythonWriter.write("\n\t")
    # ------------------------ Need to edit this save data------------------------------
    PythonWriter.write("\n\tsave_as = '" + Pythons + "'  # Filename of saved file")
    PythonWriter.write("\n\t")

    # Methods/ Functions
    PythonWriter.write("\n\t# --------------------------------------------------")
    PythonWriter.write("\n\t#            Functions")
    PythonWriter.write("\n\t# --------------------------------------------------")
    PythonWriter.write("\n\tdef __init__(self):")
    # ------------------------ Need to try loading saved data ----------------------------------
    PythonWriter.write("\n\t\tself.sampleSize = " + str(SampleSize))
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\tself.diagram = " + DiagramList + "  # Choosing variables to be shown in the diagrams")
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\t# Design Variables")
    PythonWriter.write("\n\t\tdesign_variables = [")
    for i in range(0, NInput):
        for j in range(0, len(MatVar)):
            if Input[i] == MatVar[j]:
                TypeOfTheVar = MatType[j]
        PythonWriter.write("\n\t\t\t['" + Input[i] + "', '" + TypeOfTheVar + "',  0, 100]")
        if i != NInput-1:
            PythonWriter.write(",")
    PythonWriter.write("\n\t\t]")
    PythonWriter.write("\n\t\t")
    # Design variables
    PythonWriter.write("\n\t\t# Design variables 2")
    PythonWriter.write("\n\t\tfor i in range(0, len(design_variables)):")
    PythonWriter.write('\n\t\t\tself.x[i]["name"] = design_variables[i][0]')
    PythonWriter.write('\n\t\t\tself.x[i]["unit"] = design_variables[i][1]')
    PythonWriter.write('\n\t\t\tself.x[i]["dsl"] = design_variables[i][2]')
    PythonWriter.write('\n\t\t\tself.x[i]["dsu"] = design_variables[i][3]')
    PythonWriter.write('\n\t\t\tself.x[i]["l"] = design_variables[i][2]')
    PythonWriter.write('\n\t\t\tself.x[i]["u"] = design_variables[i][3]')
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\t# Quantities of interest")
    PythonWriter.write("\n\t\tquantities_of_interest = [")
    for i in range(0, NOutput):
        for j in range(0, len(MatVar)):
            if Output[i] == MatVar[j]:
                TypeOfTheVar = MatType[j]
                ColorOfTheVar = MatColor[j]
        rgb = [1, 0, 0]
        # ------------------------ Need to try getting RGB colours list ----------------------------------
        PythonWriter.write("\n\t\t\t['" + Output[i] + "', '" + TypeOfTheVar + "', " + str(rgb) + ",  0, 200, 1]")
        if i != NOutput-1:
            PythonWriter.write(",")
    PythonWriter.write("\n\t\t]")
    PythonWriter.write("\n\t\t")
    # Quantities of interest
    PythonWriter.write("\n\t\t# Quantities of interest 2")
    PythonWriter.write("\n\t\tfor i in range(0, len(quantities_of_interest)):")
    PythonWriter.write('\n\t\t\tself.y[i]["name"] = quantities_of_interest[i][0]')
    PythonWriter.write('\n\t\t\tself.y[i]["unit"] = quantities_of_interest[i][1]')
    PythonWriter.write('\n\t\t\tself.y[i]["color"] = quantities_of_interest[i][2]')
    PythonWriter.write('\n\t\t\tself.y[i]["l"] = quantities_of_interest[i][3]')
    PythonWriter.write('\n\t\t\tself.y[i]["u"] = quantities_of_interest[i][4]')
    PythonWriter.write('\n\t\t\tself.y[i]["active"] = quantities_of_interest[i][5]')
    PythonWriter.write('\n\t\t\tself.y[i]["condition"] = "Violating " + quantities_of_interest[i][0]')
    PythonWriter.write("\n\t\t")
    # Parameters
    PythonWriter.write("\n\t\t# Parameters")
    PythonWriter.write("\n\t\tparameters = [")
    PythonWriter.write("\n\t\t\t# Text parameters %'Name','Unit',15.6")
    # For now this is empty
    parameters = []
    PythonWriter.write("\n\t\t]")
    PythonWriter.write("\n\t\tself.p = [")
    for i in range(0, len(parameters)-1):
        PythonWriter.write("{}, ")
    if len(parameters) > 0:
        print("{}")
    PythonWriter.write("]")
    PythonWriter.write("\n\t\t# Parameters 2")
    PythonWriter.write("\n\t\tfor i in range(0, len(parameters)):")
    PythonWriter.write('\n\t\t\tself.p[i]["name"] = parameters[i][0]')
    PythonWriter.write('\n\t\t\tself.p[i]["unit"] = parameters[i][1]')
    PythonWriter.write('\n\t\t\tself.p[i]["value"] = parameters[i][2]')
    PythonWriter.write("\n\t\t")

    # Marker size
    PythonWriter.write("\n\t\t# Marker size of samples")
    PythonWriter.write('\n\t\tself.samples["marker"]["size"] = 10')
    PythonWriter.write('\n\t\tself.samples["marker"]["type"] = "."')
    PythonWriter.write("\n\t\tself.m = len(self.y)")
    PythonWriter.write("\n\t\tself.d = len(self.x)")
    PythonWriter.write("\n\t\tself.np = len(self.p)")
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\tself.legend = self.CreateLegend(self.y)  # Legende erstellen vereinfacht durch Steger")
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\tself.k = 0")
    PythonWriter.write("\n\t\tself.b = 0")
    PythonWriter.write("\n\t\t")

    # System response Function
    PythonWriter.write("\n\t# Calculates system response")
    PythonWriter.write("\n\tdef SystemResponse(self, x):")
    PythonWriter.write("\n\t\t# Importing modules")
    systemimport = Folder_Systems[1:].replace('\\', ".")
    systemimport = systemimport.replace("/", ".")
    PythonWriter.write("\n\t\tfrom " + systemimport + ".")
    PythonWriter.write(Pythonf[:-3] + " import " + Pythonf[:-3])
    PythonWriter.write("\n\t\t")
    PythonWriter.write("\n\t\t# Function:")
    PythonWriter.write("\n\t\ty = [[]")
    for i in range(0, len(Output)-1):
        PythonWriter.write(", []")
    PythonWriter.write("]")
    PythonWriter.write("\n\t\t[y[")
    for i in range(0, len(Output)):
        PythonWriter.write(str(i))
        if i == len(Output)-1:
            PythonWriter.write("]] = ")
        else:
            PythonWriter.write("], y[")
    PythonWriter.write(Pythonf[:-3])
    PythonWriter.write("(x[")
    for i in range(0, len(Input)):
        PythonWriter.write(str(i))
        if i == len(Input) - 1:
            PythonWriter.write("])")
        else:
            PythonWriter.write("], x[")
    PythonWriter.write("\n\t\treturn y")

    # CreateLegend Function
    PythonWriter.write("\n\t")
    PythonWriter.write("\n\tdef CreateLegend(self, y):")
    PythonWriter.write('\n\t\tlegend = ["{\color{green} \ bullet }Good design"]')
    PythonWriter.write('\n\t\tfor i in range(0, self.m):')
    PythonWriter.write('\n\t\t\tif self.y[i]["active"] == 1:')
    PythonWriter.write('\n\t\t\t\tlegend.append("{\color[rgb]{" + str(self.y[i]["color"])')
    PythonWriter.write(' + "]} \ bullet }" + str(self.y[i]["condition"]))')
    PythonWriter.write('\n\t\treturn legend')
    PythonWriter.write('\n\t\t')

    PythonWriter.close()

    # Moving the x file to Design Problems Folder
    shutil.move(Path(Folder_Main+Folder_Systems +"/"+ Pythonx), Path(Folder_Main+Folder_Design_Problems +"/"+ Pythonx))

    return Pythonx