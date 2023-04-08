import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.optimize import curve_fit
from matplotlib.animation import FFMpegWriter
plt.rcParams["animation.ffmpeg_path"] = "C:\\ffmpeg\\bin\\ffmpeg.exe"
plt.rcParams['font.size'] = 17

class Plotter():
    def __init__(self, xlabel: str, ylabel: str, figname: str): #initialises plotter
        self.xlabel = xlabel        #label of x-axis
        self.ylabel = ylabel        #label of y-axis
        self.figname = figname      #name of plot
        self.fig = plt.figure(figsize=(10, 7))     #initialising figure
        self.hex_const = "#%06X"
        self.color = self.hex_const % random.randint(0, 0xFFFFFF)


    def generate_random_color(self, color1):
        """
        Generates a random colour with a contrast ratio > 3.
        """

        color2 = '#%06X' % random.randint(0, 0xFFFFFF)

        # Convert hex color values to RGB values
        r1, g1, b1 = tuple(int(color1.strip('#')[i:i+2], 16) for i in (0, 2, 4))
        r2, g2, b2 = tuple(int(color2.strip('#')[i:i+2], 16) for i in (0, 2, 4))
        
        # Calculate the luminance of each color using the formula from the W3C's
        # Web Content Accessibility Guidelines (WCAG)
        L1 = 0.2126 * r1 + 0.7152 * g1 + 0.0722 * b1
        L2 = 0.2126 * r2 + 0.7152 * g2 + 0.0722 * b2
        
        # Calculate the contrast ratio using the formula from the WCAG
        if L1 > L2:
            ratio = (L1 + 0.05) / (L2 + 0.05)
        else:
            ratio = (L2 + 0.05) / (L1 + 0.05)

        return color2 if ratio > 3 else self.generate_random_color(color1)


    def plot_graph(self, xlist, ylist, xlims, ylims, ls="None", marker='x', label=None, best_fit=False): #plots a graph
        ax = self.fig.add_subplot(111)
        ax.plot(
            xlist,
            ylist,
            ls=ls,
            marker=marker,
            markersize=4,
            color=self.color,
            label=label
        )

        if best_fit != False:
            self.plot_best_fit(ax, xlist, ylist, best_fit)

        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_xlim(xlims)
        ax.set_ylim(ylims)

        self.fig.tight_layout()
        self.fig.savefig(f"plots/{self.figname}.png", dpi=350)


    def plot_best_fit(self, ax, xlist, ylist, type): #plots a best fit line on a graph
        #convert xlist and ylist to lists to avoid error
        xlist = np.array(list(xlist))
        ylist = np.array(list(ylist))

        match type.lower():
            case "linear":
                func = lambda x, m, c: m*x + c
            
            case "exponential":
                func = lambda x, a, b, c: a*np.exp(-b*(x**2))+c
        
            case _:
                raise ValueError("Invalid type of best fit line")

        popt = curve_fit(func, xlist, ylist)[0]

        ax.plot(
            xlist,
            func(xlist, *popt),
            ls='--',
            color=self.generate_random_color(self.color)
        )


    def plot_multiple_plots(self, n, *args: dict, best_fit=False): #plots multiple graphs on the same figure
        assert len(args) == n, "Number of arguments must equal number of graphs to be plotted"
        
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
                color=self.color
            )

            if best_fit != False:
                self.plot_best_fit(ax, arg.keys(), arg.values(), best_fit)

            ax.set_xlabel(self.xlabel)
            ax.set_ylabel(self.ylabel)

            # Generate a random color that has a contrast ratio of at least 3
            self.color = self.generate_random_color(self.color)

        self.fig.tight_layout()
        self.fig.savefig(f"plots/{self.figname}.png", dpi=350)


    def plot_multiple_graphs(self, *args: dict, best_fit=False, ls="None", marker='x', xlims, ylims, labels: list): # plots multiple graphs on the same plot
        assert len(args) == len(labels), "Number of arguments must equal number of graphs to be plotted"

        ax = self.fig.add_subplot(111)
        for i in range(len(args)):
            ax.plot(
                args[i].keys(),
                args[i].values(),
                ls=ls,
                marker=marker,
                markersize=4,
                color=self.color,
                label=labels[i]
            )
        
            if best_fit != False:
                self.plot_best_fit(ax, args[i].keys(), args[i].values(), best_fit)

            # Generate a random color that has a contrast ratio of at least 3
            self.color = self.generate_random_color(self.color)

        ax.set_xlim(xlims)
        ax.set_ylim(ylims)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.legend(loc=1,fontsize=12)

        self.fig.tight_layout()
        self.fig.savefig(f"plots/{self.figname}.png", dpi=350)


    def animate(self, xlist, func, time, xlims, ylims): # xlist is the x-axis, func is the function to be animated, time is the time to animate over
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
                        ylist = func(xlist, tval) / max(func(xlist, np.linspace(0, time, 1000)[1])) #normalises the function

                l.set_data(xlist, ylist) #updates the plot
                writer.grab_frame() #saves the frame

