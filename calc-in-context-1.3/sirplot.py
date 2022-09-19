from pylab import plot, show

t = 0
S = 45400
I = 2100
R = 2500

deltat = 0.01
days = 20

a = 0.00001
b = 1/14

tlist = [t]
slist = [S]
ilist = [I]
rlist = [R]

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
    #Append lists with new values
    tlist.append(t)
    slist.append(S)
    ilist.append(I)
    rlist.append(R)

plot(tlist,slist)
plot(tlist,ilist)
plot(tlist,rlist)
show()
