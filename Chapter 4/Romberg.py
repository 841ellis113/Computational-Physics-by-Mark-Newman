import numpy
from matplotlib import pylab
import math

def function(x):            
    term = x
    return term

def trapezoidal(a,b,N):                     
    I = 0.5*(function(a) + function(b))     
    h = (b-a)/N                             
    for i in range(1,N):
        I += function(a+(i*h))
    return h*I

def half_trap_terms(a,b,N):
    total = 0
    h = (b-a)/(N)
    for i in range(1,N,2):
        total += function(a+(i*h))
        result = total*h
    return result
        
def Romberg_eqn(Rl,Ru,m):
    return Rl + (1/((4**m)-1)*(Rl - Ru))

def Romberg_error(Rl,Ru,m):
    return (1/((4**m)-1)*(Rl - Ru))

def Romberg_int(a,b,N,epsilon):
    M = 1
    error = 1
    upper = []
    upper.append(trapezoidal(a,b,N))
    N = 2*N
    lower = []
    lower.append(upper[0]*0.5 + half_trap_terms(a,b,N))
    lower.append(Romberg_eqn(lower[0],upper[0],M))
    while error > epsilon:
        upper = lower.copy()
        lower = []
        N = 2*N
        M +=1
        lower.append(upper[0]*0.5 + half_trap_terms(a,b,N))
        for i in range(1,M+1,1):
            lower.append(Romberg_eqn(lower[i-1],upper[i-1],(i)))
        error = abs(Romberg_error(lower[-2],upper[-1],M))
    return lower[-1]

      
