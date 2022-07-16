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

    N_i = np.zeros(dim)

    dvbox_A = np.repeat(dvbox[:, :, np.newaxis], sum(sum(Points_A)), axis=2)
    mu_A = np.zeros((sum(sum(Points_A)), 1))

    ind_B = np.where(Points_B == True)[1]

    for A in range(0, sum(sum(Points_A))):
        for B in range(0, sum(sum(Points_B))):
            for i in range(0, dim):
                N_i[i] = sum(dv_sample[Points_A.astype(bool)[0, :], i] > dv_sample[ind_B[B], i])

            arr = weight * N_i
            j = np.where(arr == np.amin(arr))

            dvbox_A[1, j, A] = np.minimum(dvbox_A[1, j, A], dv_sample[ind_B[B], j] - np.finfo(float).eps)

        arr = np.transpose(weight) * (dvbox_A[1, :, A] - dvbox_A[0, :, A])
        mu_A[A] = arr.prod()

    mu = np.amax(mu_A)
    ind_mu_A_max = np.where(mu_A == mu)[0][0]
    dvbox = dvbox_A[:, :, ind_mu_A_max]

    return [dvbox, mu]
