#Approximates a sin function using taylor polynomial

from math import pi, factorial
from pylab import plot, show

a = 0
b = pi

h = 0.1

def fnpoly(x):
    Sum = x
    sign = -1
    for k in range(3,17,2):
        Sum += sign * x**k/factorial(k)
        sign *= -1
    return Sum

t = []
y = []

for k in range(0,int((b-a)/h)+1):
    #print(a + k*h)
    t.append(a + k*h)
    y.append(fnpoly(a + k*h))

print(y)

plot(t,y)
show()
