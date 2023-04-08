from values import Values
import numpy as np
from plotter import Plotter

class Diffusion(Plotter):
    def __init__(self, figname):
        """
        Diffusion class

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
        values : Values
            The values object.
        
        """

        self.xlabel = "Displacement / $\mu$m"
        self.ylabel = "Charge Carrier Concentration / $n_{0}$"
        self.xlist = np.linspace(-1, 1, 50001)
        self.values = Values()

        super().__init__(self.xlabel, self.ylabel, figname)


    def normaliser(self, t):
        """
        Normalises the diffusion equation.

        Parameters
        ----------
        t : float
            The time.

        Returns
        -------
        float
            The normalised value.
        """

        return np.sqrt(4*np.pi*self.values.D*t) ** -1


    def diffusion_1d(self, x, t):
        """
        Diffusion equation.

        Parameters
        ----------
        x : float
            The displacement.
        t : float

        Returns
        -------
        float
            The normalised value.
        """

        return self.normaliser(t) * np.exp(-x**2 / (4*self.values.D * t))


    def diffusion_drift_1d(self, x, t):
        """
        Diffusion equation with drift.

        Parameters
        ----------
        x : float
            The displacement.
        t : float
            The time.

        Returns
        -------
        float
            The normalised value.
        """

        return self.normaliser(t) * np.exp(-(x - self.values.v*t)**2 / (4*self.values.D * t))


    def diffusion_decay_1d(self, x, t):
        """
        Diffusion equation with decay.

        Parameters
        ----------
        x : float
            The displacement.
        t : float
            The time.

        Returns
        -------
        float
            The normalised value.
        """

        return self.diffusion_drift_1d(x, t) * np.exp(-t/self.values.TAU)
