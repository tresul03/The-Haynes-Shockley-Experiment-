class Values:
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

