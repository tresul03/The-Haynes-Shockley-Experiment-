from matplotlib import pyplot as plt
import numpy as np
import random
import pandas as pd
from plotter_v2 import Plotter

class RandomWalk():
    def random_walk(self):
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

        plotter = Plotter(dict_positions.keys(), dict_positions.values(), 0, "Displacement / m", "$P(x, t)$", "random")
        plotter.plot_graph()

randomer = RandomWalk()
randomer.random_walk()