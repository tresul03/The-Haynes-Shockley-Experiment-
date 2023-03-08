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
carrier_conc = 1e14 #Charge Carrier Concentration

D = (MOBILITY*K*T)/Q        #Diffusion Constant

fig = plt.figure()
l, = plt.plot([], [], ls="-", color="red")

plt.xlim(-0.5, 0.5)
plt.ylim(0, 20)

normaliser = lambda t: (np.sqrt(4*np.pi*D*t)) **-1 #ensures probability of finding charge carrier anywhere in semiconductor = 1
diffusion_1d = lambda x, t: np.exp(-x**2 / (4*D*t)) #term for modelling diffusion among minority charge carriers in semiconductor
diffusion_drift_1d = lambda x, t: np.exp(-(x - v*t)**2 / (4*D*t)) #same term as above, but for when an electric field is applied across the semiconductor
decay = lambda t: np.exp(-t/tau)


metadata = dict(title="Diffusion", artist="Resul Teymuroglu")
writer = FFMpegWriter(fps=100, metadata=metadata)

xlist = np.linspace(-1, 1, 10000)
ylist = np.zeros(10000)

xlabel, ylabel = "Displacement / m", "Charge Carrier Concentration" 

# charge carrier diffusion:
with writer.saving(fig, "plots/diffusion.mp4", 100):
    for tval in np.linspace(0, 10, 1000):
        match tval:
            case 0:
                ylist = xlist * 0
            case _:
                ylist = normaliser(tval) * diffusion_1d(xlist, tval)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        l.set_data(xlist, ylist)
        writer.grab_frame()
        ylist = np.array([])
print("Sim 1 done.")

#charge carrier diffusion + drift
with writer.saving(fig, "plots/diffusion_with_drift.mp4", 100):
    for tval in np.linspace(0, 10, 1000):
        match tval:
            case 0:
                ylist = xlist * 0
            case _:
                ylist = normaliser(tval) * diffusion_drift_1d(xlist, tval)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        l.set_data(xlist, ylist)
        writer.grab_frame()
        ylist = np.array([])
print("Sim 2 done.")

#charge carrier diffusion + decay:
with writer.saving(fig, "plots/diffusion_with_decay.mp4", 100):
    plt.xlim(-0.01, 0.01)
    plt.ylim(0, 0.5)
    for tval in np.linspace(0, 1e-3, 1000):
        match tval:
            case 0:
                ylist = xlist * 0
            case _:
                ylist = decay(tval) * normaliser(tval) * diffusion_1d(xlist, tval)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)


        l.set_data(xlist, ylist)
        writer.grab_frame()
        ylist = np.array([])
