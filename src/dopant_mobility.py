import numpy as np

class DopantMobility():
    def __init__(self):
        self.xlabel = "Temperature / K"
        self.ylabel = "Mobility / $cm^2 V^{-1} s^{-1}$"

        self.temp_list = np.linspace(10, 1000, 50001)
        self.mobility = lambda t: 2.4e8 * (t**-2.3)


