# Author: Resul Teymuroglu
# Date: 8/4/2023
# Description: This file contains the RandomWalk class, which is used to generate random walks and plot them.

import numpy as np
import random
from values import Values
from plotter import Plotter

class RandomWalk(Plotter):
    """
    RandomWalk class

    Parameters
    ----------
    figname : str
        The name of the plot.

    Attributes
    ----------
    xlabel : str
        The label of the x-axis.
    ylabel : str
        The label of the y-axis.
    xlist : numpy.ndarray
        The list of x-values.
    tlist : numpy.ndarray
        The list of t-values.
    values : Values
        The values object.

    Methods
    -------
    random_walk(steps, skew_point, decay_prob)
        Generates a random walk.
    diffusion()
        Generates a diffusion curve.

    """

    def __init__(self, figname):
        self.xlabel = "Displacement / $\mu$m"
        self.ylabel = "Frequency"
        self.xlist = np.linspace(-1, 1, 500000)
        self.tlist = np.linspace(0.4e-4, 0.45e-4, 15) 
        self.values = Values()

        super().__init__(self.xlabel, self.ylabel, figname)


    def random_walk(self, steps, drift_prob: int, decay_prob=0) -> dict: #skew_point is the probability of moving right, decay_prob is the probability of decay
        """
        Generates a random walk.
        
        Parameters
        ----------
        steps : int
            The number of steps to take.
        skew_point : int
            The probability of moving right.
        decay_prob : int
            The probability of decay.

        Returns
        -------
        dict_positions : dict
            The dictionary of positions and number of particles at that position.
        
        """

        num_particles = 500000
        positions = np.zeros(num_particles, dtype=int)

        for _ in range(steps):  
            drift_right = np.random.rand(num_particles) <= (drift_prob / 100)
            positions[drift_right] += 1
            positions[~drift_right] -= 1

        decay = np.random.rand(num_particles) > (decay_prob / 100)
        positions = positions[decay]

        unique_positions, counts = np.unique(positions, return_counts=True)
        dict_positions = dict(zip(unique_positions, counts))

        return dict_positions


    def diffusion(self) -> dict:
        """
        Generates a diffusion curve.

        Returns
        -------
        dict
            The dictionary of positions and number of particles at that position.
        
        """
        
        diffusion_1d = lambda x: np.exp(-x**2 / (4*self.values.D)) #diffusion equation
        keys = np.linspace(-1, 1, 1001)
        values = diffusion_1d(keys)

        return dict(zip(keys, values))
