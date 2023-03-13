from matplotlib import pyplot as plt
import numpy as np
import subprocess
import pandas as pd
from plotter import Plotter

class RandomWalk():
    def random_walk(self):
        subprocess.call("functions")
        df = pd.DataFrame(pd.read_csv("random_walk.csv"))
        df = df.sort_values(by=["x/m"]).reset_index()
        
        dict_df = {}
        for i in range(len(df)):
            count = (df["x/m"] == df["x/m"][i]).sum()
            if df["x/m"][i] not in dict_df and count > 0:
                dict_df[i] = count
        
        dict_df = {dict_df[keys]:(values / max(values)) for keys, values, in dict_df.items()}

        xlabel, ylabel = "Displacement / m", "$P(x, t)$"

        #todo: pass dict_df into plotter
        plotter = Plotter()


randomer = RandomWalk()
randomer.random_walk()