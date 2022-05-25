"""
S0001_f_Simple_Transmission.py

Description:

Input:
	z_22 = Numer of teeth driven gear [-]
	z_21 = Numer of teeth driving gear [-]
	z_11 = Numer of teeth driving gear [-]
	z_12 = Numer of teeth driven gear [-]
	n_in = Incoming rotational speed of the shaft [rad/s]
	T_in = Incoming torque [Nm]

Intermediate:
	i_2 = Transmission ratio stage 2 [-]
	i_1 = Transmission ratio stage 1 [-]
	i = Transmision ratio [-]

Output:
	T_out = Output tourque [Nm]
	n_out = Output rotational speed [rad/s]

Example:

Formula:

"""
#  Code:

import numpy as np


def S0001_f_Simple_Transmission(z_22, z_21, z_11, z_12, n_in, T_in):
	from _01_Database.M0002_f_Two_stage_gear import M0002_f_Two_stage_gear
	from _01_Database.M0001_f_Transmission import M0001_f_Transmission
	from _01_Database.M0003_f_Spur_gear import M0003_f_Spur_gear
	from _01_Database.M0004_f_Worm_gear import M0004_f_Worm_gear
	# Code
	[i_1] = M0003_f_Spur_gear(z_11, z_12)
	[i_2] = M0004_f_Worm_gear(z_21, z_22)
	[i] = M0002_f_Two_stage_gear(i_1, i_2)
	[T_out, n_out] = M0001_f_Transmission(T_in, n_in, i)
	return [T_out, n_out]
#
# # import numpy as np
# x = [[10], [10], [10], [10], [100], [500]]
# y = [[], []]
# [y[0], y[1]] = S0001_f_Simple_Transmission(x[0], x[1], x[2], x[3], x[4], x[5])
# print(y)