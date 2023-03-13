import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib.animation import FFMpegWriter
plt.rcParams["animation.ffmpeg_path"] = "C:\\ffmpeg\\bin\\ffmpeg.exe"


class Plotter():
    def __init__(self, x, y, xlabel, ylabel, figname, time=None, funct=None, ls="None", marker='.', best_fit=False, animation=False):
        self.x = x
        self.y = y
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.figname = figname
        self.time = time
        self.funct = funct
        self.ls = ls
        self.marker = marker
        self.best_fit = best_fit
        self.animation = animation

        self.fig = plt.figure(figsize=(10, 7))
        self.fig.set_xlabel(self.xlabel)
        self.fig.set_ylabel(self.ylabel)

    def animate(self):
        l, = plt.plot([], [], ls="-", color="red")
        metadata = dict(title="Diffusion", artist="Resul Teymuroglu")
        writer = FFMpegWriter(fps=100, metadata=metadata)

        with writer.saving(f"plots/{self.figname}.mp4", 100):
            for tval in np.linspace(0, self.time, 1000):
                match tval:
                    case 0:
                        self.ylist = self.xlist * 0
                    case _:
                        self.ylist = self.funct

                l.set_data(self.xlist, self.ylist)
                writer.grab_frame()
                self.ylist = np.array([])
    
    def plot(self):



#todo: write animate function
#todo: write plotting function


'''
animate:
    produces mp4 of function variation with time
    how:


'''