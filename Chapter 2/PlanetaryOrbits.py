import math

def orbit(V1,L1):
    G = 6.6738e-11
    M = 1.9891e30
    B = -(2*G*M)/(V1*L1)
    C = -(V1**2 - (2*G*M)/L1)
    #delta = B**2 -(4*1*C)
    V2 = (-B - math.sqrt(B**2 -(4*1*C)))/2
    L2 = (V1*L1)/V2
    semi_major, semi_minor = 0.5*(L1+L2), math.sqrt(L1*L2)
    period = (2*math.pi*semi_major*semi_minor)/(L1*V1)
    eccentricity = (L2-L1)/(L2+L1)
    return V2, L2, period, eccentricity

LL = 8.7830e10
VV = 5.4529e4
results = orbit(VV,LL)
period_year = round(results[2]/31449600,1)

print(f"Velocity at Perihelion: {VV} (m/s)\nDistance at Perihelion: {LL} (m)")
print(f"Velocity at Aphelion: {round(results[0],1)} (m/s)\nDistnace at Aphelion: {round(results[1],1)} (m)")
print(f"Period of orbit: {period_year} (years)\nEccentricity: {round(results[3],3)}")
