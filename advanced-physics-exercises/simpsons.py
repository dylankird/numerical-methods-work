def f(x):
    return x**4 - 2*x + 1

N = 100
a = 0.0
b = 2.0
h = (b-a)/N

s = f(a) + f(b)

for k in range(1,N,2):
    s += 4*f(a+k*h)

for k in range(2,N,2):
    s += 2*f(a+k*h)

print(h*s/3)
print(abs(4.4-(h*s/3)))

#The error is O(h^4)
