import random
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import time

def random_walk():    
    walker = 0
    final_positions = []

    for _ in range(10000):
        for _ in range(1000):
            match random.randint(0, 1):
                case 0:
                    walker -= 1
                
                case 1:
                    walker += 1
            
        final_positions.append(walker)
        walker = 0
    
    count_positions = {}
    for i in range(min(final_positions), max(final_positions)+1):
        if final_positions.count(i) > 0:
            count_positions[i] = final_positions.count(i)
    
    plt.plot(
        count_positions.keys(),
        count_positions.values(),
        ls="None",
        marker=".",
        markersize=4
    )

    plt.ylim(ymin=0)
    


    plt.show()
