#This is a test script to check different lines of code

import math

def transmission_prob(E,M,V):                               #inputs are energy of particle, mass and potential barrier energy
    energy    = E * 1.60218e-19
    potential = V * 1.60218e-19
    bar       = 1.054571817e-34
    k1      = math.sqrt(2*M*energy)/bar                 #Wavevector k1
    k2      = math.sqrt(2*M*(energy - potential))/bar   #wavevector k2
    transmission = (4*k1*k2)/((k1 + k2)**2)
    reflection   = ((k1 - k2)/(k1 + k2))**2

    return round(transmission,2), round(reflection,2)
