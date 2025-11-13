from numpy import ones,copy,cos,tan,pi,linspace,exp
import matplotlib.pyplot as plt

V     = 0.001
kb    = 1.380649e-23
Db    = 428
rho   = 6.022e28
points = 50

def integrand(x):
    term = ((x**4)*(exp(x)))/((exp(x)-1)**2)
    return term

def gaussxw(N):
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)
    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

def gaussian_quadrature(N,a,b):
    total = 0
    points,weights = gaussxwab(N,a,b)
    for i in range(N):
        total += weights[i]*integrand(points[i])
    return total

def Heat_capacity(T):
    TDb           = T/Db
    limb          = 1/TDb
    lima          = 0
    constant_term = 9*V*rho*kb*(TDb**3)
    cv            = constant_term*gaussian_quadrature(points,lima,limb)
    return cv

def CV_range(T0,T1,M):
    xaxis    = list(linspace(T0,T1,M))
    yaxis    = []
    for t in xaxis:
        yaxis.append(Heat_capacity(t))
    plt.plot(xaxis,yaxis)
    plt.xlabel('Temperature / K')
    plt.ylabel('Heat capacity / (J/K)')
    plt.title('Debye Model of Heat Capacity of Solid Aluminium')
    plt.show()
