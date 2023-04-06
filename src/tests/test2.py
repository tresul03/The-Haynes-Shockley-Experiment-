import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.cm import ScalarMappable
from random_walk import RandomWalk
import matplotlib.colors as mcolors
from diffusion import Diffusion

randomer = RandomWalk()
diffusion = Diffusion()
dict4 = [dict(zip(randomer.xlist, diffusion.diffusion_decay_1d(randomer.xlist, tval))) for tval in randomer.tlist]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

# Create the colormap and ScalarMappable
# give a list of colours for colourmap
cmap = LinearSegmentedColormap.from_list("mycmap", ["#0000ff", "#00ff00", "#ffff00", "#ff0000"][::-1])

sm = ScalarMappable(cmap=cmap)
sm.set_clim(vmin=min(randomer.tlist), vmax=max(randomer.tlist))

for i, arg in enumerate(dict4):
    ax.plot(
        list(arg.keys()),
        list(arg.values()) / max(dict4[0].values()),
        ls='-',
        color=sm.to_rgba(randomer.tlist[i]),
        marker='None'
    )

#make a colorbar
cbar = fig.colorbar(sm)
cbar.set_label("Time / s", rotation=270, labelpad=15)

ax.set_xlabel("Displacement / $\mu$m")
ax.set_ylabel("Charge Carrier Concentration / $n_{0}$")
ax.set_xlim(-0.0025, 0.0025)
ax.set_ylim(0, 1)

fig.tight_layout()
fig.savefig("plots/decay-static2.pdf", dpi=350)
