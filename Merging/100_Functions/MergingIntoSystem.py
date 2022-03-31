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
    import shutil
    import sys
    from Merging2Models import Merging2Models
    from ReplaceTemporaryLineCode import ReplaceTemporaryLineCode
    from ReorderLines import ReorderLines
    sys.path.append(str(Folder_Main+Folder_Merging_Create_x_file))
    from FromType1toType2 import FromType1toType2

    # Creating TemporaryFolder
    Folder_Temporary = Folder_Merging_Funtions+"\\temp_"+System_Name
    os.mkdir(Folder_Main+Folder_Temporary)   

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

    # Loop to find the empty number that is going to be used which is "i"
    for i in range(1, max(List2)):
        if i not in  List2: break
    
    # Add the zeros
    Number = f"{i:04}"
    SystemName_a_ThisForm = "S"+Number+"_a_"+System_Name
    
    # CODEs
    N = len(CODEs)
    PYs = []
    CSVs = []
    MODELs = []
    TEMPOs = []

    file = os.listdir(Folder_Main+Folder_Database)
    for i in range(0,N):
        for name in file:
            if name.startswith(CODEs[i]) and name.endswith(".py"):
                PYs.append(name)        
            if name.startswith(CODEs[i]) and name.endswith(".csv"):
                CSVs.append(name)
                MODELs.append(name[:-4])
        TEMPOs.append("TXXX_a_Temporary"+str(i+1))
        shutil.copyfile(Folder_Main+Folder_Database+"\\"+PYs[i],Folder_Main+Folder_Temporary+"\\"+PYs[i])
        shutil.copyfile(Folder_Main+Folder_Database+"\\"+CSVs[i],Folder_Main+Folder_Temporary+"\\"+CSVs[i])
    
    # Explanation in DSM Paper or Nicky's master thesis
    Merging2Models(MODELs[0],MODELs[1],TEMPOs[0],Folder_Main,Folder_Temporary,Folder_Merging_Funtions,
                            Folder_Merging_Sequencing,Folder_Merging_Create_x_file)
    if N>2:
        for i in range(2,N):
            if i==N-1:
                TEMPOs[N-1] = SystemName_a_ThisForm
            [InputVariables,IntermediateVariables,OutputVariables] = Merging2Models(TEMPOs[i-2],MODELs[i],TEMPOs[i-1],Folder_Main,
            Folder_Temporary,Folder_Merging_Funtions,Folder_Merging_Sequencing,Folder_Merging_Create_x_file)
            ReplaceTemporaryLineCode(TEMPOs[i-2],MODELs[i],TEMPOs[i-1],Folder_Main,
            Folder_Temporary,Folder_Merging_Funtions,Folder_Merging_Sequencing,Folder_Merging_Create_x_file)

    # Here Reorder
    ReorderLines(SystemName_a_ThisForm,InputVariables,IntermediateVariables,OutputVariables,Folder_Main,
    Folder_Temporary,Folder_Merging_Funtions,Folder_Merging_Sequencing,Folder_Merging_Create_x_file)

    # Remane with _f_
    CSVFinal = SystemName_a_ThisForm+".csv"
    PYFinal = FromType1toType2(CSVFinal,".csv",".m","f")

    # Copying Final files to Systems
    #shutil.copyfile(Folder_Main+Folder_Temporary+"\\"+PYFinal,Folder_Main+Folder_Systems+"\\"+PYFinal)
    #shutil.copyfile(Folder_Main+Folder_Temporary+"\\"+CSVFinal,Folder_Main+Folder_Systems+"\\"+CSVFinal)

    # Deleting TemporaryFolder
    shutil.rmtree(Folder_Main+Folder_Temporary)


    # Final Output
    
    return CSVFinal