from pylab import plot,show


t = 0
endt = 3

h = 0.2

d = 0
v = 10
dv = 32

ts = [0]
ds = [0]
vs = [10]


for k in range(int(endt/h)):
    d += v*h
    v += dv*h
    t += h
    ts.append(t)
    ds.append(d)
    vs.append(v)
    print(k,t,d,v)

plot(ts,ds)
plot(ts,vs)
show()
