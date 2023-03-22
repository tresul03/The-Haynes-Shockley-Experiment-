from values import Values
import numpy as np
from plotter import Plotter

class Diffusion():
    def __init__(self):
        self.xlabel = "Displacement / m"
        self.ylabel = "Charge Carrier Concentration / $n_{0}$"
        self.xlist = np.linspace(-1, 1, 50001)
        self.values = Values()

    def normaliser(self, t):
        return np.sqrt(4*np.pi*self.values.D*t) ** -1

    def diffusion_1d(self, x, t):
        return self.normaliser(t) * np.exp(-x**2 / (4*self.values.D * t))

    def diffusion_drift_1d(self, x, t):
        return self.normaliser(t) * np.exp(-(x - self.values.v*t)**2 / (4*self.values.D * t))

    def diffusion_decay_1d(self, x, t):
        return self.diffusion_drift_1d(x, t) * np.exp(-t/self.values.TAU)


