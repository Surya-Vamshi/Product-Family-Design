import numpy as np
import importlib
from Constraint import Constraint
from Constraint_test import Constraint_test


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

x = np.array([0.84760726, 0.10843993, 0.00252505, 0.24770135, 0.45374032, 0.55195826])
print(x)

## Main Testing Arena
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize

algorithm = NSGA2(pop_size=20)

res = minimize(const,
               algorithm,
               ('n_gen', 200),
               seed=1,
               verbose=False)

# print(res.X)
x = x * dv_norm + dv_norm_l

# calculate a hash to show that all executions end with the same result
dist_2 = np.sum((res.X - x)**2, axis=1)
index = dist_2.argmin()
x_final = res.X[index]
x_final = (x_final - dv_norm_l) / dv_norm

const1 = Constraint_test(problem, reqU_call* 0.99, reqL_call* 1.01, parameters_call, dv_norm, dv_norm_l, qoi_norm, 1)

N_pop = 3*10
from pymoo.algorithms.soo.nonconvex.pso import PSO
algorithm = PSO(pop_size=N_pop, adaptive=True, max_velocity_rate=0.020)

res = minimize(const1, algorithm, seed=1, verbose=False)

print(res.X)

if any(const1.Constraint_fun(x_final) > 0):
    dv_par_box = 0
    exitflag = 0
    print("Inside if condition")
else:
    print("Inside else condition")
    exitflag = 1
print(const1.Constraint_fun(x_final))



