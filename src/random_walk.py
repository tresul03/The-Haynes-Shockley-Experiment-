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
        self.tlist = np.linspace(0.4e-4, 1e-4, 15) 
        self.values = Values()

        super().__init__(self.xlabel, self.ylabel, figname)


    def random_walk(self, steps, skew_point: int, decay_prob=0) -> dict: #skew_point is the probability of moving right, decay_prob is the probability of decay
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

        walker = 0 #initial particle position
        positions = [] #list of final positions reached by each particle

        for _ in range(10000): #10000 particles
            for _ in range(steps): #1000 steps per particle
                match random.randint(0, 100) <= skew_point: #probability of moving right 
                    case False: 
                        walker -= 1
                    case _:
                        walker += 1
            
            if random.randint(0, 100) >= decay_prob:
                positions.append(walker)

            walker = 0 #resets position for next particle
        
        dict_positions = {} #dictionary of positions and number of particles at that position
        for i in range(min(positions), max(positions)+1):
            if positions.count(i) > 0:
                dict_positions[i] = positions.count(i)

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
