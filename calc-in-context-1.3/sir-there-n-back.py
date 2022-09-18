initialt = 0
initialS = 45400
initialI = 2100
initialR = 2500

deltat = 1
days = 3

a = 0.00001
b = 1/14

rounding = 3

t = initialt
S = initialS
I = initialI
R = initialR

print(t, S, I, R)

for k in range(int(days/deltat)):
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
    print(round(t, rounding),round(S, rounding),round(I, rounding),round(R, rounding))

for k in range(int(days/deltat)):
    #Calculate the rates of change
    Sprime = -1*a*S*I
    Iprime = a*S*I - b*I
    Rprime = b*I
    #Calculate the deltas
    deltaS = Sprime * deltat * -1
    deltaI = Iprime * deltat * -1
    deltaR = Rprime * deltat * -1
    #Calculate the new values
    t -= deltat
    S += deltaS
    I += deltaI
    R += deltaR
    #Print new values
    print(round(t, rounding),round(S, rounding),round(I, rounding),round(R, rounding))