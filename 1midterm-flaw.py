from math import log

y = log(11) - log(10)

for k in range(25):
    y = 1/(k+1) - 10*y
    print(y)
