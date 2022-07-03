import numpy as np
from pymoo.core.problem import Problem

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

class Constraint(Problem):
    def __init__(self, problem, reqU, reqL, parameters, dv_norm, dv_norm_l, qoi_norm, num_prod, varargin=None):
        self.problem = problem
        self.reqU = reqU
        self.reqL = reqL
        self.parameters = parameters
        self.dv_norm = dv_norm
        self.dv_norm_l = dv_norm_l
        self.qoi_norm = qoi_norm
        self.num_prod = num_prod
        if varargin == None:
            self.varargin = []
        else:
            self.varargin = varargin
        size = len(dv_norm)
        super().__init__(n_var=size,
                         n_obj=size,
                         n_constr=size,
                         xl=dv_norm_l,
                         xu=dv_norm)

    def _evaluate(self, x, out, *args, **kwargs):
        return None
        # f1 = x[:, 0] ** 2 + x[:, 1] ** 2
        # f2 = (x[:, 0] - 1) ** 2 + x[:, 1] ** 2
        #
        # g1 = 2 * (x[:, 0] - 0.1) * (x[:, 0] - 0.9) / 0.18
        # g2 = - 20 * (x[:, 0] - 0.4) * (x[:, 0] - 0.6) / 4.8
        #
        # out["C"] = np.column_stack([f1, f2])

def Constraint_fun(problem,x,reqU,reqL,parameters,dv_norm,dv_norm_l,qoi_norm,num_prod,varargin):

    ind_parameters = np.argwhere(~np.isnan(parameters[0]))

    if not varargin:
        N_pop = varargin[0]
        if np.size(x, 1) != N_pop:
            N_pop = np.size(x, 1)
    else:
        N_pop = 1

    x_vec = x*dv_norm + dv_norm_l

    if num_prod == 1: # For PSO with vectorization
        for i in range(0,np.size(ind_parameters,0)):
            x_vec = [x_vec[0:ind_parameters[i]-1,:]]

    c = []
    return c