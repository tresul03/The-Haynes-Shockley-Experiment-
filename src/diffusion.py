import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
plt.rcParams["animation.ffmpeg_path"] = "C:\\ffmpeg\\bin\\ffmpeg.exe"
import time

t0 = time.time()

MOBILITY = 1e-1     #Charge Carrier Mobility
BARLENGTH = 950e-6  #Length of Semiconductor
VOLTAGE = 6e-2      #Voltage across semiconductor
K = 1.38e-23        #Boltzmann's Constant
T = 300             #Temperature
Q = 1.6e-19         #Electron Charge
TAU = 10e-6         #Charge Carrier Lifetime
CARRIER_CONC = 1e14 #Charge Carrier Concentration

v = (MOBILITY * VOLTAGE) / BARLENGTH    #Charge Carrier Drift Velocity
D = (MOBILITY*K*T)/Q                    #Diffusion Constant

fig = plt.figure()
l, = plt.plot([], [], ls="-", color="red")

plt.xlim(-0.5, 0.5)
plt.ylim(0, 50)

normaliser = lambda t: (np.sqrt(4*np.pi*D*t)) **-1 #ensures probability of finding charge carrier anywhere in semiconductor = 1
diffusion_1d = lambda x, t: np.exp(-x**2 / (4*D*t)) #term for modelling diffusion among minority charge carriers in semiconductor
diffusion_drift_1d = lambda x, t: np.exp(-(x - v*t)**2 / (4*D*t)) #same term as above, but for when an electric field is applied across the semiconductor
decay = lambda t: np.exp(-t/TAU) #exponential decay due to the recombination of holes in semiconductor with electrons


metadata = dict(title="Diffusion", artist="Resul Teymuroglu")
writer = FFMpegWriter(fps=100, metadata=metadata)

xlist = np.linspace(-1, 1, 50001)
ylist = np.zeros(50001)

xlabel, ylabel = "Displacement / m", "Charge Carrier Concentration / $n_{0}$" 

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
    for tval in np.linspace(0, 0.1, 1000):
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

#charge carrier diffusion + decay + drift:
with writer.saving(fig, "plots/diffusion_with_decay.mp4", 100):
    plt.xlim(-0.002, 0.002)
    for tval in np.linspace(0, 1.5e-4, 1000):
        match tval:
            case 0:
                ylist = xlist * 0
            case _:
                ylist = decay(tval) * normaliser(tval) * diffusion_drift_1d(xlist, tval)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)


        l.set_data(xlist, ylist)
        writer.grab_frame()
        ylist = np.array([])

print("Sim 3 done.")
print(f"Runtime: {time.time() - t0}")
