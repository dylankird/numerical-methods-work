t = 0
S = 45400
I = 2100
R = 2500

deltat = 1

a = 0.00001
b = 1/14

print(t, S, I, R)

for k in range(3):
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
print("Done")
