import numpy as np
from plotter import Plotter

class DopantMobility(Plotter):
    """
    DopantMobility class

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
    temp_list : numpy.ndarray
        The list of temperatures.
    mobility : function
        The mobility function.

    Methods
    -------
    None

    """
    def __init__(self, figname):

        self.xlabel = "Temperature / K"
        self.ylabel = "Mobility / $cm^2 V^{-1} s^{-1}$"
        super().__init__(self.xlabel, self.ylabel, figname)

        self.temp_list = np.linspace(10, 1000, 50001)
        self.mobility = lambda t: 2.4e8 * (t**-2.3)


