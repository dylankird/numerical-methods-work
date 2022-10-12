from math import exp
from pylab import plot,show

def f(x):
    return exp((-2)*x)

def fprime(x):
    return (-2)*exp((-2)*x)

x0=0.5
h=0.1

hs = []
errors = []


for k in range(1,15):
    error = abs(fprime(x0)-(f(x0+h) - f(x0))/h)
    hs.append(h)
    errors.append(error)
    h *= 0.1

plot(hs, errors)
show()
