import math
a=int(input("Students in Class 1: "))
b=int(input("Students in Class 2: "))
c=int(input("Students in Class 3: "))
desk1=math.ceil(a/2)
desk2=math.ceil(b/2)
desk3=math.ceil(c/2)
total=desk1+desk2+desk3
print(f"Total Number of desks required:{total}")