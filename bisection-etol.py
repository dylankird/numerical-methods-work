from math import pi

def f(x):
    return x**3 + x - 1

a,b = -1,3
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

