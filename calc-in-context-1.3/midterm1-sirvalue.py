initialt = 0
initialS = 4000
initialI = 200
initialR = 100

deltat = 0.1
days = 5

a = 0.00002
b = 0.1

rounding = 9

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
    print(round(t, rounding),round(S, rounding),round(I, rounding),round(R, rounding),S+I+R,sep='\t')

#print(deltat, round(finalS, rounding), round(finalI, rounding), round(finalR, rounding), round(S, rounding), round(abs(initialS - S), rounding))
