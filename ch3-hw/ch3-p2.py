from math import cos

def g(x):
    return -4 + 4*x-x**2/2

x = 3.8

for k in range(41):
    x = g(x)
    print(k+1,x)
