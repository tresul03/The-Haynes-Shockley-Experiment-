import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.optimize import curve_fit
from matplotlib.animation import FFMpegWriter
plt.rcParams["animation.ffmpeg_path"] = "C:\\ffmpeg\\bin\\ffmpeg.exe"

class Plotter():
    def __init__(self, xlabel: str, ylabel: str, figname: str):
        self.xlabel = xlabel        #label of x-axis
        self.ylabel = ylabel        #label of y-axis
        self.figname = figname      #name of plot
        self.fig = plt.figure(figsize=(10, 7))     #initialising figure
        self.ax = self.fig.add_subplot(111)        #initialising axis


    def plot_graph(self, xlist, ylist, xlims, ylims, ls="None", marker='x', label=None, best_fit=False):
        self.ax.plot(
            xlist,
            ylist,
            ls=ls,
            marker=marker,
            markersize=4,
            color='#%06X' % random.randint(0, 0xFFFFFF),
            label=label
        )

        if best_fit:
            self.plot_best_fit(xlist, ylist)

        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)
        self.ax.set_xlim(xlims)
        self.ax.set_ylim(ylims)

        self.fig.tight_layout()
        self.fig.savefig(f"plots/{self.figname}.pdf", dpi=350)

    def plot_best_fit(self, xlist, ylist):
        linear = lambda m,x,c: m*x+c
        popt, pcov = curve_fit(linear, xlist, ylist)

        plt.plot(
            xlist,
            popt[0]*xlist + popt[1],
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
            self.fig.savefig(f"plots/{self.figname}.pdf", dpi=350)


    def animate(self, xlist, func, time, xlims, ylims):
        metadata = dict(title="Diffusion", artist="Resul Teymuroglu")
        writer = FFMpegWriter(fps=100, metadata=metadata)
        l, = plt.plot([], [], ls="-", color="red")

        with writer.saving(self.fig, f"videos/{self.figname}.mp4", 100):
            for tval in np.linspace(0, time, 1000):
                plt.xlim(xlims)
                plt.ylim(ylims)
                plt.xlabel(self.xlabel)
                plt.ylabel(self.ylabel)

                ylist = np.array([])
                match tval:
                    case 0:
                        ylist = xlist * 0
                    case _:
                        ylist = func(xlist, tval)

                l.set_data(xlist, ylist)
                writer.grab_frame()


    def plot_multiple_graphs(self, *args: dict, best_fit=False, ls="None", marker='x', xlims, ylims):
        ax = self.fig.add_subplot(111)
        for arg in args:
            ax.plot(
                arg.keys(),
                arg.values(),
                ls=ls,
                marker=marker,
                markersize=4,
                color='#%06X' % random.randint(0, 0xFFFFFF)
            )
        
            if best_fit:
                self.plot_best_fit(arg.keys(), arg.values())

        ax.set_xlim(xlims)
        ax.set_ylim(ylims)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)

        self.fig.savefig(f"plots/{self.figname}.pdf", dpi=350)