from math import log,exp

def f(x):
    return exp(x)+x-7

def fPrime(x):
    return exp(x)+1

def g(x):
    return x - f(x)/fPrime(x)


x = 1.0

print(0,x)
for k in range(8):
    x = g(x)
    print(k+1,x)

#It converges incredibly quickly 
