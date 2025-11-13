import numpy
from matplotlib import pylab

def feigenbaum(r,x,iterations):
    x_values = []
    r_value  = []
    for i in range(iterations):
        value = r*x*(1-x)
        x = value
        if i > 1500:
            x_values.append(x)
            r_value.append(r)
    return r_value, x_values
    
def range_feigenbaum(x0,iterations):
    for r in numpy.linspace(0,4,401):
        values = feigenbaum(r,x0,iterations)
        pylab.plot(values[0],values[1],"k.", markersize = 0.1)
    pylab.ylim(0,1)
    pylab.xlim(0,4)
    pylab.title('The Logistic Map Transitioning to Chaos')
    pylab.show()
    
range_feigenbaum(0.5,2000)



