deltats = [0.5,0.1,0.05,0.01,0.005,0.001]

rounding = 6

for deltat in deltats:
    t = 0
    x = 2.5
    y = 1
    for k in range(abs(int(x/deltat))):
        #Calculate the rates of change
        yprime = 0.2*y*(5-y)
        #Calculate the deltas
        deltay = yprime * deltat
        #Calculate the new values
        t += deltat
        y += deltay
        #Print new values
    print(deltat,round(y, rounding),sep='\t')

#note: a digit has stabilized when it pops up twice. We can use an answer accurate to that digit.
