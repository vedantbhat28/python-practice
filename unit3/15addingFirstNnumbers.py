n=int(input("Enter n: "))
if n<=0:
    print("enter a positive number")
else:
    total=0
    for number in range (1, n+1):
        total+=number
    average=total/n
    print(f"Sum:{total}\nAvg:{average}")