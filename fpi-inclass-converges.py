from math import log,exp

def g(x):
    return log(7-x)

x = 1

print(0,x)
for k in range(8):
    x = g(x)
    print(k+1,x)

#It diverges
