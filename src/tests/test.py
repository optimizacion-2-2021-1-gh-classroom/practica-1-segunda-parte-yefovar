import Simplex
from scipy.optimize import linprog
from pytest import approx
import numpy as np
from pulp import *
import cvxpy as cp

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

status = prob.solve(PULP_CBC_CMD(msg=0))
x=value(x)
y=value(y)

pulp_result = np.array([x,y])

##cvxpy

x = cp.Variable(boolean=False, integer= False)
y = cp.Variable(boolean=False, integer= False)


constraints = [0 <= cp.sum(x),
               0 <= cp.sum(y),
               cp.sum(x)<=4,
               cp.sum(2*y)<=12,
               cp.sum(3*x+2*y)<=18
               ]

model = cp.Maximize(cp.sum(3*x+5*y))

prob = cp.Problem(model, constraints)

result = prob.solve()

x=x.value
y=y.value

cvxpy_result = np.array([x,y])

##Simplex

problema = Simplex.Simplex(c,A,b,problem='Max')
method_result,opt,status = problema.solve()

print('Test con paqueteria scipy')
print(method_result== approx(scipy_result, abs=1e-8, rel=1e-8))

print('Test con paqueteria pulp')
print(method_result== approx(pulp_result, abs=1e-8, rel=1e-8))

print('Test con paqueteria cvxpy')
print(method_result== approx(cvxpy_result, abs=1e-6, rel=1e-6))

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

prob += 1*x + 1*y +2*z <= 9
prob += 1*x + 1*y -1*z <= 2
prob += -1*x + 1*y +1*z <= 4
prob += 1*x +1*y -4*z

status = prob.solve(PULP_CBC_CMD(msg=0))
x=value(x)
y=value(y)
z=value(z)

pulp_result = np.array([x,y,z])

##cvxpy

x = cp.Variable(boolean=False, integer= False)
y = cp.Variable(boolean=False, integer= False)
z = cp.Variable(boolean=False, integer= False)


constraints = [0 <= cp.sum(x),
               0 <= cp.sum(y),
               0 <= cp.sum(z),
               cp.sum(x+y+2*z)<=9,
               cp.sum(x+y-z)<=2,
               cp.sum(-x+y+z)<=4
               ]

model = cp.Minimize(cp.sum(1*x+1*y-4*z))

prob = cp.Problem(model, constraints)

result = prob.solve()

x=x.value
y=y.value
z=z.value

cvxpy_result = np.array([x,y,z])

##Simplex

problema = Simplex(c,A,b,problem='Min')
method_result,opt,status = problema.solve()

print('Test con paqueteria scipy')
print(method_result== approx(scipy_result, abs=1e-8, rel=1e-8))

print('Test con paqueteria pulp')
print(method_result== approx(pulp_result, abs=1e-8, rel=1e-8))

print('Test con paqueteria cvxpy')
print(method_result== approx(cvxpy_result, abs=1e-6, rel=1e-6))
