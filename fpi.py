from math import cos

def g(x):
    return cos(x)

x = 0

for k in range(41):
    x = g(x)
    print(k+1,x)
