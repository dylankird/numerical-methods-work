from numpy import loadtxt
from pylab import plot, show

velocities = loadtxt("velocities.txt", float)

print(velocities[100,1])

h = 1

I = 0

time = [ 0 ]
velocity = [ velocities[0,1] ]
distance = [ 0 ]


for k in range(1,101):
    I += 0.5*(velocities[k-1,1] + velocities[k,1])
    time.append(k)
    velocity.append(velocities[k,1])
    distance.append(I)

plot(time, velocity)
plot(time, distance)
show()

