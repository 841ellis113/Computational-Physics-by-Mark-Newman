# This calculates the time it takes for a ball to fall a given height, h under the Earth's Gravitational field (ignoring air resistance)
# This uses the equations of motion and assumes the initial velocity of the ball to be 0 as it is dropped
from math import sqrt as sqt

g      = 9.81 #m/(s**2)

height = float(input("Enter the height from which the ball is dropped:")) #m
V0     = float(input("Enter the initial velocity of the ball:"))        #m/s

delta  = V0**2 - (-2*g*height)

if delta <=0:
    print("Thses initail conditions don't have a real solution")
else:
    time1 = (-V0 + sqt(delta))/(g)
    time2 = (-V0 - sqt(delta))/(g)
    if time1 < 0:
        time = time2
    else:
        time = time1
    print(f"Time taken for a ball to drop {height}m with initial velocity {V0}m/s is {round(time,2)}s")
