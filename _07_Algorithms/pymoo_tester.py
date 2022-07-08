import numpy as np
import importlib
from Constraint import Constraint

problem = "S0002_x_Simple_Transmission"

NaN = np.nan
weight_call = np.array([0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667])
dsl_call = np.array([0, 0, 0, 0, 0, 0])
dsu_call = np.array([100, 100, 100, 100, 100, 100])
l_call = np.array([0, 0, 0, 0, 0, 0])
u_call = np.array([100, 100, 100, 100, 100, 100])
reqU_call = np.array([200, 200])
reqL_call = np.array([0, 0])
parameters_call = np.array([[NaN, NaN, NaN, NaN, NaN, NaN],
                   [NaN, NaN, NaN, NaN, NaN, NaN]])
slider_value_call = 0.5
dv_norm = dsu_call - dsl_call
dv_norm_l = dsl_call
qoi_norm = np.append(reqU_call, reqL_call)
for i in range(0, len(qoi_norm)):
    if qoi_norm[i] == 0:
        qoi_norm[i] = 1

module = importlib.import_module("_03_Design_Problems." + problem)
problem = getattr(module, problem)
p = problem()
const = Constraint(problem, reqU_call, reqL_call, parameters_call, dv_norm, dv_norm_l, qoi_norm, 1)

x = np.array([9.84419514e-01, 5.45486760e-05, 2.30184154e-01, 7.68787753e-01, 3.76366683e-01, 8.39994333e-01])


## Main Testing Arena
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize

algorithm = NSGA2(pop_size=100)

res = minimize(const,
               algorithm,
               ('n_gen', 200),
               seed=1,
               verbose=False)

# print(res.X)
# calculate a hash to show that all executions end with the same result
dist_2 = np.sum((res.X - x)**2, axis=1)
index = dist_2.argmin()
print(res.X[index])



