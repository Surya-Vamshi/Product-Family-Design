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
    import importlib
    import time
    import numpy as np
    from _07_Algorithms.Constraint import Constraint

    module = importlib.import_module("_03_Design_Problems." + problem)
    problem = getattr(module, problem)
    p = problem()

    # Converting list to numpy array
    dsl = np.array(dsl)
    dsu = np.array(dsu)
    l = np.array(l)
    u = np.array(u)
    reqU = np.array(reqU)
    reqL = np.array(reqL)
    weight = np.array(weight)
    parameters = np.array(parameters)

    # Pre-processing
    dim = sum(np.isnan(parameters[0]))  # Dimension of the problem (number of DVs)
    ind_parameters = np.argwhere(~np.isnan(parameters[0]))
    time_start = time.time()

    # Norming factor for DVs
    dv_norm = dsu - dsl
    dv_norm_l = dsl

    # Norming factor for QOIs
    qoi_norm = np.append(reqU, reqL)
    for i in range(0, len(qoi_norm)):
        if qoi_norm[i] == "inf":  # might change based on inf value
            qoi_norm[i] = np.iinfo(reqL.dtype).max
        if qoi_norm[i] == "-inf":
            qoi_norm[i] = - np.iinfo(reqL.dtype).max
        if qoi_norm[i] == 0:
            qoi_norm[i] = 1

    # Norming boundaries
    l = (l - dv_norm_l) / dv_norm
    u = (u - dv_norm_l) / dv_norm
    dsl = (dsl - dv_norm_l) / dv_norm
    dsu = (dsu - dv_norm_l) / dv_norm

    """Set first candidate box"""
    # Find best starting point x_init by sampling through the DS
    # Monte Carlo Sampling
    dv_sample = (u - l) * np.random.rand(1000, dim) + l

    par_sample = np.transpose((parameters[1, :] - parameters[0, :]) * np.random.rand(1000, p.d) + parameters[0, :])

    # Evaluate System Response
    x_sample = dv_sample * dv_norm + dv_norm_l
    for i in range(0, len(ind_parameters)):  # Need to check for error
        if ind_parameters[i] > len(x_sample[0, :]):
            x_sample = np.append(x_sample[:, 0:ind_parameters(i) - 1], par_sample[:, ind_parameters[i]])
        elif ind_parameters[i] == 1:
            x_sample = np.append(par_sample[:, ind_parameters(i)], x_sample[:, ind_parameters[i]:])
        else:
            x_sample = np.append(x_sample[:, 0:ind_parameters(i) - 1], par_sample[:, ind_parameters[i]],
                                 x_sample[:, ind_parameters[i]:])

    y_sample = np.transpose(p.SystemResponse(np.transpose(x_sample)))
    c = np.append(y_sample - reqU, reqL - y_sample, axis=1) / qoi_norm

    feasible = np.all(c <= 0, axis=1)

    # Get best point of initial sampling to start search for initial good point
    max_c = np.amax(c, axis=1)
    ind_c_min = np.argmax(max_c)
    x_init = dv_sample[ind_c_min, :]

    """
    Need to add code from matlab file from line 76 to 91
    """
    if not any(feasible):
        x0 = x_init
        print("Need to add this line of code")
    else:
        x0 = x_init
    print("x0 : ")
    print(x0)

    # Finding a good point to start with (This is not there in the main MATLAB Code)
    const = Constraint(problem, reqU, reqL, parameters, dv_norm, dv_norm_l, qoi_norm, 1)
    from pymoo.algorithms.moo.nsga2 import NSGA2
    from pymoo.optimize import minimize

    algorithm = NSGA2(pop_size=20)

    res = minimize(const, algorithm, ('n_gen', 20), seed=1, verbose=False)

    x_nsga = x0 * dv_norm + dv_norm_l

    # calculate a hash to show that all executions end with the same result
    dist_2 = np.sum((res.X - x_nsga) ** 2, axis=1)
    index = dist_2.argmin()
    x_final = res.X[index]
    x_final = (x_final - dv_norm_l) / dv_norm
    x0 = x_final

    print("x0 : ")
    print(x0)

    # If there is no feasible design exit function
    if any(const.Constraint_fun(x0) > 0):
        dv_par_box = 0
        exitflag = 0
        time_taken = time.time() - time_start
        print("Inside if condition")
        return [dv_par_box, exitflag, time_taken]
    else:
        print("Inside else condition")
        exitflag = 1

    # If MO-SSE calculate starting point for further optimization using pso
    if slider_value != 1:
        N_pop = 3*dim
        from pymoo.algorithms.soo.nonconvex.pso import PSO
        algorithm = PSO()

        res = minimize(const, algorithm, seed=1, verbose=False)

        print(res.X)

        # [initPop] = set_up_initPop(problem, parameters, N_pop, dim, 1,dsl, dsu,...
        #     reqL.*1.01, reqU.*0.99, dv_norm, dv_norm_l, dv_sample, feasible)
        #
        # prob.fitnessfcn = @(x) sum((weight'.*(x'-dsl)).^2,1)'
        # prob.nonlcon = @(x) Constraint(problem, x', reqU.*0.99, reqL.*1.01,...
        #     parameters, dv_norm, dv_norm_l, qoi_norm, 1, N_pop)
        # prob.nvars = length(dsl)
        # prob.Aeq = []
        # prob.beq = []
        # prob.Aineq = []
        # prob.bineq = []
        # prob.LB = dsl
        # prob.UB = dsu
        # prob.options.PopulationSize = N_pop
        # prob.options.StallGenLimit = 100
        # prob.options.TolFun = 1e-6
        # prob.options.TolCon = 1e-6
        # prob.options.InitialPopulation = initPop
        # prob.options.Vectorized = 'on'
        # prob.options.Display = 'off'
        #
        # x0 = pso(prob)
        # x0 = x0'

    # End
    [dv_par_box, exitflag] = [0, 0]
    time_taken = time.time() - time_start

    return [dv_par_box, exitflag, time_taken]


import numpy as np

NaN = np.nan
problem_call = "S0002_x_Simple_Transmission"  # S0002_x_Simple_Transmission Class as variable
weight_call = [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667]
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
# print("dv_par_box = " + str(dv_par_box))
# print("exitflag = " + str(exitflag))
# print("time_taken = " + str(time_taken))
# Actual Result:
# dv_par_box = [[10.5977, 51.0075]
#               [13.9578, 59.1029]
#               [14.2141, 67.1239]
#               [14.3715, 53.8028]
#               [0.8116, 44.4914]
#               [0.7908, 40.1652]]
# exitflag = 1
# time_taken = 47.3578
