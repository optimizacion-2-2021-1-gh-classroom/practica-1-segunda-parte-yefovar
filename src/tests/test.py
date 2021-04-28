from Simplex import *
from scipy.optimize import linprog
from pytest import approx
import numpy as np
from pulp import *

#Maximization case

##Scipy

c = np.array([3, 5])
b = np.array([4, 12, 18])
A = np.array([[1,  0],
              [0,  2],
              [3, 2]]) 

opt = linprog(c=-c, A_ub=A, b_ub=b,
              method="simplex")
scipy_result = opt.x

##Pulp

x = LpVariable('x',0)
y = LpVariable('y',0)

prob = LpProblem('myProblem',LpMinimize)

prob += 1*x + 0*y <= 4
prob += 0*x + 2*y <= 12
prob += 3*x + 2*y <= 18
prob += -3*x -5*y

status = prob.solve()
x=value(x)
y=value(y)

pulp_result = np.array([x,y])

##Simplex

problema = Simplex(c,A,b,problem='Max')
method_result,opt,status = problema.solve()

print('Test con paqueteria scipy')
print(method_result== approx(scipy_result, abs=1e-8, rel=1e-8))

print('Test con paqueteria pulp')
print(method_result== approx(pulp_result, abs=1e-8, rel=1e-8))

print('Test con paqueteria cvxpy')

#Minimization case

##Scipy

c = np.array([1, 1, -4])
b = np.array([9, 2, 4])
A = np.array([[1,  1,  2],
              [1,  1, -1],
              [-1, 1,  1]]) 

opt = linprog(c=c, A_ub=A, b_ub=b,
              method="simplex")
scipy_result = opt.x

##Pulp
x = LpVariable('x',0)
y = LpVariable('y',0)
z = LpVariable('z',0)

prob = LpProblem('myProblem',LpMinimize)

prob += 1*x + 1*y +1*z <= 9
prob += 1*x + 1*y +1*z <= 2
prob += -1*x + 1*y +1*z <= 4
prob += 1*x +1*y -4*z

status = prob.solve()
x=value(x)
y=value(y)
z=value(z)

pulp_result = np.array([x,y,z])

##Simplex

problema = Simplex(c,A,b,problem='Min')
method_result,opt,status = problema.solve()

print('Test con paqueteria scipy')
print(method_result== approx(scipy_result, abs=1e-8, rel=1e-8))

print('Test con paqueteria pulp')
print(method_result== approx(pulp_result, abs=1e-8, rel=1e-8))

print('Test con paqueteria cvxpy')
