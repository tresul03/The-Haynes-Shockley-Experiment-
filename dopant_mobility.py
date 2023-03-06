import matplotlib.pyplot as plt
import numpy as np
import random

#intiialising the figure
fig = plt.figure(figsize=(10, 7))
plt.xlim(290, 320)

temperature = np.linspace(290, 320, 500) #dependent variable
charge_carrier_concentration = np.array([1e13*(10**i) for i in range(1, 8)])

#dopant mobility equation - I split it into parts for readability's sake
mobility_add_term = lambda temp: 54.3 * ((temp/300)**(-0.57))
mobility_numerator = lambda temp: 1.36e8 * (temp**(-2.33))
mobility_denominator = lambda temp, dopant_conc: 1 + 0.88 * (dopant_conc/(2.35e17 * (temp/300)**2.4)) * (temp/300)** -0.146

#plotting graph
for charge_conc in charge_carrier_concentration:
    mobility = np.array(mobility_add_term(temperature)) + (np.array(mobility_numerator(temperature))/np.array(mobility_denominator(temperature, charge_conc)))
    plt.plot(
        temperature,
        mobility,
        ls='-',
        color='#%06X' % random.randint(0, 0xFFFFFF),
        label=str(charge_conc)
    )

#graph customisation
plt.legend()
plt.xlabel("T / K")
plt.ylabel("$\mu_{h} / cm^{2}/Vs$")
plt.tight_layout()

#saving graph
plt.savefig("complicatedmobilityagainstatemperaturewhichihaventfound.pdf", dpi=350)