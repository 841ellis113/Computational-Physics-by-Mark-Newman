import numpy
from matplotlib import pylab
import math


def integrand(x,m,theta):
    phi = (m*theta - x*numpy.sin(theta))
    result = numpy.cos(phi)
    return result

def bessel_m(theta_a,theta_b,x,m,N):
    sum_even = 0
    sum_odd = 0
    h = (theta_b-theta_a)/N
    fa = integrand(x,m,theta_a)
    fb = integrand(x,m,theta_b)
    for i in range(1,N,2):
        sum_odd += integrand(x,m,theta_a+h*i)
        if i +1 !=N:
            sum_even += integrand(x,m,(theta_a+(i+1)*h))
        else:
            continue
    return (1/(numpy.pi*3))*(h)*(fa + fb + 4*sum_odd + 2*sum_even)

    
def bessel_plot(theta_a,theta_b):
    N = 1000
    m = [0,1,2]
    results = []
    xvalues = numpy.linspace(0,20,201)
    for i in m:
        for j in xvalues:
            results.append(bessel_m(theta_a,theta_b,j,i,N))
        pylab.plot(xvalues,results)
        results=[]
    pylab.show()
        
def intensity(wavelength,x,y):
    k = (2*numpy.pi)/wavelength
    r  = numpy.sqrt(x**2 + y**2)
    if r == 0:
        intense = (0.5)**2
    else:
        intense = (bessel_m(0,numpy.pi,k*r,1,1000)/(k*r))**2
    return intense



space = (1e-6 - -1e-6)/150

I_values = numpy.empty([151,151],float)

for i in range(151):
    for j in range(151):
        x = -1e-6 + i*space
        y = -1e-6 + j*space
        result = intensity(500e-9,x,y)
        I_values[i][j] = result
pylab.imshow(I_values,vmax=0.01)
pylab.title('Airy Disc Caused by Diffraction')
pylab.show()

