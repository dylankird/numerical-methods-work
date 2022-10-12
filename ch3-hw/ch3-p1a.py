from math import cos

def g(x):
    return 1 - x**2/4

x = 0

for k in range(41):
    if (x <= 1):
        x = g(x)
        print(k+1,x)
    else:
        print("no fixed point in domain")
        break
