#ax²+bx+c
import math
a=float(input("Enter coeff. of x²: "))
b=float(input("Enter coeff. of x: "))
c=float(input("Enter constant: "))
d=b**2-4*a*c
if (d>0):
    root1= (-b + math.sqrt(d))/2*a
    root2= (-b - math.sqrt(d))/2*a
    print(f"Your equation has 2 real roots {root1} & {root2}")
elif(d==0):
    root=(-b)/2*a
    print(f"Your equation has 1 real root {root}")
else:
    realPart=-b
    imagPart=math.sqrt(-d)/(2*a)
    print(f"Your equation has complex roots {realPart}+{imagPart}i  &  {realPart}-{imagPart}i")

