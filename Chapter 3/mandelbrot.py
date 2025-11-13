import numpy
from matplotlib import pylab as plt


def mandelbrot(c,z,iterations):
    colour = 1
    for i in range(iterations):
        z_dash = (z)**2 + c
        z = z_dash
        if numpy.abs(z_dash)>2:
            colour = 0
            break
    return colour

def mandelbrot_iter(c,z,iterations):
    number = 0
    for i in range(iterations):
        z_dash = (z)**2 + c
        z = z_dash
        if numpy.abs(z_dash)>2:
            break
        else:
            number += 1
    return number

def mandelbrot_graph(N,z,iterations):
    grid = numpy.empty([N+1,N+1],int)
    x_axis = numpy.linspace(-2,2,N+1)
    y_axis = numpy.linspace(-2,2,N+1)
    ii = 0
    kk = 0
    for i in x_axis:
        for k in y_axis:
            C_number = complex(i,k)
            value = mandelbrot_iter(C_number,z,iterations)
            grid[ii][kk] = value
            kk += 1
            if kk == N+1:
                ii += 1
                kk  = 0
    plt.imshow(grid,origin="lower", extent=[-2,2,-2,2])
    plt.title('Slice from the Mandlebrot set')
    plt.jet()
    plt.show()

