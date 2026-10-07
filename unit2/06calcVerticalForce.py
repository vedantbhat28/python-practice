import math
force=int(input("Enter Force: "))
angle=int(input("Enter Angle: "))
vertical_force=force*math.sin(math.radians(angle))
print(f"The verticle force is:{vertical_force}")
