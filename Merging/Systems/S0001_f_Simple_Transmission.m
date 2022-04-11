%% S0001_f_Simple_Transmission.m


%% Discription:

% Input:
% z_11 = Numer of teeth driving gear [-]
% z_12 = Numer of teeth driven gear [-]
% z_21 = Numer of teeth driving gear [-]
% z_22 = Numer of teeth driven gear [-]
% n_in = Incoming rotational speed of the shaft [rad/s]
% T_in = Incoming torque [Nm]

% Intermediate:
% i_1 = Transmision ratio stage 1 [-]
% i_2 = Transmision ratio stage 2 [-]
% i = Transmision ratio [-]

% Output:
% T_out = Output tourque [Nm]
% n_out = Output rotational speed [rad/s]

% Example:


%% Formula:


%% Code:
function [T_out,n_out] = S0001_f_Simple_Transmission (z_11,z_12,z_21,z_22,n_in,T_in)
	[i_1] = M0003_f_Spur_gear (z_11,z_12);
	[i_2] = M0004_f_Worm_gear (z_21,z_22);
	[i] = M0002_f_Two_stage_gear (i_1,i_2);
	[T_out,n_out] = M0001_f_Transmission (T_in,n_in,i);
end