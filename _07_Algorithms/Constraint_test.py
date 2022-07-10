import numpy as np
from pymoo.core.problem import ElementwiseProblem

"""
    Description : Constraint function for optimization of initial point for Solution Space
    Optimization

    Input variables :
    problem: Object of the problem (x-file)
    x: DVs
    reqL: Lower bound requirements
    reqU: Upper bound requirements
    parameters: Parameters of the optimization
    dv_norm: Norming factor of the DVs
    qoi_norm: Norming factor of the QOIs
    num_prod: Number of products
    varargin: Calculating with whole population or not

    Output variables :
    c: Inequality constraints
    ceq: Equality constraints
"""

class Constraint_test(ElementwiseProblem):
    def __init__(self, problem, reqU, reqL, parameters, dv_norm, dv_norm_l, qoi_norm, num_prod, varargin=None):
        self.problem = problem
        self.p = self.problem()
        self.reqU = reqU
        self.reqL = reqL
        self.parameters = parameters
        self.dv_norm = dv_norm
        self.dv_norm_l = dv_norm_l
        self.qoi_norm = qoi_norm
        self.num_prod = num_prod

        for i in range(0, len(self.reqL)):
            if self.reqU[i] == "inf":
                self.reqU[i] = np.iinfo(self.reqU[i].dtype).max
            if self.reqL[i] == "-inf":
                self.reqL[i] = - np.iinfo(self.reqL[i].dtype).max

        if varargin == None:
            self.varargin = []
        else:
            self.varargin = varargin
        super().__init__(n_var=len(dv_norm),
                         n_obj=len(reqU),
                         n_constr=1,
                         xl=dv_norm_l,
                         xu=dv_norm)

    def _evaluate(self, x, out, *args, **kwargs):
        # out["F"] = np.sum(self.p.SystemResponse(x))
        # out["F"] = []
        out["F"] = [0]
        out["G"] = self.Constraint_fun(x)

    def Constraint_fun(self, x):

        ind_parameters = np.argwhere(~np.isnan(self.parameters[0]))

        if self.varargin:
            N_pop = self.varargin[0]
            if np.size(x, 1) != N_pop:
                N_pop = np.size(x, 1)
        else:
            N_pop = 1

        x_vec = x * self.dv_norm + self.dv_norm_l

        if self.num_prod == 1:  # For PSO with vectorization
            for i in range(0, np.size(ind_parameters, 0)):
                x_vec_temp = x_vec[0:ind_parameters[i] - 1, :]
                x_vec_temp = x_vec_temp.append(np.tile(self.parameters[0, ind_parameters[i]], (1, N_pop)))
                x_vec_temp = x_vec_temp.append(x_vec[ind_parameters(i):, :])
                x_vec = x_vec_temp
        else:
            for i in range(0, np.size(ind_parameters, 0)):
                x_vec_temp = x_vec[0:ind_parameters[i] - 1, :]
                x_vec_temp = x_vec_temp.append(np.transpose(self.parameters[1:2:2*self.num_prod, ind_parameters(i)]))
                x_vec_temp = x_vec_temp.append(x_vec[ind_parameters(i):, :])
                x_vec = x_vec_temp

        y = self.p.SystemResponse(x_vec)

        for i in range(0, len(y)):
            if y[i] == "inf":
                y[i] = np.iinfo(y[i].dtype).max
            if y[i] == "-inf":
                y[i] = - np.iinfo(y[i].dtype).max

        # Shape into vector form if there are multiple products
        # Elsewise keep matrix form for the population
        if self.num_prod != 1:
            c = np.append(y - self.reqU, self.reqL - y)
            c = np.divide(c, self.qoi_norm)
        else:
            c = np.append(y - self.reqU, self.reqL - y)
            c = np.divide(c, self.qoi_norm)
            # Need to add splitapply but I am not sure what it doesll
        return c
