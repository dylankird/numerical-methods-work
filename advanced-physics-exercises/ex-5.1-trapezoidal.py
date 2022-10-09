from numpy import loadtxt

velocities = loadtxt("velocities.txt", float)

print(velocities[100,1])

h = 1

s = 0.5*velocities[0,1] + 0.5*velocities[100,1]

for k in range(1,100):
    s += velocities[k,1]
    print(k)

print(s*h)


