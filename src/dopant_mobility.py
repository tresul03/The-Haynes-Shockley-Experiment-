import numpy as np
from plotter import Plotter

class DopantMobility(Plotter):
    def __init__(self, figname):
        self.xlabel = "Temperature / K"
        self.ylabel = "Mobility / $cm^2 V^{-1} s^{-1}$"
        super().__init__(self.xlabel, self.ylabel, figname)

        self.temp_list = np.linspace(10, 1000, 50001)
        self.mobility = lambda t: 2.4e8 * (t**-2.3)


