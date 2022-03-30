"""
M0003_f_Spur_gear.m

Discription:
  This function calculates the gear ratio of a spur gear pair depending on
  the number of teeth of the two gears.

Input:
  z_11 = Numer of teeth driving gear [-]
  z_12 = Numer of teeth driven gear [-]


Intermediate:

Output:
  i1 = Transmision ratio stage 1 [-]

Example:
  [i_1] = M0003_f_Spur_gear ([5,10],[100,90])

Formula:
  $i_1 = \frac{z_{12}}{z_{11}}$
  
"""
#  Code:
import numpy as np
def  M0003_f_Spur_gear(z_11,z_12):
    i_1 = np.multiply(z_12,z_11) 
    return i_1
