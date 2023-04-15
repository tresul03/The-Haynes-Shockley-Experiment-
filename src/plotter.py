# Author: Resul Teymuroglu
# Date: 8/4/2023
# Description: This file contains the Plotter class, which prodcues plots, animations, and other types of figures the user requests for in the Brains class.

from matplotlib.cm import ScalarMappable
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.optimize import curve_fit
from matplotlib.animation import FFMpegWriter
plt.rcParams["animation.ffmpeg_path"] = "C:\\ffmpeg\\bin\\ffmpeg.exe"
plt.rcParams['font.size'] = 17

class Plotter():
    def __init__(self, xlabel: str, ylabel: str, figname: str):
        """
        Parameters:
        -----------
        xlabel : str
            The label of the x-axis.
        ylabel : str
            The label of the y-axis.
        figname : str
            The name of the plot.
            
        Attributes:
        -----------
        xlabel : str
            The label of the x-axis.
        ylabel : str
            The label of the y-axis.
        figname : str
            The name of the plot.
        fig : matplotlib.figure.Figure
            The figure object.
        hex_const : str
            The hexadecimal constant.
        color : str
            The color of the plot.

        """

        self.xlabel = xlabel                                            #label of x-axis
        self.ylabel = ylabel                                            #label of y-axis
        self.figname = figname                                          #name of plot
        self.fig = plt.figure(figsize=(10, 7))                          #initialising figure
        self.hex_const = "#%06X"                                        #hexadecimal constant
        self.color = self.hex_const % random.randint(0, 0xFFFFFF)       #random colour for graph
        self.ax = self.fig.add_subplot(111)


    def generate_random_color(self, color1):
        """
        Generates a random color that has a contrast ratio of at least 3 with
        the color passed as an argument.

        Parameters:
        -----------
        color1 : str
            The color to compare the generated color to.

        Returns:
        --------
        color2 : str
            The generated color.
        """

        # Generate a random hex color value
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

        # If the contrast ratio is less than 3, generate a new color
        return color2 if ratio > 3 else self.generate_random_color(color1)


    def plot_best_fit(self, ax, xlist, ylist, type, best_fit_label):
        """
        Plots a best fit line on the given axis.

        Parameters:
        -----------
        ax : matplotlib.axes._subplots.AxesSubplot
            The axis to plot the best fit line on.
        xlist : list
            The list of x values.
        ylist : list
            The list of y values.
        type : str
            The type of best fit line to be plotted. The options are "linear" and "exponential".
        """

        #convert xlist and ylist to lists to avoid error
        xlist = np.array(list(xlist))
        ylist = np.array(list(ylist))

        match type.lower():
            case "linear":
                func = lambda x, m, c: m*x + c

            case "gaussian":
                func = lambda x, a, b, c: a * np.exp(-((x-b)/c)**2)
            
            case "decay":
                func = lambda x, t, a, b, c, d: a * np.exp(-((x-b)/c)**2) * np.exp(-t/d)


            case _:
                raise ValueError("Invalid type of best fit line")

        popt = curve_fit(func, xlist, ylist)[0]

        ax.plot(
            xlist,
            func(xlist, *popt),
            ls='--',
            label=f"Best fit line ({type})" if best_fit_label else None,
            color=self.generate_random_color(self.color)
        )


    def add_colourbar(self, zlist):
        cmap = LinearSegmentedColormap.from_list("mycmap", ["#0000ff", "#00ff00", "#ffff00", "#ff0000"][::-1])
        sm = ScalarMappable(cmap=cmap)
        sm.set_clim(vmin=min(zlist), vmax=max(zlist))

        return sm


    def plot_multiple_subplots(self, n, *args: dict, best_fit=False, best_fit_label=False): #plots multiple graphs on the same figure
        """
        Plots multiple graphs on the same figure with the given data and optional best-fit lines.

        Parameters:
        -----------
        n : int
            The number of graphs to be plotted.
        *args : dict
            The dictionary arguments containing the x and y values of each plot.
        best_fit : str, optional
            The type of best fit line to be plotted. The options are "linear" and "exponential". If False, no best-fit line will be plotted. Default is False.
        
        Raises:
        -------
        AssertionError
            If the number of arguments is not equal to the number of graphs to be plotted.

        """

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
                self.plot_best_fit(ax, arg.keys(), arg.values(), best_fit, best_fit_label)

            ax.set_xlabel(self.xlabel)
            ax.set_ylabel(self.ylabel)

            # Generate a random color that has a contrast ratio of at least 3
            self.color = self.generate_random_color(self.color)

        self.fig.tight_layout()
        self.fig.savefig(f"plots/{self.figname}.png", dpi=350)


    def plot_graph(self, *args: dict, labels:list=None, best_fit=False, ls="None", marker='x', xlims=None, ylims=None, best_fit_label=False, zlist=None, zlabel=None, colourbar:bool=False): # plots multiple graphs on the same plot
        """
        Plots multiple graphs on the same plot with the given data and optional best-fit lines.

        Parameters:
        -----------
        *args : dict
            The dictionary arguments containing the x and y values of each plot.
        best_fit : str, optional
            The type of best-fit line to be plotted. The options are "linear" and "exponential". 
            If False, no best-fit line will be plotted. Default is False.
        ls : str, optional
            The line style of the plot. Default is "None".
        marker : str, optional
            The marker style of the plot. Default is "x".
        xlims : tuple
            A tuple of the lower and upper limits of the x-axis.
        ylims : tuple
            A tuple of the lower and upper limits of the y-axis.
        labels : list
            A list of strings that represents the labels for each plot.
        best_fit_label : bool
            If True, the best-fit line will be labelled. Default is False.

        """

        for i in range(len(args)):
            sm = self.add_colourbar(zlist) if colourbar else None

            self.ax.plot(
                args[i].keys(),
                args[i].values(),
                ls=ls,
                marker=marker,
                markersize=4,
                color=self.color if not colourbar else sm.to_rgba(zlist[i]),
                label=labels[i] if labels != None else None
            )
        
            if best_fit != False:
                self.plot_best_fit(self.ax, args[i].keys(), args[i].values(), best_fit, best_fit_label)

            # Generate a random color that has a contrast ratio of at least 3
            self.color = self.generate_random_color(self.color) if not colourbar else self.color

        self.ax.set_xlim(xlims if xlims != None else (min(min(list(arg.keys())) for arg in args), max(max(list(arg.keys()) for arg in args)))) # set x-axis limits
        self.ax.set_ylim(ylims if ylims != None else (min(min(list(arg.values())) for arg in args), max(max(list(arg.values()) for arg in args)))) # set y-axis limits
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)
        self.ax.legend(loc=1) if labels != None else None

        if colourbar:
            cbar = self.fig.colorbar(sm)
            cbar.set_label(zlabel, rotation=270, labelpad=15)

        self.fig.tight_layout()
        self.fig.savefig(f"plots/{self.figname}.png", dpi=350)


    def animate(self, xlist, func, time, xlims, ylims): # xlist is the x-axis, func is the function to be animated, time is the time to animate over
        """
        Animates a function over time with the given x and y data, total time to animate, and axis limits.

        Parameters:
        -----------
        xlist : list or array
            The x-values of the data to be plotted.
        func : function
            A function that takes x and t as inputs and returns y values.
        time : float
            The total time to animate the function over.
        xlims : tuple
            A tuple of the lower and upper limits of the x-axis.
        ylims : tuple
            A tuple of the lower and upper limits of the y-axis.

        """

        metadata = dict(title="Diffusion", artist="Resul Teymuroglu")
        writer = FFMpegWriter(fps=100, metadata=metadata)
        l, = self.ax.plot([], [], ls="-", color="red")
        tlist = np.linspace(0, time, 1000)

        self.ax.set_xlim(xlims)
        self.ax.set_ylim(ylims)
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)

        with writer.saving(self.fig, f"videos/{self.figname}.mp4", 100):
            for tval in tlist:

                ylist = np.array([])
                match tval:
                    case 0:
                        ylist = xlist * 0
                    case _:
                        ylist = func(xlist, tval) / max(func(xlist, tlist[1])) #normalises the function

                l.set_data(xlist, ylist) #updates the plot
                writer.grab_frame() #saves the frame
