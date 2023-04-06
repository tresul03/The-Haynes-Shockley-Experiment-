import numpy as np
import matplotlib.pyplot as plt
from diffusion import Diffusion
from matplotlib.colors import LinearSegmentedColormap

# Define the function that takes x and y as inputs
plt.figure(figsize=(10, 7))
diffusion = Diffusion()

# Create a grid of x and y values using np.meshgrid
x = np.linspace(-1, 1, 500)
t = np.linspace(1e-8, 10, 500)
X, T = np.meshgrid(x, t)

# Evaluate the function at each point in the grid
Z = diffusion.diffusion_1d(X, T)
Z /= np.max(Z)
cmap = LinearSegmentedColormap.from_list('custom', ['purple', 'orange', 'yellow'])

# Create a 2D color map using pcolormesh
plt.pcolormesh(T, X, Z, cmap=cmap)
cbar = plt.colorbar()
cbar.set_label('Normalised Concentration / $n_{0}$')

# Set the axis labels and title
plt.xlabel('t / s')
plt.ylabel('x / $\mu$m')
plt.ylim(-0.25, 0.25)
plt.xlim(0, 1)

plt.savefig("plots/test.pdf")