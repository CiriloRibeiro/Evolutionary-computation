from scipy.optimize import differential_evolution
from problemas import PressureVessel, TensionCompressionSpring, SpeedReducer
import pandas as pd

class DifferentialEvolution:
    def __init__(self, problem, bounds, seed, G, mutation, recombination, popsize=15):
    """
    scipy.optimize.differential_evolution(func, bounds, args=(), strategy='best1bin', maxiter=1000, 
    popsize=15, tol=0.01, mutation=(0.5, 1), recombination=0.7, seed=None, callback=None, disp=False, 
    polish=True, init='latinhypercube', atol=0, updating='immediate', workers=1, constraints=(), x0=None)
    """
        self.func = differential_evolution
        self.result = None
        self.problem = problem
        self.bounds = bounds
        self.seed = seed
        self.maxiter = G
        self.mutation = mutation
        self.recombination = recombination
        self.popsize = popsize

    @property
    def fun(self):
        return self.result.fun
        
    def run(self):
        self.result = self.func(self.problem, bounds=self.bounds, seed=self.seed, maxiter=self.maxiter, mutation=self.mutation, recombination=self.recombination, self.popsize=popsize)