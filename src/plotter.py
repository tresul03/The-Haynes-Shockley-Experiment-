import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
from scipy.optimize import curve_fit
from matplotlib.animation import FFMpegWriter
plt.rcParams["animation.ffmpeg_path"] = "C:\\ffmpeg\\bin\\ffmpeg.exe"


class Plotter():
    def __init__(self, x, y, xlabel, ylabel, figname, funct=None, best_fit=False):
        self.x = x
        self.y = y
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.figname = figname
        self.funct = funct
        self.best_fit = best_fit

        self.fig = plt.figure(figsize=(10, 7))

        self.fig.set_xlabel(self.xlabel)
        self.fig.set_ylabel(self.ylabel)

    def animate(self, time):
        l, = plt.plot([], [], ls="-", color="red")
        y = np.array([])
        
        metadata = dict(title="Diffusion", artist="Resul Teymuroglu")
        writer = FFMpegWriter(fps=100, metadata=metadata)

        with writer.saving(f"plots/{self.figname}.mp4", 100):
            for tval in np.linspace(0, time, 1000):
                match tval:
                    case 0:
                        y = self.x * 0
                    case _:
                        y = self.funct(self.x, tval)

                l.set_data(x, y)
                writer.grab_frame()
                y = np.array([])
    
    def plot_graph(self, label=None):
        self.fig.plot(
            self.x,
            self.y,
            ls="None",
            marker='x',
            markersize=4,
            color='#%06X' % random.randint(0, 0xFFFFFF),
            label=label
        )

        if self.best_fit:
            linear = lambda m,x,c: m*x+c

            popt, pcov = curve_fit(linear, self.x, self.y)
            self.fig.plot(
                self.x,
                popt[0]*self.x + popt[1],
                ls='--',
                color='#%06X' % random.randint(0, 0xFFFFFF),
            )
            
            print(f"Gradient = {popt[0]:.2f} +/- {pcov[0][0]:.2f}, Intercept = {popt[1]:.2f} +/- {pcov[1][1]:.2f}")


        self.fig.legend()
        self.fig.tight_layout()
        self.fig.savefig(f"{self.figname}.pdf", dpi=350)

#todo: write animate function
#todo: write plotting function
#! y-values are obtained by passing xlist into c program