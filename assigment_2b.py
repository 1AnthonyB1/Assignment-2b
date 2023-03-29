import math
pi = math.pi
d = float(input("What is the diamatre of your circle? "))
r = (float(d)/2)

print("This is the Radius:",float(r))

rsquared = float(r**2)
print("This is the Area:",pi*rsquared)

twopi = (2*pi)
print("This is the circumference:",twopi*r)