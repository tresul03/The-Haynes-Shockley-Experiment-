import random
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def random_walk() -> None:    
    walker = 0
    final_positions = []

    for _ in range(10000):
        for _ in range(1000):
            match random.randint(0, 1):
                case 0:
                    walker -= 1
                
                case 1:
                    walker += 1
            
        final_positions.append(walker)
        walker = 0
    
    count_positions = {}
    for i in range(min(final_positions), max(final_positions)+1):
        if final_positions.count(i) > 0:
            count_positions[i] = final_positions.count(i)
    
    plt.plot(
        count_positions.keys(),
        count_positions.values(),
        ls="None",
        marker=".",
        markersize=4
    )

    plt.ylim(ymin=0)
    plt.tight_layout()

    plt.savefig("random-walk.pdf", dpi=350)

#todo: write the random-walk function
#todo: plot the equation for diffusion next to the random-walk plot

def plot_diffusion() -> None:
    MOBILITY = 1e-1
    K = 1.38e-23        #Boltzmann's Constant
    T = 300             #Temperature
    Q = 1.6e-19         #Electron Charge

    D = (MOBILITY*K*T)/Q        #Diffusion Constant

    diffusion_1d = lambda x: np.exp(-x**2 / (4*D))

    xlist = np.linspace(-1, 1, 1000)

    plt.plot(
        xlist,
        diffusion_1d(xlist),
        ls='-',
        color="red"
    )

    plt.ylim(ymin=0)
    plt.tight_layout()

    plt.savefig("initial_diffusion_plot.pdf", dpi=350)

random_walk()
plot_diffusion()