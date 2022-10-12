from math import cos

def g(x):
    return 2**((-1)*x)

x = 0

for k in range(41):
    if (x <= 1):
        x = g(x)
        print(k+1,x)
    else:
        print("no fixed point in domain")
        break
