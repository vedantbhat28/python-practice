n=int(input("Enter n: "))
if n<=0:
    print("Enter a positive count")
else:
    factorial=1
    for n in range (1, n+1):
        print(n)