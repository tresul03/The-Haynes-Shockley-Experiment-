import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#todo: produce a graph of hole mobility against temperature

#intiialising the figure
fig = plt.figure()
plt.xlim(250, 500)

temperature = np.linspace(250, 500, 500) #dependent variable
charge_carrier_concentration = np.array([1e13*(10**i) for i in range(1, 8)])

#dopant mobility equation - I split it into parts for readability's sake
mobility_add_term = lambda temp: 54.3 * ((temp/300)**(-0.57))
mobility_numerator = lambda temp: 1.36e8 * (temp**(-2.33))
mobility_denominator = lambda temp, dopant_conc: 1 + 0.88 * (dopant_conc/(2.35e17 * (temp/300)**2.4)) * (temp/300)** -0.146

