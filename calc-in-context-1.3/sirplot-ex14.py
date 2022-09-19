from pylab import plot, show

t = 0
S = 45400
I = 2100
R = 2500

deltat = -0.01

a = 0.00001
b = 1/14

tlist = [t]
slist = [S]
ilist = [I]
rlist = [R]

Iprime = a*S*I - b*I

while I >= 1:
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
    #Append lists with new values
    tlist.append(t)
    slist.append(S)
    ilist.append(I)
    rlist.append(R)

print(t - deltat, S, I, R)

#"""
plot(tlist,slist)
plot(tlist,ilist)
plot(tlist,rlist)
show()
#"""
