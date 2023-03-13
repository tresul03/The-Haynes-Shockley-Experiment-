import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import subprocess
from scipy.optimize import curve_fit
from matplotlib.animation import FFMpegWriter
plt.rcParams["animation.ffmpeg_path"] = "C:\\ffmpeg\\bin\\ffmpeg.exe"

class Plotter():
    def __init__(self, x, y, func: int, xlabel: str, ylabel: str, figname: str):
        self.func = func            #the id of the function that x will be passed to
        self.xlabel = xlabel        #label of x-axis
        self.ylabel = ylabel        #label of y-axis
        self.figname = figname      #name of plot
        self.x = x                  #dependent variable
        match self.func:
            case 0:
                self.y = y
            case _:
                self.y = pd.DataFrame(y).to_csv(f"{self.figname}.csv", index=False)
                subprocess.call("functions")
                self.y = pd.DataFrame(pd.read_csv(f"{self.figname}.csv"))




        self.fig = plt.figure()                 #initialising figure
        plt.xlabel(self.xlabel)        #adding xlabel to figure
        plt.ylabel(self.ylabel)        #adding ylabel to figure


    def plot_graph(self, label=None, best_fit=False):
        plt.plot(
            self.x,
            self.y,
            ls="None",
            marker='x',
            markersize=4,
            color='#%06X' % random.randint(0, 0xFFFFFF),
            label=label
        )

        if best_fit:
            self.plot_best_fit()

        self.fig.tight_layout()
        self.fig.savefig(f"{self.figname}.pdf", dpi=350)

    def plot_best_fit(self):
        linear = lambda m,x,c: m*x+c
        popt, pcov = curve_fit(linear, self.x, self.y)

        plt.plot(
            self.x,
            popt[0]*self.x + popt[1],
            ls='--',
            color='#%06X' % random.randint(0, 0xFFFFFF)
        )

        print(f"Gradient = {popt[0]:.2f} +/- {pcov[0][0]:.2f}")
        print(f"Intercept = {popt[1]:2f} +/- {pcov[1][1]:.2f}")
    
    