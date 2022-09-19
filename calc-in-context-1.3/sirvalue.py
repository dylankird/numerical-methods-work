tinitial = 0
tfinal = 3
S = 45400
I = 2100
R = 2500

t = tinitial 

numberofsteps = 3000

deltat = (tfinal - tinitial)/numberofsteps

a = 0.00001
b = 1/14

print(t, S, I, R)

for k in range(numberofsteps):
    #Calculate the rates of change
    Sprime = -1*a*S*I
    Iprime = a*S*I - b*I
    Rprime = b*I
    #Calculate the deltas
    deltaS = Sprime * deltat
    deltaI = Iprime * deltat
    deltaR = Rprime * deltat
    #Calculate the new values
    t += deltat
    S += deltaS
    I += deltaI
    R += deltaR
    #Print new values
    print(t,S,I,R)
