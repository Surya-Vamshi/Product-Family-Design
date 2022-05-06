"""
M0004_f_Worm_gear.m

Description:
  This function calculates the gear ratio of a worm gear pair depending on
  the number of teeth of the two gears.

Input:
  z_21 = Numer of teeth driving gear [-]
  z_22 = Numer of teeth driven gear [-]

Intermediate:

Output:
  i_2 = Transmission ratio stage 2 [-]

Example:
  [i_2] = M0004_f_Worm_gear ([2,4],[50,80])

Formula:
  $i_2 = \frac{z_{22}}{z_{21}}$
  
"""
#  Code:
import numpy as np


def M0004_f_Worm_gear(z_21, z_22):
    i_2 = np.multiply(z_22, z_21)
    return i_2
