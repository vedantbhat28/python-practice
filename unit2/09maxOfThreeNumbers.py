a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if (a>=b) and (a>=c):
    print(f"A is maximum: {a}")
elif(b>=a) and (b>=c):
    print(f"B is maximum: {b}")
else:
    print(f"C is maximum: {c}")