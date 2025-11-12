import math

G_con      = 6.67*10**-11       # Gravitational Constant
pi         = math.pi
MassE      = 5.97*10**24      # mass of the Earth in Kg
RadiusE    = 6371*10**3        # Radius of the Earth in metres

def DayConverter(day):
    seconds = day*3600*24
    return seconds

def Altitude(T):
    height = ((G_con*MassE*(T**2))/(4*pi**2))**(1/3) - RadiusE
    return height

Difference = Altitude(86400) - Altitude(86148)
print(Difference)

    
