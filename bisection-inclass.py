from math import exp

def f(x):
    return exp(x)+x-7

a,b = 1,2

for k in range(33):
    x = .5*(a+b)
    print(k,x)
    if f(x)*f(a) < 0:
        b = x
    else:
        a = x

