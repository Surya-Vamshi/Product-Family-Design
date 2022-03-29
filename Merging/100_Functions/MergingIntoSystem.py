def MergingIntoSystem(CODEs,System_Name,Folder_Main,Folder_Systems,Folder_Database,Folder_Merging_Funtions,
                            Folder_Merging_Sequencing,Folder_Merging_Create_x_file):
    """
    Description : Merging models into the global system with DSM Sequencing and
    system function depending of the models function in a python file
    
    Input variables :
    CODEs : list of code of the modular models used in the system (which are going to be merged.)
    THE FORMAT SHOULD BE : [{'MXXXX'},{'MXXXX'},{'MXXXX'},{'MXXXX'}]
    System_Name : name of the system (without "SXXXX_a_" and ".csv")
    Folder_Main : Main Folder containing all the code files
    Folder_Systems : Folder with CSV and Python files of the systems
    Folder_Database : Folder with all modular models
    Folder_Merging_Funtions : Folder with all the merging algorithms
    Folder_Merging_Sequencing : Folder with all the Sequencing algorithms
    Folder_Merging_Create_x_file :Folder with all the Create_x_file algorithms

    TemporaryFolder : name of the folder for the algorithm. Can be a random name 
    (will be creat and deleted in the algorithm was important for the programming work)

    Output variables : output is useless in our algorithm. Can be changed
    CSVFinal : name of the CSV file of the merged system
    
    CODEs format : [{'MXXXX'},{'MXXXX'},{'MXXXX'},{'MXXXX'}]
    system name format : SystemName_a_ThisForm (without .csv) 
    """
    
    # Importing Modules
    import os
    from Merging2Models import Merging2Models
    from ReplaceTemporaryLineCode import ReplaceTemporaryLineCode
    from ReorderLines import ReorderLines

    # Creating TemporaryFolder
    TemporaryFolder = Folder_Merging_Funtions+"\\temp_"+System_Name
    os.mkdir(Folder_Main+TemporaryFolder)

    # Deleting TemporaryFolder
    os.rmdir(Folder_Main+TemporaryFolder)    

    # From SystemName to SXXXX_a_SystemName
    List = []
    for x in os.listdir(Folder_Main+Folder_Systems):
        if x.endswith(".csv"):
            # Listing all the already used numbers
            List.append(x)
    List2 = []
    for x in List:
        List2.append(int(x[1:5]))
    List2.append(int(4))
    print(List2)
    # Loop to find the empty number that is going to be used which is "i"
    for i in range(1, max(List2)):
        if i not in  List2: break
    print(i)
    # Add the zeros
    Number = f"{i:04}"
    SystemName_a_ThisForm = "S"+Number+"_a_"+System_Name
    print(SystemName_a_ThisForm)

    # CODEs
    N = len(CODEs)
    PYs = CODEs
    CSVs = CODEs
    MODELs = CODEs
    TEMPOs = CODEs





    CSVFinal = "Not yet done"
    return CSVFinal