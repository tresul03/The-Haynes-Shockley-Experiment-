import numpy as np
import random
from plotter_v2 import Plotter
from values import Values
from diffusion_v2 import Diffusion

class RandomWalk():
    def random_walk(self, upper: int) -> dict:
        walker = 0 #initial particle position
        positions = [] #list of final positions reached by each particle

        for _ in range(10000):
            for _ in range(1000):
                match random.randint(0, 100) > upper: 
                    case False:
                        walker -= 1
                    case _:
                        walker += 1

            positions.append(walker)
            walker = 0 #resets position for next particle

        dict_positions = {}
        for i in range(min(positions), max(positions)+1):
            if positions.count(i) > 0:
                dict_positions[i] = positions.count(i)

        return dict_positions

    def diffusion(self) -> dict:
        diffusion_1d = lambda x: np.exp(-x**2 / (4*Values.D))
        keys = np.linspace(-1, 1, 1001)
        values = diffusion_1d(keys)

        return dict(zip(keys, values))

randomer = RandomWalk()
diffusion = Diffusion()
plotter = Plotter("Displacement / m", "$P(x, t)$", "random")
plotter2 = Plotter("Displacement / m", "$P(x, t)$", "random-multiple")
plotter3 = Plotter("Displacement / m", "$P(x, t)$", "decay_static")

xlist = np.linspace(-1, 1, 500000)
tlist = np.linspace(0.4e-4, 1e-4, 10)

dict1 = randomer.random_walk(50)
dict2 = randomer.diffusion()
dict3 = [randomer.random_walk(i) for i in range(50, 100, 10)]
dict4 = [dict(zip(xlist, diffusion.diffusion_decay_1d(xlist, tval))) for tval in tlist]

plotter.plot_multiple_plots(2, dict1, dict2)
plotter2.plot_multiple_graphs(*dict3, xlims=(-1500, 500), ylims=(0, 1000))
plotter3.plot_multiple_graphs(*dict4, xlims=(-0.0025, 0.0025), ylims=(0, 20), marker="None", ls="-")