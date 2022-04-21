def Merging2Models(Model1, Model2, MergedModel, Folder_Main, Folder_Temporary, Folder_Merging_Funtions,
                   Folder_Merging_Sequencing, Folder_Merging_Create_x_file):
    """
    Description : Merging 2 models (CSV+Python file but without ordering system)
    (this algorithm is just regrouping sub algorithms which make the big part of the work)

    Input variables:
    Model1 : name of CSV file of the first model without '.csv'
    Model2 : name of CSV file of the second model without '.csv'
    MergedModel : Name of the new merged csv file without '.csv'
    Folder_Main : Main Folder containing all the code files
    Folder_Database : Folder with all modular models
    Folder_Merging_Funtions : Folder with all the merging algorithms
    Folder_Merging_Sequencing : Folder with all the Sequencing algorithms
    Folder_Merging_Create_x_file :Folder with all the Create_x_file algorithms

    Output variables:
    InputVariables : list of the input varialbes of the new merged model
    IntermediateVariables : list of the intermediate varialbes of the new merged model
    OutputVariables : list of the output varialbes of the new merged model
    """
    # Importing Modules
    from Functions.Sequencing.Merging2CSV import Merging2CSV
    from Functions.Sequencing.CSVSequencing import CSVSequencing
    from Functions.Create_x_file.Merging2Matlab import Merging2Matlab

    CSV1 = Model1 + ".csv"
    CSV2 = Model2 + ".csv"
    # Reorder CSV inputs in case it's not ordered
    # CSVSequencing(CSV1,"",Folder_Temporary, Folder_Merging_Funtions,
    #               Folder_Merging_Sequencing, Folder_Merging_Create_x_file)
    # CSVSequencing(CSV2,"",Folder_Temporary, Folder_Merging_Funtions,
    #               Folder_Merging_Sequencing, Folder_Merging_Create_x_file)

    # Merging 2 CSV in a 3rd one with name of it. Nothing more
    CSV3 = Merging2CSV(CSV1, CSV2, MergedModel, Folder_Main, Folder_Temporary, Folder_Merging_Funtions,
                       Folder_Merging_Sequencing, Folder_Merging_Create_x_file)

    # Merging 2 matlab files in 3rd one. You need the CSV of final model
    Model3 = CSV3[:-4]
    [InputVariables, IntermediateVariables, OutputVariables] = Merging2Matlab(Model1, Model2, Model3, Folder_Main,
                                                                              Folder_Merging_Funtions,
                                                                              Folder_Merging_Sequencing,
                                                                              Folder_Merging_Create_x_file)

    return InputVariables, IntermediateVariables, OutputVariables
