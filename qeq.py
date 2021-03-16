import math
import cmath

a = float(input("podaj a: "))
b = float(input("podaj b: "))
c = float(input("podaj c: "))
delta2 = b**2-4*a*c
if delta2>=0:
    delta = math.sqrt(delta2)
    x1 = (-b+delta)/(2*a)
    x2 = (-b-delta)/(2*a)
    print("rozwiązania równania kwadratowego ax^2+bx+c=0 to {0:.2f}, oraz {1:.2f}".format(x1,x2))
else:
    x1 = (-b + cmath.sqrt(delta2) ) / (2*a)
    x2 = (-b - cmath.sqrt(delta2) ) / (2*a)
    print("rozwiązania równania kwadratowego ax^2+bx+c=0 to {0:.2f}, oraz {1:.2f}".format(x1,x2))