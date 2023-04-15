from diffusion import Diffusion
from random_walk import RandomWalk
from dopant_mobility import DopantMobility
from scipy.integrate import trapz
from plotter import Plotter
import numpy as np

class Brains():
    """
    Brains class

    Attributes
    ----------
    diffusion : Diffusion
        The diffusion class.
    drift : Diffusion
        The diffusion class with drift.
    decay : Diffusion
        The diffusion class with decay.
    random : RandomWalk
        The random walk class.
    random_multiple : RandomWalk
        The random walk class with multiple time steps.
    decay_static : RandomWalk
        The random walk class with decay.
    dopant_mobility : DopantMobility
        The dopant mobility class.

    Methods
    -------
    normalise_dict(target_dict)
        Normalises a dictionary.

    prdoduce_videos()
        Produces videos of the plots.

    plot_graphs()
        Plots the graphs.

    """


    def __init__(self):
        """
        Parameters
        ----------
        diffusion : Diffusion
            The diffusion class.
        drift : Diffusion
            The diffusion class with drift.
        decay : Diffusion
            The diffusion class with decay.
        random : RandomWalk
            The random walk class.
        random_multiple : RandomWalk
            The random walk class with multiple time steps.
        decay_static : RandomWalk
            The random walk class with decay.
        dopant_mobility : DopantMobility
            The dopant mobility class.

        Returns
        -------
        None

        """

        #Crating Diffusion Classes:
        self.diffusion = Diffusion("diffusion")
        self.drift = Diffusion("drift")
        self.decay = Diffusion("decay")

        #Creating Random Walk Classes:
        self.random = RandomWalk("random")
        self.random_multiple = RandomWalk("random-multiple")
        self.decay_static = RandomWalk("decay-static")
        
        #Creating Dopant Mobility and Plotter Classes:
        self.dopant_mobility = DopantMobility("dopant_mobility")
        self.area_vs_steps = Plotter("Number of Steps", "Integral Area", "area_vs_steps")


    def normalise_dict(self, target_dict):
        """
        Normalises a dictionary.

        Parameters
        ----------
        target_dict : dict
            The dictionary to normalise.

        Returns
        -------
        dict
            The normalised dictionary.
        """

        if isinstance(target_dict, dict): # Returns one normalised dictionary
            dict_max = max(target_dict.values())
            return dict(zip(target_dict.keys(), [target_dict[i] / dict_max for i in target_dict.keys()]))

        elif isinstance(target_dict, list): # Returns a list of normalised dictionaries
            dict_max = max([max(target_dict[i].values()) for i in range(len(target_dict))])
            return [dict(zip(target_dict[i].keys(), [target_dict[i][j] / dict_max for j in target_dict[i].keys()])) for i in range(len(target_dict))]


    def produce_videos(self):
        """
        Produces the videos.
        """

        self.diffusion.animate(self.diffusion.xlist, self.diffusion.diffusion_1d, 10, (-0.5, 0.5), (0, 1))
        self.drift.animate(self.drift.xlist, self.drift.diffusion_drift_1d, 0.1, (-1, 1), (0, 1))
        self.decay.animate(self.decay.xlist, self.decay.diffusion_decay_1d, 1.5e-4, (-0.0025, 0.0025), (0, 1))


    def plot_graphs(self):
        """
        Plots the graphs.
        """

        list_steps = np.array([i for i in range(500, 2501, 500)]) # List of steps for random walk

        # Creating dicts
        dict1 = self.normalise_dict(self.random.random_walk(1000, 50))
        dict2 = self.normalise_dict([dict(zip(self.random.xlist, self.diffusion.diffusion_decay_1d(self.random.xlist, tval))) for tval in self.random.tlist])
        dict3 = self.normalise_dict([self.random.random_walk(i, 55, (i/2600)*100) for i in list_steps])
        dict3_integrals = [trapz(list(arg.values()), list(arg.keys())) for arg in dict3] # Integrals of the random walk graphs
        dict4 = dict(zip(list_steps, dict3_integrals))

        # Plotting dicts
        self.random.plot_graph(dict1, labels=["Random Walk"], best_fit="gaussian", best_fit_label=True)
        self.random_multiple.plot_graph(*dict3, labels=[f"Steps = {i}" for i in list_steps], ylims=(0, 1))
        self.decay_static.plot_graph(*dict2, xlims=(-0.0025, 0.0025), ylims=(0, 1), marker="None", ls="-", zlist=self.random.tlist, zlabel="Time / s", colourbar=True)
        self.area_vs_steps.plot_graph(dict4, marker="x", xlims=(0, 3000), ylims=(0, 100), labels=["Integral Area"], best_fit="linear")
        self.dopant_mobility.plot_graph(dict(zip(self.dopant_mobility.temp_list, self.dopant_mobility.mobility(self.dopant_mobility.temp_list))), xlims=(250, 400), ylims=(0, 2e3), marker="None", ls="-", labels=["Mobility"])
