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

    # Pre-processing
    dim = sum(np.isnan(parameters[0, :]))  # Dimension of the problem (number of DVs)
    ind_parameters = np.argwhere(~np.isnan(parameters[0, :]))
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

# import numpy as np
#
# # Pre-processing
# a = np.empty((2, 6))
# a[:] = np.nan
# dim = np.argwhere(~np.isnan(a[0, :]))
# print(dim)