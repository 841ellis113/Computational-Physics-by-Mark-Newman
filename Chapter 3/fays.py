from numpy import sin as SIN
from numpy import cos as COS
from numpy import pi as PI
from numpy import exp as EXP
import numpy
from matplotlib import pylab

'''end = 24*PI'''

def radians(points,end):                    #Split the range 0-2pi into given number of points
    interval = numpy.linspace(0,end,points)
    return interval

def r_values(points,end):
    theta = radians(points,end)
    term1 = EXP(COS(theta))
    term2 = 2*COS(4*theta)
    term3 = (SIN(theta/12))**5
    return (term1 -term2 +term3)

def Fays_funct(points,end):
    angle_interval = radians(points,end)
    RValue_interval = r_values(points,end)
    x_values = RValue_interval*numpy.cos(angle_interval)
    y_values = RValue_interval*numpy.sin(angle_interval)
    pylab.plot(x_values,y_values)
    pylab.show()


    
