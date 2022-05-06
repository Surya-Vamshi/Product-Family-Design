def System_XRay_From_Models(CODEs, System_Name, SampleSize, Folder_Main, Folder_Design_Problems, Folder_Systems,
                            Folder_Database, Folder_Merging_Funtions, Folder_Merging_Sequencing,
                            Folder_Merging_Create_x_file):
    """
    Description :
    Merging of models into a global system with a Sequenced DSM in a CSV file + function of the system
    in a Python file and another Python file ready to be used in the XRay tool.
    
    Input variables :
    CODEs : list of code of the modular models used in the system (which are going to be merged.)
    THE FORMAT SHOULD BE : [{'MXXXX'},{'MXXXX'},{'MXXXX'},{'MXXXX'}]
    System_Name : Name of the System (without "SXXXX_a_" and ".csv")
    
    SampleSize : Number of samples 
    Folder_Main : Main Folder containing all the code files
    Folder_Design_Problems : Folder with the X_ray tool file of the systems
    Folder_Systems : Folder with CSV and Python files of the systems
    Folder_Database : Folder with all modular models
    Folder_Merging_Funtions : Folder with all the merging algorithms
    Folder_Merging_Sequencing : Folder with all the Sequencing algorithms
    Folder_Merging_Create_x_file :Folder with all the Create_x_file algorithms
    
    TemporaryFolder : Name of the folder for the algorithm. Can be a random name 
    (will be creat and deleted in the algorithm was important for the programming work)
    
    Output variables :
    CSVFinal : Name of Final CSV File with the system global function
    Pythonx : Name of the final Python file for the XRay tool 
    """

    # Importing Modules
    from Functions.MergingIntoSystem import MergingIntoSystem
    from Functions.CreatxFile import CreatxFile

    # Merging
    CSVFinal = MergingIntoSystem(CODEs, System_Name, Folder_Main, Folder_Systems, Folder_Database,
                                 Folder_Merging_Funtions, Folder_Merging_Sequencing, Folder_Merging_Create_x_file)

    # Creation of the file for the XRay tool
    Pythonx = CreatxFile(CSVFinal, SampleSize, Folder_Main, Folder_Design_Problems, Folder_Systems, Folder_Database,
                         Folder_Merging_Funtions, Folder_Merging_Sequencing, Folder_Merging_Create_x_file)

    return CSVFinal, Pythonx
