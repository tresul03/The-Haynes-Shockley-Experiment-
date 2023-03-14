import numpy as np
import random
from plotter_v2 import Plotter
from values import Values

class RandomWalk():
    def random_walk(self) -> dict:
        walker = 0 #initial particle position
        positions = [] #list of final positions reached by each particle

        for _ in range(10000):
            for _ in range(1000):
                match random.randint(0, 1): 
                    case 0:
                        walker -= 1
                    case _:
                        walker += 1

            positions.append(walker)
            walker = 0 #resets position for next particle

        dict_positions = {}
        for i in range(min(positions), max(positions)+1):
            if positions.count(i) > 0:
                dict_positions[i] = positions.count(i)

        max_position = max(dict_positions.values())
        for key in dict_positions.keys():
            dict_positions[key] /= max_position

        return dict_positions

    def diffusion(self) -> dict:
        diffusion_1d = lambda x: np.exp(-x**2 / (4*Values.D))
        keys = np.linspace(-1, 1, 1001)
        values = diffusion_1d(keys)

        return dict(zip(keys, values))


randomer = RandomWalk()
dict1 = randomer.random_walk()
dict2 = randomer.diffusion()

plotter = Plotter("Displacement / m", "$P(x, t)$", "random")
plotter.plot_multiple_plots(2, dict1, dict2)