from math import pi

def f(x):
    return x**3 + x - 1

a,b = -1,3
x=.5*(a+b)

for k in range(7):
    x = .5*(a+b)
    print(k,x)
    if f(x)*f(a) < 0:
        b = x
    else:
        a = x

