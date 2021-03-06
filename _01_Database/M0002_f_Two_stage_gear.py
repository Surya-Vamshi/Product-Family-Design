"""
M0002_f_Two_stage_gear.m

Description:
  This function calculates the total transmission ratio of a gearbox with
  two gear stages.

Input:
  i_1 = Transmission ratio stage 1 [-]
  i_2 = Transmission ratio stage 2 [-]

Intermediate:

Output:
  i = Total transmission ratio [-]

Example:
  [i] = M0002_f_Two_stage_gear ([5,7],[20,15])

Formula:
  $i = i_1 \cdot i_2$
  
"""
#  Code:
import numpy as np


def M0002_f_Two_stage_gear(i_1, i_2):
    i = np.multiply(i_1, i_2).tolist()
    return [i]
