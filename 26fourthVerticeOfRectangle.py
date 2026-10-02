#Only for axis aligned Rectangles
x1,y1 = map(int, input("Entre (x1, y1)").split())
x2,y2 = map(int, input("Entre (x2, y2)").split())
x3,y3 = map(int, input("Entre (x3, y3)").split())

if(x1==x2):
    x4=x3
elif(x1==x3):
    x4=x2
else:
    x4=x1
if(y1==y2):
    y4=y3
elif(y1==y3):
    y4=y2
else:
    y4=y1

print(f"The co-ordinates of 4th Point is{x4},{y4}")