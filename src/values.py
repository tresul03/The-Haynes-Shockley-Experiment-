class Values:
    def __init__(self):
        self.MOBILITY = 4e-2                                        #Charge Carrier Mobility
        self.BARLENGTH = 950e-6                                     #Length of Semiconductor
        self.VOLTAGE = 6                                            #Voltage across semiconductor
        self.K = 1.38e-23                                           #Boltzmann's Constant
        self.T = 300                                                #Temperature
        self.Q = 1.6e-19                                            #Electron Charge
        self.TAU = 1e-6                                             #Charge Carrier Lifetime
        self.v = (self.MOBILITY * self.VOLTAGE) / self.BARLENGTH    #Charge Carrier Drift Velocity
        self.D = (self.MOBILITY*self.K*self.T)/self.Q               #Diffusion Constant
