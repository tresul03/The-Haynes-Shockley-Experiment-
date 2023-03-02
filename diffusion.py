import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from matplotlib.animation import FFMpegWriter
plt.rcParams["animation.ffmpeg_path"] = "C:\\ffmpeg\\bin\\ffmpeg.exe"

MOBILITY = 1e-1
K = 1.38e-23
T = 300
Q = 1.6e-19

v = 0.1

D = (MOBILITY*K*T)/Q

fig = plt.figure()
l, = plt.plot([], [], ls="-", color="red")

plt.xlim(-0.5, 0.5)
plt.ylim(0, 20)

normaliser = lambda t: (np.sqrt(4*np.pi*D*t)) **-1
diffusion_1d = lambda x, t: np.exp(-x**2 / (4*D*t))
diffusion_drift_1d = lambda x, t: np.exp(-(x - v*t)**2 / (4*D*t))

metadata = dict(title="Diffusion", artist="Resul Teymuroglu")
writer = FFMpegWriter(fps=100, metadata=metadata)

xlist = np.linspace(-1, 1, 1000)
ylist = np.zeros(1000)

with writer.saving(fig, "diffusion.mp4", 100):
    for tval in np.linspace(0, 10, 1000):
        match tval:
            case 0:
                ylist = xlist * 0
            case _:
                ylist = normaliser(tval) * diffusion_1d(xlist, tval)

        plt.xlabel("Displacement / m")
        plt.ylabel("Charge Carrier Population")

        l.set_data(xlist, ylist)
        writer.grab_frame()
        ylist = np.array([])

with writer.saving(fig, "diffusion_with_drift.mp4", 100):
    for tval in np.linspace(0, 10, 1000):
        match tval:
            case 0:
                ylist = xlist * 0
            case _:
                ylist = normaliser(tval) * diffusion_1d(xlist, tval)
                        
        plt.xlabel("Displacement / m")
        plt.ylabel("Charge Carrier Population")

        l.set_data(xlist, ylist)
        writer.grab_frame()
        ylist = np.array([])

#! the lambda functions are encountering division by zero, but they're only used if tval != 0