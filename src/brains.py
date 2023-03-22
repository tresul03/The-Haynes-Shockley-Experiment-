from diffusion import Diffusion
from values import Values
from plotter import Plotter
from random_walk import RandomWalk

class Brains():
    def __init__(self):
        self.values = Values()
        self.diffusion = Diffusion()
        self.randomer = RandomWalk()

    def plot_diffusion_videos(self):
        plotter_diffusion = Plotter(self.diffusion.xlabel, self.diffusion.ylabel, "diffusion_v2")
        plotter_drift = Plotter(self.diffusion.xlabel, self.diffusion.ylabel, "drift_v2")
        plotter_decay = Plotter(self.diffusion.xlabel, self.diffusion.ylabel, "decay_v2")

        plotter_diffusion.animate(self.diffusion.xlist, self.diffusion.diffusion_1d, 10, (-0.5, 0.5), (0, 20))
        plotter_drift.animate(self.diffusion.xlist, self.diffusion.diffusion_drift_1d, 0.1, (-1, 1), (0, 50))
        plotter_decay.animate(self.diffusion.xlist, self.diffusion.diffusion_decay_1d, 1.5e-4, (-0.0025, 0.0025), (0, 20))


    def plot_random_walk_graphs(self):
        plotter = Plotter(self.randomer.xlabel, self.randomer.ylabel, "random_v2") #plotter for random walk
        plotter2 = Plotter(self.randomer.xlabel, self.randomer.ylabel, "random-multiple_v2") #plotter for multiple random walks
        plotter3 = Plotter(self.randomer.xlabel, self.randomer.ylabel, "decay-static_v2") #plotter for decay at set times

        dict1 = self.randomer.random_walk(50)
        dict2 = self.randomer.diffusion()
        dict3 = [self.randomer.random_walk(i) for i in range(50, 100, 10)]
        dict4 = [dict(zip(self.randomer.xlist, self.diffusion.diffusion_decay_1d(self.randomer.xlist, tval))) for tval in self.randomer.tlist]

        plotter.plot_multiple_plots(2, dict1, dict2) #plots random walk and diffusion
        plotter2.plot_multiple_graphs(*dict3, xlims=(-1500, 500), ylims=(0, 1000)) #plots random walk at different probabilities
        plotter3.plot_multiple_graphs(*dict4, xlims=(-0.0025, 0.0025), ylims=(0, 20), marker="None", ls="-") #plots decay at set times

