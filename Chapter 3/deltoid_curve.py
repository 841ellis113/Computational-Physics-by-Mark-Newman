from numpy import sin as SIN
from numpy import cos as COS
from numpy import pi as PI
import numpy
from matplotlib import pylab

def deltoid_x(theta):                   #Calculates the x coord from angle, r = 1
    x = 2*COS(theta) + COS(2*theta)
    return x

def deltoid_y(theta):                   #Calculates the y coord from angle, r = 1
    y = 2*SIN(theta) - SIN(2*theta)
    return y

def radians(points):                    #Split the range 0-2pi into given number of points
    interval = numpy.linspace(0,2*PI,points)
    return interval

def deltoid_data(points):
    angle_interval = radians(points)
    x_values = deltoid_x(angle_interval)
    y_values = deltoid_y(angle_interval)
    pylab.plot(x_values,y_values)
    pylab.show()


    
