from math import log,exp

def g(x):
    return 7-exp(x)

x = 1

print(0,x)
for k in range(8):
    x = g(x)
    print(k+1,x)

#It diverges
