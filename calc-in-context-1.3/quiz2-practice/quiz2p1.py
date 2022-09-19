initialt = 0
initialS = 45400
initialI = 2100
initialR = 2500

deltat = 0.25
days = 120

a = 0.00001
b = 1/14

rounding = 4

t = initialt
S = initialS
I = initialI
R = initialR

print(t, S, I, R,sep='\t')

for k in range(abs(int(days/deltat))):
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
    print(round(t, rounding),round(S, rounding),round(I, rounding),round(R, rounding),sep='\t')

#print(deltat, round(finalS, rounding), round(finalI, rounding), round(finalR, rounding), round(S, rounding), round(abs(initialS - S), rounding))
