def StepA_modified_upper_bounds(dvbox, dv_sample, Points_A, Points_B, dim, weight):
    """
    Description : This function performs a modified Step A from Zimmermann and von
    Hoessle (2013, p297-300). In the modified version, just the upper bounds
    are manipulated to exclude bad designs from the solution box. Thus, it is
    possible to calculate the maximal Solution Space for given (fixed) lower bounds.

    Input variables :
    :param dvbox: Intervals of the DVs
    :param dv_sample: Sampled DVs
    :param Points_A: Good points in the sample
    :param Points_B: Bad points in the sample
    :param dim: Number of DVs
    :param weight: Weights of the DVs

    Output variables :
    :return:
    dvbox: Intervals of the DVs after all bad points are removed
    mu: Size of the solution space
    """

    # Importing Modules
    import numpy as np

    N_i = np.zeros(1, dim)

    dvbox_A = dvbox * np.ones((1, 1, sum(Points_A)))
    mu_A = np.zeros(sum(Points_A), 1)

    ind_B = np.nonzero(Points_B)

    for A in range(0, sum(Points_A)):
        for B in range(0, sum(Points_B)):
            for i in range(0, dim):
                N_i[i] = sum(dv_sample[i, Points_A] > dv_sample[i, ind_B[B]])

            arr = weight * N_i
            j = np.where(arr == np.amin(arr))

            dvbox_A[j, 1, A] = np.minimum(dvbox_A[j, 1, A], dv_sample[j, ind_B[B]] - np.finfo(float))

        arr = np.transpose(weight) * (dvbox_A[:, 1, A] - dvbox_A[:, 0, A])
        mu_A[A] = arr.prod()

    mu = np.amax(mu_A)
    ind_mu_A_max = np.where(mu_A == np.amax(mu_A))
    dvbox = dvbox_A[:, :, ind_mu_A_max]

    return [dvbox, mu]
