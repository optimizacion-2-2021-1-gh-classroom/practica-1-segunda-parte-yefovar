from __init__ import Symplex
#from src import *
from scipy.optimize import linprog
from pytest import approx
import numpy as np

#Maximization case

#Minimization case

c = np.array([1, 1, -4])
b = np.array([9, 2, 4])
A = np.array([[1,  1,  2],
              [1,  1, -1],
              [-1, 1,  1]]) 

opt = linprog(c=c, A_ub=A, b_ub=b,
              method="simplex")
python_result = opt.x

problema = Simplex(c,A,b,problem='Min')
method_result = problema.solve()

print(method_result== approx(python_result, abs=1e-8, rel=1e-8))
