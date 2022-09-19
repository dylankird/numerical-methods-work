deltat = 0.005

t = 0
x = 2.5
y = 1

rounding = 4


for k in range(abs(int(x/deltat))):
    #Calculate the rates of change
    yprime = 0.2*y*(5-y)
    #Calculate the deltas
    deltay = yprime * deltat
    #Calculate the new values
    t += deltat
    y += deltay
    #Print new values
    print(round(t, rounding),round(y, rounding),sep='\t')
