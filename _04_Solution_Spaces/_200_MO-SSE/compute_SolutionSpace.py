def compute_SolutionSpace(problem, weight, dsl, dsu, l, u, reqU, reqL, parameters, slider_value):
    """
    Description : This function computes the maximal box shaped solution space of an
    n-dimensional problem by using a slightly modified algorythm as presented
    in Zimmermann and von Hoessle (2013, p297-300).

    Input variables :
    problem: Object of the problem (x-file)
    weight: Weights of the DVs
    dsl: Lower bounds of the design spaces
    dsu: Upper bounds of the design spaces
    l: Lower bounds of the DVs
    u: Upper bounds of the DVs
    reqL: Lower bound requirements
    reqU: Upper bound requirements
    parameters: Parameters of the optimization
    slider_value: Slider value for MO-SSE

    Output variables :
    dv_par_box: Intervals of DVs and parameters
    exitflag: Flag why the optimization terminated
    time: Time for the execution of the optimization
    """
    # Importing Modules
    from pathlib import Path
    import time
    import numpy as np

    # Converting list to numpy array
    dsl = np.array(dsl)
    dsu = np.array(dsu)
    l = np.array(l)
    u = np.array(u)
    reqU = np.array(reqU)
    reqL = np.array(reqL)
    weight = np.array(weight)



    # Pre-processing
    dim = sum(np.isnan(parameters[0]))  # Dimension of the problem (number of DVs)
    ind_parameters = np.argwhere(~np.isnan(parameters[0]))
    time_start = time.time()

    # Norming factor for DVs
    dv_norm = dsu - dsl
    dv_norm_l = dsl

    # # Norming factor for QOIs
    # qoi_norm = [reqU; reqL]
    # qoi_norm(qoi_norm == inf) = realmax
    # qoi_norm(qoi_norm == -inf) = realmax
    # qoi_norm(qoi_norm == 0) = 1
    #
    # # Norming boundaries
    # l = (l-dv_norm_l)/dv_norm
    # u = (u-dv_norm_l)/dv_norm
    # dsl = (dsl-dv_norm_l)/dv_norm
    # dsu = (dsu-dv_norm_l)/dv_norm

    [dv_par_box, exitflag] = [0, 0]
    time_taken = time.time() - time_start

    return [dv_par_box, exitflag, time_taken]

import numpy as np
NaN = np.nan
problem_call = 0  # S0002_x_Simple_Transmission Class as variable
weight_call = [1.667, 1.667, 1.667, 1.667, 1.667, 1.667]
dsl_call = [0, 0, 0, 0, 0, 0]
dsu_call = [100, 100, 100, 100, 100, 100]
l_call = [0, 0, 0, 0, 0, 0]
u_call = [100, 100, 100, 100, 100, 100]
reqU_call = [200, 200]
reqL_call = [0, 0]
parameters_call = [[NaN, NaN, NaN, NaN, NaN, NaN],
                   [NaN, NaN, NaN, NaN, NaN, NaN]]
slider_value_call = 0.5
[dv_par_box, exitflag, time_taken] = compute_SolutionSpace(problem_call, weight_call, dsl_call, dsu_call, l_call,
                                                           u_call, reqU_call, reqL_call, parameters_call,
                                                           slider_value_call)
print("dv_par_box = " + str(dv_par_box))
print("exitflag = " + str(exitflag))
print("time_taken = " + str(time_taken))
# Actual Result:
# dv_par_box = [[10.5977, 51.0075]
#               [13.9578, 59.1029]
#               [14.2141, 67.1239]
#               [14.3715, 53.8028]
#               [0.8116, 44.4914]
#               [0.7908, 40.1652]]
# exitflag = 1
# time_taken = 47.3578