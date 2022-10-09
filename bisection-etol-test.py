from math import pi

def f(x):
    return x**7

a,b = -1,pi
x=.5*(a+b)

etol = 0.5*10e-9
k = 0

while abs(f(x)) > etol:
    x = .5*(a+b)
    print(k,x)
    if f(x)*f(a) < 0:
        b = x
    else:
        a = x
    k += 1

#This is a bad approach - we might think that we have a very small error, but actually the function flattens out so much that we think we've gotten the root, but we haven't. Some small number to the 7th power is very small!
