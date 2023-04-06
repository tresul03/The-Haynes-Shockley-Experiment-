import numpy as np
import random
from plotter import Plotter
from values import Values
from diffusion import Diffusion

class RandomWalk():
    def __init__(self):
        self.xlabel = "Displacement / m"
        self.ylabel = "Frequency"
        self.values = Values() #initialises values
        self.xlist = np.linspace(-1, 1, 500000)
        self.tlist = np.linspace(0.4e-4, 1e-4, 15) 

    def random_walk(self, skew_point: int, decay_prob=0) -> dict: #skew_point is the probability of moving right, decay_prob is the probability of decay
        walker = 0 #initial particle position
        positions = [] #list of final positions reached by each particle

        for _ in range(10000): #10000 particles
            for _ in range(1000): #1000 steps per particle
                match random.randint(0, 100) <= skew_point: #probability of moving right 
                    case False: 
                        walker -= 1
                    case _:
                        walker += 1
            
            if random.randint(0, 100) >= decay_prob:
                positions.append(walker)

            walker = 0 #resets position for next particle
        
        # print(len(positions))
        dict_positions = {} #dictionary of positions and number of particles at that position
        for i in range(min(positions), max(positions)+1):
            if positions.count(i) > 0:
                dict_positions[i] = positions.count(i)

        return dict_positions

    def diffusion(self) -> dict:
        diffusion_1d = lambda x: np.exp(-x**2 / (4*self.values.D)) #diffusion equation
        keys = np.linspace(-1, 1, 1001)
        values = diffusion_1d(keys)

        return dict(zip(keys, values))

