from math import exp
from pylab import plot, show


def f(t):
    return exp(-1*(t**2))

a = 0.0
b = 4.0
h = 0.01

k = a+h
E = 0

x = [0]
Es = [0]


steps = abs(b-a)/h

for i in range(1,int(steps)):
    E += 0.5*h*(f(k-h) + f(k))
    print(k,E)
    x.append(k)
    Es.append(E)
    k+=h

plot(x,Es)
show()
