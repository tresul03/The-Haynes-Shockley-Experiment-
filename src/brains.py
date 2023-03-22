from diffusion import Diffusion
from values import Values
from plotter import Plotter
from random_walk import RandomWalk

class Brains():
    def __init__(self):
        self.values = Values()
        self.diffusion = Diffusion()

    def plot_diffusion_videos(self):
        plotter_diffusion = Plotter(self.diffusion.xlabel, self.diffusion.ylabel, "diffusion_v2")
        plotter_diffusion.animate(self.diffusion.xlist, self.diffusion.diffusion_1d, 10, (-0.5, 0.5), (0, 20))

        plotter_drift = Plotter(self.diffusion.xlabel, self.diffusion.ylabel, "drift_v2")
        plotter_drift.animate(self.diffusion.xlist, self.diffusion.diffusion_drift_1d, 0.1, (-1, 1), (0, 50))

        plotter_decay = Plotter(self.diffusion.xlabel, self.diffusion.ylabel, "decay_v2")
        plotter_decay.animate(self.diffusion.xlist, self.diffusion.diffusion_decay_1d, 1.5e-4, (-0.0025, 0.0025), (0, 20))

    def plot_random_walk_graphs(self):
