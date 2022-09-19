deltats = [0.2]

rounding = 6

for deltat in deltats:
    t = 10
    x = 11
    y = 0.2
    for k in range(abs(int((x-t)/deltat))):
        #Calculate the rates of change
        yprime = 2*y*(1-y)
        #Calculate the deltas
        deltay = yprime * deltat
        #Calculate the new values
        t += deltat
        y += deltay
        #Print new values
        print(t,round(y, rounding),sep='\t')

#note: a digit has stabilized when it pops up twice. We can use an answer accurate to that digit.
