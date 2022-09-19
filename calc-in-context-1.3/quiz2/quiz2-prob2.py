deltats = [0.001]

rounding = 6

for deltat in deltats:
    t = 5
    x = 20
    R = 3750
    for k in range(abs(int((x-t)/deltat))):
        #Calculate the rates of change
        Rprime = 0.005*R
        #Calculate the deltas
        deltaR = Rprime * deltat
        #Calculate the new values
        t += deltat
        R += deltaR
        #Print new values
        print(t,round(R, rounding),sep='\t')

#note: a digit has stabilized when it pops up twice. We can use an answer accurate to that digit.
