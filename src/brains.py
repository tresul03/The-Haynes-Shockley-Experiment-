from diffusion import Diffusion
from random_walk import RandomWalk
from dopant_mobility import DopantMobility

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

        self.diffusion = Diffusion("diffusion")
        self.drift = Diffusion("drift")
        self.decay = Diffusion("decay")

        self.random = RandomWalk("random")
        self.random_multiple = RandomWalk("random-multiple")
        self.decay_static = RandomWalk("decay-static")

        self.dopant_mobility = DopantMobility("dopant_mobility")


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

        if type(target_dict) == dict:
            dict_max = max(target_dict.values())
            return dict(zip(target_dict.keys(), [target_dict[i] / dict_max for i in target_dict.keys()]))
        
        elif type(target_dict) == list:
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

        self.dopant_mobility.plot_graph(self.dopant_mobility.temp_list, self.dopant_mobility.mobility(self.dopant_mobility.temp_list), xlims=(250, 400), ylims=(0, 2e3), marker="None", ls="-")
        
        list_steps = [i for i in range(200, 2001, 400)]
        dict1 = self.normalise_dict(self.random.random_walk(1000, 50))
        dict2 = self.normalise_dict([self.random.random_walk(i, 55, 50) for i in list_steps])
        dict3 = self.normalise_dict([dict(zip(self.random.xlist, self.diffusion.diffusion_decay_1d(self.random.xlist, tval))) for tval in self.random.tlist])

        self.random.plot_multiple_plots(1, dict1, best_fit="exponential")
        self.random_multiple.plot_graph(*dict2, xlims=(-200, 400), ylims=(0, 1), labels=[f"steps = {i}" for i in list_steps])
        self.decay_static.plot_graph(*dict3, xlims=(-0.0025, 0.0025), ylims=(0, 1), marker="None", ls="-", labels=[f"t = {tval*1e6:.1f}$\mu$s" for tval in self.random.tlist])
