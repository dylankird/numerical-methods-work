import math

T = float(input("Enter the period of the orbit in seconds:"))

G = 6.67 * 10**(-11)
M = 5.97 * 10**24
R = 6371

h = (G*M*T**2 / (4*(math.pi)**2))**(1/3) - R


print("The height of the satellite is",h,"meters.")
