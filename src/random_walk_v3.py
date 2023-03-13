from matplotlib import pyplot as plt
import numpy as np
import subprocess
import pandas as pd
from plotter_v2 import Plotter

class RandomWalk():
    def random_walk(self):
        subprocess.call("gcc functions.c -o functions")
        subprocess.call("functions")
        df = pd.DataFrame(pd.read_csv("random_walk.csv")).reset_index()

        dict_df = {}
        for i in range(min(df["x/m"]), max(df["x/m"])+1):
            try:
                if df["x/m"].value_counts()[i] > 0:
                    dict_df[i] = df["x/m"].value_counts()[i]
            except KeyError:
                continue


        max_df = max(dict_df.values())
        for keys in dict_df.keys():
            dict_df[keys] /= max_df

        xlabel, ylabel = "Displacement / m", "$P(x, t)$"

        #todo: pass dict_df into plotter
        plotter = Plotter(dict_df.keys(), dict_df.values(), 0, xlabel, ylabel, "random")
        plotter.plot_graph()


randomer = RandomWalk()
randomer.random_walk()