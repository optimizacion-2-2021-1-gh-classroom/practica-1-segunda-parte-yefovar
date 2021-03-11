# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:57:29 2021

@author: joser
"""

##KKT
import numpy as np 



class Constraint:
    def __init__(self,A = None,x = None, b = None):
        self.A = A
        self.x = x
        self.b = b
        
        
class Variables:
    def __init__(self,var = None):
        self.var = var
        self.x = self.var_to_vec(self.var)
    
    @staticmethod   
    def var_to_vec(var):
        lenvar = len(var)
        x_vec = np.zeros(lenvar)
        return x_vec
    
    def __str__(self):
            return str(self.x)
        
    def __repr__(self):
        return str(self.x)
        
    
    
class Objective:
    def __init__(self,objective_coef = None, variables = None):
        self.objective_coef = objective_coef
        self.variables = variables
        self.maximum = self.objfun(self.objective_coef,self.variables)
    
    @staticmethod
    def objfun(objective_coef,variables):
        maximum = objective_coef @ variables.x
        return maximum
    
    
    
    def __str__(self):
            return str(self.maximum)
        
    def __repr__(self):
        return str(self.maximum)




class KKTOptLinear:
    def __init__(self,variables = None, constraints = None, objective = None):
        self.variables = variables
        self.constraints = constraints
        self.objective = objective
        self.gradient
        self.step_size
        
        
    
    