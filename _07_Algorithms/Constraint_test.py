import importlib
import numpy as np
from pymoo.core.problem import ElementwiseProblem


class Constraint(ElementwiseProblem):
    def __init__(self, problem, reqU, reqL, parameters, dv_norm, dv_norm_l, qoi_norm, num_prod, varargin=None):
        # module = importlib.import_module("_03_Design_Problems." + problem)
        # self.problem = getattr(module, problem)
        self.problem = problem
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
        c = 0
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
                x_vec_temp = x_vec_temp.append(np.transpose(self.parameters[1:2:2 * self.num_prod, ind_parameters(i)]))
                x_vec_temp = x_vec_temp.append(x_vec[ind_parameters(i):, :])
                x_vec = x_vec_temp

        p = self.problem()
        y = p.SystemResponse(x)

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

        out["F"] = c
        out["G"] = []
        # return None
        # f1 = x[:, 0] ** 2 + x[:, 1] ** 2
        # f2 = (x[:, 0] - 1) ** 2 + x[:, 1] ** 2
        #
        # g1 = 2 * (x[:, 0] - 0.1) * (x[:, 0] - 0.9) / 0.18
        # g2 = - 20 * (x[:, 0] - 0.4) * (x[:, 0] - 0.6) / 4.8
        #
        # out["C"] = np.column_stack([f1, f2])

    def Constraint_fun(self, x):
        c = 0
        return c
