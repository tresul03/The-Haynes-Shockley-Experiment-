from diffusion import Diffusion
from values import Values
from plotter import Plotter
from random_walk import RandomWalk
from dopant_mobility import DopantMobility

class Brains():
    def __init__(self):
        self.values = Values()
        self.randomer = RandomWalk()
        self.dopant_mobility = DopantMobility()
        self.diffusion = Diffusion()

    def plot_diffusion_videos(self): #plots diffusion videos
        diffusion = Diffusion() #plots diffusion
        plotter_diffusion = Plotter(diffusion.xlabel, diffusion.ylabel, "diffusion")
        plotter_diffusion.animate(diffusion.xlist, diffusion.diffusion_1d, 10, (-0.5, 0.5), (0, 1))

        drift = Diffusion() #plots diffusion with drift
        plotter_drift = Plotter(drift.xlabel, drift.ylabel, "drift")
        plotter_drift.animate(drift.xlist, drift.diffusion_drift_1d, 0.1, (-1, 1), (0, 1))

        decay = Diffusion() #plots diffusion with drift and decay
        plotter_decay = Plotter(decay.xlabel, decay.ylabel, "decay")
        plotter_decay.animate(decay.xlist, decay.diffusion_decay_1d, 1.5e-4, (-0.0025, 0.0025), (0, 1))


    def plot_random_walk_graphs(self):
        plotter = Plotter(self.randomer.xlabel, self.randomer.ylabel, "random") #plotter for random walk
        plotter2 = Plotter(self.randomer.xlabel, self.randomer.ylabel, "random-multiple") #plotter for multiple random walks
        plotter3 = Plotter(self.randomer.xlabel, self.randomer.ylabel, "decay-static") #plotter for decay at set times

        dict1 = self.randomer.random_walk(50)
        dict3 = [self.randomer.random_walk(i, i) for i in range(50, 100, 10)]
        dict4 = [dict(zip(self.randomer.xlist, self.diffusion.diffusion_decay_1d(self.randomer.xlist, tval))) for tval in self.randomer.tlist]

        dict1_max = max(dict1.values())
        dict4_max = max([max(dict4[i].values()) for i in range(len(dict4))])

        dict1 = dict(zip(dict1.keys(), [dict1[i] / dict1_max for i in dict1.keys()]))
        dict4 = [dict(zip(dict4[i].keys(), [dict4[i][j] / dict4_max for j in dict4[i].keys()])) for i in range(len(dict4))]

        plotter.plot_multiple_plots(1, dict1, best_fit="exponential") #plots random walk and diffusion
        plotter2.plot_multiple_graphs(*dict3, xlims=(-100, 1500), ylims=(0, 150), labels=[f"P(right) = P(decay) = {i / 100}" for i in range(50, 100, 10)]) #plots random walk at different probabilities of drift and decay
        plotter3.plot_multiple_graphs(*dict4, xlims=(-0.0025, 0.0025), ylims=(0, 1), marker="None", ls="-", labels=[f"t = {tval*1e6:.1f}$\mu$s" for tval in self.randomer.tlist]) #plots decay at set times


    def plot_dopant_mobility_graphs(self):
        plotter = Plotter(self.dopant_mobility.xlabel, self.dopant_mobility.ylabel, "mobility")
        plotter.plot_graph(self.dopant_mobility.temp_list, self.dopant_mobility.mobility(self.dopant_mobility.temp_list), xlims=(250, 400), ylims=(0, 2e3), marker="None", ls="-")

    