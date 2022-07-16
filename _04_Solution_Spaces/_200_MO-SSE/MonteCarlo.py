def MonteCarlo(problem, dvbox, parameters, reqL, reqU, dv_norm, dv_norm_l, ind_parameters, N, dim):
    """
    Description : This function performs a Monte Carlo Sampling in a given DV box. The
    System Response is evaluated and good as well as bad designs are
    determined via the boundary conditions of the QOIs.

    Input variables :
    :param problem: Object of the problem (x-file)
    :param dvbox: Intervals of the DVs
    :param parameters: Parameters of the optimization
    :param reqL: Lower bound requirements
    :param reqU: Upper bound requirements
    :param dv_norm: Norming factor for the DVs
    :param dv_norm_l: Normed values of DVs
    :param ind_parameters: Index which input is a parameter
    :param N: Number of sample points
    :param dim: Number of DVs

    Output variables :
    :return:
    Points_A_sorted: Points A sorted by their performance value in descending order
    m: Number of points A
    Points_B_sorted: Points B sorted by their performance value in descending order
    dv_sample_sorted: Sampled DVs sorted by their performance value in descending order
    """

    # Importing Modules
    import numpy as np

    p = problem()
    # Create sample points
    dv_sample = (dvbox[1, :] - dvbox[0, :]) * np.random.rand(N, dim) + dvbox[0, :]

    par_sample = (parameters[1, :] - parameters[0, :]) * np.random.rand(N, p.d) + parameters[0, :]

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

    y_sample = np.transpose(p.SystemResponse(np.transpose(x_sample)))  # Evaluate sample points

    # The commented code below needs to written in python format if it is needs to be used
    # Points_A = all(y_sample >= reqL & y_sample <= reqU, 1)  # Indicates the good designs of candidate box
    # m = sum(Points_A)                                       # Quantity of good points
    # Points_B = ~Points_A                                    # Indicates the bad designs of candidate box

    # Calculate if a sample fulfills the requirements
    c = np.append(y_sample - reqU, reqL - y_sample, axis=1)
    c_max = np.max(c, axis=1)

    # Sort samples in descending order
    ind_sort = np.flip(np.argsort(c_max))
    c_max_sorted = c_max[ind_sort]
    dv_sample_sorted = dv_sample[ind_sort]

    Points_A_sorted = np.array([c_max_sorted <= 0])  # c_max_sorted <= 0  # Indicates the good designs of candidate box
    m = sum(sum(Points_A_sorted))  # Quantity of good points
    Points_B_sorted = np.array(np.invert(Points_A_sorted))  # Indicates the bad designs of candidate box

    return [Points_A_sorted, m, Points_B_sorted, dv_sample_sorted]
