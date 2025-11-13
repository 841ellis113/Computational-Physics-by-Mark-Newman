import numpy
import math

#########################################################################################################

def function(x):                #function on which Simpson's rule calculates integral
    return (x**2 + 2*x)c

#########################################################################################################

def simpsons(a,b):              #Calculates the area of a slice using Simpson's rule              
    h = (b-a)/2             
    f0= function(a+h)
    f1= function(a)
    f2 = function(b)
    area = (1/3)*h*(f1+f2+4*f0)
    return area


def simpsons_numerical(Xa,Xb,N):                        #calculates integral by summing up
    total = 0                                           #many slices calculated using Simpson's
    width     = (Xb-Xa)/N                               #rule
    for i in range(int(N/2)):
        total += simpsons(Xa+2*i*width,Xa+2*(i+1)*width)
    return total
        
def simpsons_analytical(Xa,Xb,N):                       #Calculates the integral using analytical
    sum_even = 0                                        #result for simpsons rule
    sum_odd = 0                                         #for the error on Simpson's rule to equal
    h = (Xb-Xa)/N                                       #machine error, N is about 10000
    fa = function(Xa)
    fb = function(Xb)
    for i in range(1,N,2):
        sum_odd += function(Xa+h*i)
        if i +1 !=N:
            sum_even += function(Xa+(i+1)*h)
        else:
            continue
    return (1/3)*(h)*(fa + fb + 4*sum_odd + 2*sum_even)

#########################################################################################################

def error(a,b,N):                                       #Calculates error using numerical methods
    I1 = simpsons_analytical(a,b,int(N/2))
    I2 = simpsons_analytical(a,b,N)
    return abs((1/15)*(I2-I1))


def adaptive_term(a,b,N):                                                               
    sum_odd = 0                                         
    h = (b-a)/N
    for i in range(1,N,2):
        sum_odd += function(a+h*i)
    return (2/3)*(sum_odd),h

def adaptive_simpson(a,b,N,epsilon):
    even = 0                                        #result for simpsons rule
    odd = 0
    error = 1
    h = (b-a)/N                                       
    fa = function(a)
    fb = function(b)
    for i in range(1,N,2):
        odd += function(a+h*i)
        if i +1 !=N:
            even += function(a+(i+1)*h)
        else:
            continue
    sum_odd = (2/3)*odd
    sum_even = fa + fb + even
    integral1 = h*(2*sum_odd + sum_even)
    while error > epsilon:
        N = 2*N
        sum_even = sum_odd + sum_even
        terms = adaptive_term(a,b,N)
        sum_odd = terms[0]
        h = terms[1]
        integral2 = h*(sum_even + 2*sum_odd)
        error = abs((integral2 - integral1)/15)
        integral1 = integral2
        print(error,integral1,N)
    return integral1
        



        
