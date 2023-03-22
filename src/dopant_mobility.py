import numpy as np
from values import Values
from plotter import Plotter

class DopantMobility():
    def __init__(self):
        self.temp_list = np.linspace(10, 1000, 50001)
        self.mobility = lambda t: 2.4e8 * (t**-2.3)
        



plotter = Plotter("Temperature / K", "Mobility / $cm^2 V^{-1} s^{-1}$", "mobility")
plotter.plot_graph(DopantMobility().temp_list, DopantMobility().mobility(DopantMobility().temp_list), xlims=(150, 400), ylims=(0, 2e3), marker="None", ls="-")
print(DopantMobility().mobility(300))