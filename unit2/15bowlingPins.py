N=int(input("Enter total pins (N): "))
K=int(input("Enter total balls (K): "))

pins=["I"]*N

for i in range (K):
    start, end = map (int, input(f"Enter range for ball {i+1}: ").split())
    for j in range (start-1, end):
        pins[j]="."
print("".join(pins))