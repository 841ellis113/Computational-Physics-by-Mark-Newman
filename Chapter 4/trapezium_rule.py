import numpy
from matplotlib import pylab
import math


def trapezium(h,y1,y2):     #calculates the area of a trapezium
    return 0.5*h*(y1+y2)


def function(x):            #function that is being evaluated
    return numpy.sin(x**2 + 2*x)


def derivative(x):          #deriviative of the function defined by function()
    return (4*x**3) - 2

def half_trap_terms(a,b,N):
    total = 0
    h = (b-a)/N
    for i in range(1,N,2):
        total += function(a+(i*h))
        result = total*h
    return result, h
        
def trapezoidal(a,b,N):                     #trapezium rule to numerically calculate integral
    I = 0.5*(function(a) + function(b))     #This use the formula of (0.5)(f(a)+f(b)+ sum(f(xk)))
    h = (b-a)/N                             #This does not compute integral as a sum of trapeziums
    for i in range(1,N):
        I += function(a+(i*h))
    return h*I


def analytical_error(a,b,N):                #Calculates the approximation error of trap method
    h = (b-a)/N                             #Derived from taylor expansion and estimete is to order 1
    fda = derivative(a)                     #error is of h**2 order
    fdb = derivative(b)                     #rounding error due to precision of computer is around 1e-16
    return abs((1/12)*(h**2)*(fda - fdb))   #for approximation error to match that, the trapezoidal rule
                                            #needs about 100 million iterations!

def numerical_error(a,b,N):                 #Returns error based on practical data rather than analytical
    integral_1 = trapezoidal(a,b,int(N/2))  #results. useful when dealing with data sets or points rather 
    integral_2 = trapezoidal(a,b,N)         #than functions. N must be even.
    return abs((integral_2-integral_1)/3)


def adaptive_trap(a,b,N,epsilon):           #Calculate the indefinate integral between points and b
    Initial = trapezoidal(a,b,N)
    error = 1
    M = 2*N
    while error > epsilon:
        h    = (b-a)/M
        half = half_trap_terms(a,b,M)
        Inext = (0.5)*Initial + half
        error = abs((1/3)*(Inext-Initial))
        Initial = Inext
        M = 2*M
    return Inext               
    
def Romberg(a,b,N,epsilon):           #Calculate the indefinate integral between points and b
    Initial = trapezoidal(a,b,N)
    second  = 0
    error = 1
    M = 2*N
    while error > epsilon:
        h    = (b-a)/M
        half = half_trap_terms(a,b,M)
        Inext = (0.5)*Initial + half
        error = abs((1/3)*(Inext-Initial))
        Initial = Inext
        M = 2*M
    return Inext 
