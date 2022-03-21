from scipy.optimize import differential_evolution
from examples import PressureVessel, TensionCompressionSpring, SpeedReducer
import pandas as pd

class DifferentialEvolution:
    def __init__(self, problem, bounds, seed, G, mutation, recombination, popsize=15):
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
        self.result = self.func(self.problem, bounds=self.bounds, seed=self.seed, maxiter=self.maxiter, mutation=self.mutation, recombination=self.recombination)