def WritingList2CSV(MatVar, MatType, MatColor, Matrix, Path):
    """
    Descirption : To Save new dependency graph in CSV File

    Input variables :
    MatVar : 1: table with variable name
    MatType : 1: table with variable type
    MatColor : 1: table with variable color
    Matrix : Matrix of the DSM
    Path : Path of the CSV file to be saved in

    Output variables :
    Path : Path of the CSV file saved
    """
    # Importing Modules
    import numpy as np
    import csv

    # open the file in the write mode
    f = open(Path, 'w', newline="")

    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(MatVar)
    writer.writerow(MatType)
    writer.writerow(MatColor)

    Matrix = Matrix.tolist()
    writer.writerows(Matrix)

    # close the file
    f.close()

    return Path
