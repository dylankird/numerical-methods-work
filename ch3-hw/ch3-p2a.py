from math import cos

def g(x):
    return -4 + 4*x - (x**2)/2

x = 1.9

actual = 2.0
rounding = 6

print("Iteration\tX Value\tAbs. Error\tRel. Error")
print(0, round(x, rounding),  round(abs(actual-x), rounding), round(abs((actual-x)/actual), rounding),sep="\t")
for k in range(10):
    x = g(x)
    print(k+1, round(x, rounding),  round(abs(actual-x), rounding), round(abs((actual-x)/actual), rounding),sep="\t")
