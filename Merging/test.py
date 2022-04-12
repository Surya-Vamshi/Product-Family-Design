PyVar1 = ['T_in', 'n_in', 'i', 'n_out', 'T_out']
PyVar2 = ['i_1', 'i_2', 'i']
PyType2 = ['-', '-', '-']
PyColor2 = ['black', 'black', 'black']
Mat2 = [['0', '0', '1'], ['0', '0', '1'], ['0', '0', '0']]

from Functions.Sequencing.P1toP2Tables import P1toP2Tables
from Functions.Sequencing.P1toP2Matrix import P1toP2Matrix

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
