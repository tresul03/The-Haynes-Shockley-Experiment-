import random
from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 7))

def random_walk() -> None:
    fig1 = plt.subplot(1, 2, 1)

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

    count_max = max(count_positions.values())
    for keys in count_positions.keys():
        count_positions[keys] /= count_max


    fig1.plot(
        count_positions.keys(),
        count_positions.values(),
        ls="None",
        marker=".",
        markersize=4
    )

    fig1.set_ylim(ymin=0)


def plot_diffusion() -> None:
    fig2 = plt.subplot(1, 2, 2)

    MOBILITY = 1e-1
    K = 1.38e-23        #Boltzmann's Constant
    T = 300             #Temperature
    Q = 1.6e-19         #Electron Charge

    D = (MOBILITY*K*T)/Q        #Diffusion Constant

    diffusion_1d = lambda x: np.exp(-x**2 / (4*D))

    xlist = np.linspace(-1, 1, 1000)

    fig2.plot(
        xlist,
        diffusion_1d(xlist),
        ls='-',
        color="red"
    )

    fig2.set_ylim(ymin=0)


random_walk()
plot_diffusion()

plt.tight_layout()
plt.savefig("plots/random-walk.pdf")