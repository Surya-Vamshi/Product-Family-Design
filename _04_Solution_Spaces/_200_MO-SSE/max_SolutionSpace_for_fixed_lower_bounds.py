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
    import warnings
    import numpy as np
    from MonteCarlo import MonteCarlo
    from _07_Algorithms.Constraint import Constraint

    print("Testing of max_SolutionSpace_for_fixed_lower_bounds:")

    # Pre-processing

    # Save initial values of outputs when they are put in
    dvbox_initial = dvbox
    mu_initial = mu
    weight_initial = weight
    dv_norm_initial = dv_norm
    dv_norm_l_initial = dv_norm_l

    # Check which DVs can be independently expanded to higher values
    expandable_dv = np.zeros_like(dsl)
    ind_dv_in_par_vector = np.argwhere(np.isnan(parameters[0, :])).squeeze()
    parameters_initial = parameters

    # Expand upper bound of every DV and check if the constraints are met
    for i in range(0, dim):
        x = np.array(dvbox[1, :])
        x[i] = x[i] + (dsu[i] - dsl[i]) * 0.05

        const = Constraint(problem, reqU, reqL, parameters, dv_norm, dv_norm_l, qoi_norm, 1)
        if all(const.Constraint_fun(x) <= 0):
            expandable_dv[i] = 1
        else:
            # Make non expandable DVs to parameters
            parameters[:, ind_dv_in_par_vector[i]] = np.transpose(dvbox[:, i])*dv_norm[i] + dv_norm_l[i]

    # Checking if no DV is possible to expand to higher values
    if sum(expandable_dv) == 0:
        dvbox = dvbox_initial
        mu = mu_initial
        return [dvbox, mu]

    # Reduce dvbox, dsl, dsu, dv_norm and weight to just the expandable DVs
    dvbox = dvbox[:, expandable_dv == 1]
    dsl = dsl[expandable_dv == 1]
    dsu = dsu[expandable_dv == 1]
    dv_norm = dv_norm[expandable_dv == 1]
    dv_norm_l = dv_norm_l[expandable_dv == 1]
    weight = weight[expandable_dv == 1]
    weight = weight / sum(weight)

    dim = len(dsl)

    ind_parameters = np.argwhere(~np.isnan(parameters[0, :])).squeeze()

    """ Phase I for initial Point """
    dvbox_old = dvbox

    Iter_Phase_I = 0
    mu_vec = mu

    # At first expand dvbox isotroply in all directions
    anisotropic_expandation = 0
    tol_Phase_I = 5e-2

    while True:
        Iter_StepB = 0
        while True:
            Iter_StepB = Iter_StepB + 1

            # Step B
            if ~anisotropic_expandation:
                # Expand dvbox in upper sides of each interval isotroply
                dvbox_new = dvbox_old + g*(dsu - dsl)*[[0], [1]]
            else:
                # Expand dvbox in upper sides of each interval anisotroply
                dvbox_new = dvbox_old + g*(dvbox_old[1, :] - dvbox_old[0, :])*[[0], [1]]

            # Expend maximal to DS bounds
            dvbox_new[0, :] = np.maximum(dvbox_new[0, :], dsl)
            dvbox_new[1, :] = np.minimum(dvbox_new[1, :], dsu)

            # Monte Carlo Sampling
            [Points_A, m, Points_B, dv_sample] = MonteCarlo(problem, dvbox_new, parameters, reqL, reqU, dv_norm,
                                                            dv_norm_l, ind_parameters, N, dim)

            # 50% of the samples in the candidate box have to be good designs to
            # end the growing process. Otherwise, the growth rate must be set
            # smaller and the growing reruns. End also with maximal Iterations
            if m/N >= 0.5 or Iter_StepB >= 100:
                dvbox = dvbox_new

                # Step size control only for maximal Solution Space.
                # Otherwise, the points are necessary for pareto front.

                # Change step size to a bigger value if there were enough good
                # design points in the step
                g = 2*m/N*g
                break
            else:
                # Change step size to a smaller value if there were not enough
                # good design points in the step and repeat step
                g = 2 * m / N * g

                # If m is zero, then g is zero in every following step ==>
                # further expansion is not possible ==> g has to have at least
                # a small, nonzero and positive value
                if g <= 0:
                    g = 0.006

        if m != 0:
            Iter_Phase_I = Iter_Phase_I + 1

            # Step A
            """need to add StepA_modified_upper_bounds"""

            # Stop phase I if mu doesn't change significantly from step to step
            # or if the maximal iteration is reached
            if abs(0) < tol_Phase_I:
                """Need to edit this"""
                if anisotropic_expandation == 0:
                    # When isotropic expandation converges, expand anisotropic
                    # with lower tolerance
                    anisotropic_expandation = 1
                    tol_Phase_I = 1e-2
                else:
                    break
            elif Iter_Phase_I > 1000:
                warnings.warn("Warning! Phase I stopped due to reaching the maximal iteration counter! Solution may "
                              "not be the maximal Solution Space!")
                break
        else:
            dvbox = dvbox_initial
            mu = mu_initial
            return [dvbox, mu]
        dvbox_old = dvbox

    """Intermediate Phase  for initial Point"""
    # Monte Carlo Sampling

    return [dvbox, mu]

