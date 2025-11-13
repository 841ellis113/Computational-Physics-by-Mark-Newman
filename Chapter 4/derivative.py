from numpy import tanh, linspace, cosh
import matplotlib.pyplot as plt

def func(x):
    return 1 + 0.5*(tanh(2*x))

def numerical(x,h):
    half = h/2
    dfdx   = (func(x+half) - func(x-half))/h
    return dfdx

def analytical(x):
    return (1/(cosh(2*x)))**2

def graph_num(a,b,h):
    N = int((b-a)/h)
    xrange = linspace(a,b,N+1)
    ynrange = []
    yarange = []
    for i in xrange:
        ynrange.append(numerical(i,h))
        yarange.append(analytical(i))
    plt.plot(xrange,ynrange,'bx')
    plt.plot(xrange,yarange,'y--')
    plt.show()
    
