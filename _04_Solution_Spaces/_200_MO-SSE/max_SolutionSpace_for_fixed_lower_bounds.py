def max_SolutionSpace_for_fixed_lower_bounds(problem, dvbox, parameters, mu, g, dsl, dsu, reqL, reqU, dv_norm,
                                             dv_norm_l, qoi_norm, weight, N, dim):
    """
    Description : This function calculates the maximal Solution Space for a given lower
    bounds. The initial dvbox has to be the point of the lower bounds.

    Input variables :
    problem: Object of the problem (x-file)
    dvbox: Intervals of the DVs
    parameters: Parameters of the optimization
    mu: Size of the solution space
    g: Exploration coefficient
    dsl: Lower bounds of the design spaces
    dsu: Upper bounds of the design spaces
    reqL: Lower bound requirements
    reqU: Upper bound requirements
    dv_norm: Norming factor for the DVs
    qoi_norm: Norming factor for the QOIs
    weight: Weights of the DVs
    N: Number of sample points
    dim: Number of DVs

    Output variables :
    dvbox: Intervals of the DVs
    mu: Size of the solution SPACE
    """
    # Importing Modules
    import numpy as np
    from _07_Algorithms.Constraint import Constraint


    # Pre-processing

    # Save initial values of outputs when they are put in
    dvbox_initial = dvbox
    mu_initial = mu
    weight_initial = weight
    dv_norm_initial = dv_norm
    dv_norm_l_initial = dv_norm_l

    # Check which DVs can be independently expanded to higher values
    expandable_dv = np.zeros_like(dsl)
    ind_dv_in_par_vector = np.argwhere(~np.isnan(parameters[0]))
    parameters_initial = parameters

    # Expand upper bound of every DV and check if the constraints are met
    for i in range(0, dim):
        x = dvbox[1, :]
        x[i] = x[i] + dsu[i] - dsl[i] * 0.05

        const = Constraint(problem, reqU, reqL, parameters, dv_norm, dv_norm_l, qoi_norm, 1)
        if all(const.Constraint_fun(x) <= 0):
            expandable_dv[i] = 1
        else:
            # Make non expandable DVs to parameters
            parameters[:, ind_dv_in_par_vector[i]] = np.transpose(dvbox[:, i])*dv_norm[i] + dv_norm_l[i]
            """Need to check if everything is correct"""

    return [dvbox, mu]

