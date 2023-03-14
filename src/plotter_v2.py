import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import subprocess
from scipy.optimize import curve_fit
from matplotlib.animation import FFMpegWriter
plt.rcParams["animation.ffmpeg_path"] = "C:\\ffmpeg\\bin\\ffmpeg.exe"

class Plotter():
    def __init__(self, xlabel: str, ylabel: str, figname: str):
        self.xlabel = xlabel        #label of x-axis
        self.ylabel = ylabel        #label of y-axis
        self.figname = figname      #name of plot
        self.fig = plt.figure(figsize=(10, 7))     #initialising figure

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
    
    def plot_multiple_plots(self, n, *args: dict):
        rows = int(np.ceil(n/np.ceil(np.sqrt(n))))
        columns = int(np.ceil(np.sqrt(n)))
        

        for arg in args:
            ax = self.fig.add_subplot(rows, columns, args.index(arg)+1)
            ax.plot(
                arg.keys(),
                arg.values(),
                ls="None",
                marker='x',
                markersize=4,
                color='#%06X' % random.randint(0, 0xFFFFFF),
            )

            ax.set_xlabel(self.xlabel)
            ax.set_ylabel(self.ylabel)

            self.fig.tight_layout()
            self.fig.savefig(f"plots/{self.figname}.pdf")
