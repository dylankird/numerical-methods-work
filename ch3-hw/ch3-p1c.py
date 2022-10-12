from math import cos

def g(x):
    return 1/x

x = 0.5

for k in range(41):
    if (x <= 5.2):
        x = g(x)
        print(k+1,x)
    else:
        print("no fixed point in domain")
        break
