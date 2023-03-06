import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
plt.rcParams["animation.ffmpeg_path"] = "C:\\ffmpeg\\bin\\ffmpeg.exe"

MOBILITY = 1e-1
K = 1.38e-23        #Boltzmann's Constant
T = 300             #Temperature
Q = 1.6e-19         #Electron Charge
tau = 10e-6         #Charge Carrier Lifetime
v = 0.1             #Charge Carrier Drift Velocity

D = (MOBILITY*K*T)/Q        #Diffusion Constant

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

#charge carrier diffusion:
with writer.saving(fig, "plots/diffusion.mp4", 100):
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

#charge carrier diffusion with drift
with writer.saving(fig, "plots/diffusion_with_drift.mp4", 100):
    for tval in np.linspace(0, 10, 1000):
        match tval:
            case 0:
                ylist = xlist * 0
            case _:
                ylist = normaliser(tval) * diffusion_drift_1d(xlist, tval)
                        
        plt.xlabel("Displacement / m")
        plt.ylabel("Charge Carrier Population")

        l.set_data(xlist, ylist)
        writer.grab_frame()
        ylist = np.array([])


#todo: do another simulation accounting for carrier lifetime