from math import cos

def g(x):
    return x**3 - 5*x

x = 2

for k in range(2):
    x = g(x)
    print(k,x)
