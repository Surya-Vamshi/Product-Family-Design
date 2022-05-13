"""
M0001_f_Transmission.m

Description:
  This function calculates the output torque and rotational speed of a gearbox.

Input:
  T_in = Incoming torque [Nm]
  n_in = Incoming rotational speed of the shaft [rad/s]
  i = Transmision ratio [-]

Intermediate:

Output:
  T_out = Output tourque [Nm]
  n_out = Output rotational speed [rad/s]

Example:
  [T_out,n_out] = M0001_f_Transmission ([5000,15000],[250,100],[7,5])

Formula:
  $T_{out} = T_{in} \cdot i$  
  $n_{out} = \frac{n_{in}}{i}$

"""
#  Code:
import numpy as np


def M0001_f_Transmission(T_in, n_in, i):
    T_out = np.multiply(i, T_in).tolist()
    n_out = np.multiply(n_in, i).tolist()
    return [T_out, n_out]
