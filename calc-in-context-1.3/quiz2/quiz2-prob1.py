initialt = 0
initialS = 4500
initialI = 100
initialR = 500

deltats = [1, 0.1, 0.01, 0.001, 0.0001]
days = 120

a = 0.0001
b = 0.1

rounding = 4

t = initialt
S = initialS
I = initialI
R = initialR

print(t, S, I, R,sep='\t')

for deltat in deltats:
    t = initialt
    S = initialS
    I = initialI
    R = initialR
    while I <= 1000:
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
    print(deltat,t,round(S, rounding),round(I, rounding),round(R, rounding),sep='\t')

#print(deltat, round(finalS, rounding), round(finalI, rounding), round(finalR, rounding), round(S, rounding), round(abs(initialS - S), rounding))
