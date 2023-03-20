from values import Values
import numpy as np
from plotter_v2 import Plotter

class Diffusion:
    def normaliser(self, t):
        return np.sqrt(4*np.pi*Values.D*t) ** -1

    def diffusion_1d(self, x, t):
        return self.normaliser(t) * np.exp(-x**2 / (4*Values.D * t))

    def diffusion_drift_1d(self, x, t):
        return self.normaliser(t) * np.exp(-(x - Values.v*t)**2 / (4*Values.D * t))

    def diffusion_decay_1d(self, x, t):
        return self.diffusion_drift_1d(x, t) * np.exp(-t/Values.TAU)

    xlist = np.linspace(-1, 1, 50001)
    xlabel = "Displacement / m"
    ylabel = "Charge Carrier Concentration / $n_{0}$"

diffusion = Diffusion()
plotter_diffusion = Plotter(diffusion.xlabel, diffusion.ylabel, "diffusion_v2")
plotter_diffusion.animate(diffusion.xlist, diffusion.diffusion_1d, 10, (-0.5, 0.5), (0, 20))

drift = Diffusion()
plotter_drift = Plotter(drift.xlabel, drift.ylabel, "drift_v2")
plotter_drift.animate(drift.xlist, drift.diffusion_drift_1d, 0.1, (-1, 1), (0, 50))

decay = Diffusion()
plotter_decay = Plotter(decay.xlabel, decay.ylabel, "decay_v2")
plotter_decay.animate(decay.xlist, decay.diffusion_decay_1d, 1.5e-4, (-0.0025, 0.0025), (0, 20))
