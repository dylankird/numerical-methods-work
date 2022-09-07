#Exercise 2.1 (page 22 of the pdf)

from math import sqrt

h = float(input("Enter the height of the tower: "))
g = 9.81
t = sqrt(2*h/g)
print("The ball hits the ground at t=",t,sep="")
