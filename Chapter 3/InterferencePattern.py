import numpy
from matplotlib import pylab

def grid(points,x1,y1):
    spacing = 1/points
    r1 = numpy.empty([points+1,points+1], float)
    for i in range(points+1):
        for j in range(points+1):
            r1[i][j] = numpy.sqrt((i*spacing-y1)**2 + (j*spacing-x1)**2)
    return r1

    
def wave_one(points,x1,y1,amp,wave):
    vector = (2*numpy.pi)/wave
    heights = amp*numpy.sin(vector*grid(points,x1,y1))
    return heights

def wave_two(points,x1,y1,x2,y2,amp,wave):
    first = wave_one(points,x1,y1,amp,wave)
    second = wave_one(points,x2,y2,amp,wave)
    return first + second

    
'''pylab.imshow(grid(1000,0.5,0.5))
pylab.gray()
pylab.show()
pylab.imshow(wave_one(1000,0.4,0.5,0.01,0.05))
pylab.gray()
pylab.show()
pylab.imshow(wave_one(1000,0.6,0.5,0.01,0.05))
pylab.gray()
pylab.show()
pylab.imshow(wave_two(2000,0.1,0.4,0.9,0.7,0.01,0.05),origin = "lower",extent=[0,1,0,1])
pylab.gray()
pylab.show()'''
first = wave_one(1500,0.5,0.2,0.01,0.05)
second = wave_one(1500,0.2,0.5,0.01,0.05)
third  = wave_one(1500,0.8,0.65,0.01,0.05)
total = first+second+third
pylab.imshow(total,origin = "lower",extent=[0,1,0,1])
pylab.gray()
pylab.title('Interference Pattern of Three Waves Interacting')
pylab.show()
