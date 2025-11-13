from numpy import sin as SIN
from numpy import cos as COS
from numpy import pi as PI
import numpy
from matplotlib import pylab

def radians(points,end):                    #Split the range 0-2pi into given number of points
    interval = numpy.linspace(0,end,points)
    return interval

def r_values(points,end):
    values = radians(points,end)**2
    return values

def Galilen_spiral(points,end):
    angle_interval = radians(points,end)
    RValue_interval = r_values(points,end)
    x_values = RValue_interval*numpy.cos(angle_interval)
    y_values = RValue_interval*numpy.sin(angle_interval)
    pylab.plot(x_values,y_values)
    pylab.show()


    
