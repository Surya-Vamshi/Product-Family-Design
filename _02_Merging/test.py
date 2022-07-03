PyVar1 = ['i_1','i_2','i','n_in','T_in','T_out','n_out']
PyVar2 = ['z_11','i_2','i_1']
PyType2 = ['-', '-', '-']
PyColor2 = ['black', 'black', 'black']
Mat2 = [['0', '0', '1'], ['0', '0', '1'], ['0', '0', '0']]
import numpy as np

from Functions.Sequencing.P1toP2Tables import P1toP2Tables
from Functions.Sequencing.P1toP2Matrix import P1toP2Matrix

Mat2 = np.array(Mat2)
N1 = len(PyVar1)
N2 = len(PyVar2)
Step2 = 0
for i in range(N1 - 1, -1, -1):
    Letter1 = PyVar1[i]
    for j in range(N2 - Step2 - 1, -1, -1):
        Letter2 = PyVar2[j]
        if j == (N2 - Step2):
            if Letter1 == Letter2:
                Step2 = Step2 + 1
        else:
            if Letter1 == Letter2:
                PyVar2, PyType2, PyColor2 = P1toP2Tables(PyVar2, PyType2, PyColor2, j, N2 - Step2 - 1)
                Mat2 = P1toP2Matrix(Mat2, j, N2 - Step2 - 1)
                Step2 = Step2 + 1

print(PyVar2)
print(PyType2)
print(PyColor2)
print(Mat2)

