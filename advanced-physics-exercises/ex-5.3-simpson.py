from math import exp

def f(t):
    return exp(-1*(t**2))

a = 0.0
b = 3.0
h = 0.01

k = a+h
E = 0

steps = abs(b-a)/h

for i in range(1,int(steps)):
    E += 0.5*h*(f(k-h) + f(k))
    print(k,E)
    k+=h


