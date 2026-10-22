value=int(input("Enter a number: "))
n=int(input("Enter a positive count: "))
if n<=0:
    print("Enter a positive number")
else:
    for multipler in range (1, n+1):
        print(value*multipler)